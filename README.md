# Spectrum Arch, Inc. website (spectrumarch.org)

A plain static site: HTML, CSS and one small JavaScript file. There's no build step, no database and no server code. It's meant for **Azure Static Web Apps**.

```
./
├── index.html, about.html, services.html, resources.html,
│   get-involved.html, contact.html, 404.html
├── assets/css/site.css      calm, low-sensory styling (light + dark mode)
├── assets/js/site.js        mobile menu toggle only
├── assets/img/logo.svg
├── staticwebapp.config.json security headers, 404 page, caching
├── robots.txt, sitemap.xml
└── deploy.sh                deploy from your own computer (no GitHub needed)
```

Preview locally: open `index.html` in a browser, or run `npx serve .` (or `swa start .`) and visit the address it prints.

---

## Do I need GitHub?

**No.** Azure Static Web Apps accepts a deploy straight from a folder on your computer. You have two options:

| | Option A: local folder (no GitHub) | Option B: private GitHub repo |
|---|---|---|
| Where the files live | Your PC or company file share | A private GitHub repository |
| How you publish | Run `./deploy.sh` | Automatic on every push |
| Change history / undo | Only if you back it up yourself | Full history, easy rollback |
| Secrets to protect | The deployment token on your PC | The deployment token in GitHub's encrypted secrets |

**What "security" means for this site:** every page on a public website can be read by anyone. Hosting the source files locally doesn't hide the website. It only controls who can *change* it. The things that really need protecting are:

1. **The Azure deployment token.** Anyone who has it can replace the site. Keep it in a password manager and never commit it to a repo or email it. If it leaks, reset it in the portal.
2. **Your Azure account.** Turn on multi-factor authentication. Give only the people who need it access to the resource group.
3. **Private information.** Don't put donor lists, family case notes, board documents or ID numbers in this folder. Everything here is meant to be public.

Recommendation: keep the working copy on your computer and deploy with **Option A**. If more than one person will edit the site, move it into its own **private** GitHub repository (Option B) for history and review. Either is secure if the token is kept secret.

---

## Step 1: Create the Static Web App in Azure (one time)

1. Sign in to <https://portal.azure.com>.
2. **Create a resource → Static Web App**.
3. Fill in the form:
   - **Resource group:** new, e.g. `rg-spectrumarch`
   - **Name:** `spectrumarch`
   - **Plan type:** *Free* is enough for this site. Choose *Standard* if you later need an SLA, private endpoints or password-protected staging.
   - **Deployment source:** **Other**. This is the setting that avoids connecting GitHub.
4. **Review + create**. When it finishes, open the resource and copy its default URL (something like `https://<random-name>.azurestaticapps.net`).

## Step 2A: Deploy from your computer (no GitHub)

```bash
# one-time: install Node.js LTS, then
npm install -g @azure/static-web-apps-cli

# each deploy
export SWA_CLI_DEPLOYMENT_TOKEN='<Azure portal → Static Web App → Overview → Manage deployment token>'
./deploy.sh
```

On Windows PowerShell, run `$env:SWA_CLI_DEPLOYMENT_TOKEN='...'` and then `swa deploy . --env production`. `deploy.sh` only uploads the public files, so `README.md` and `deploy.sh` are never published.

## Step 2B (alternative): Deploy automatically from this private repo

The workflow in `.github/workflows/azure-static-web-apps.yml` publishes the site every time `main` changes. You can also start it by hand from the **Actions** tab (**Run workflow**). It uploads only the public site files.

One-time setup: in this repo, go to **Settings → Secrets and variables → Actions → New repository secret**. Name it `AZURE_STATIC_WEB_APPS_API_TOKEN` and paste the deployment token as the value. Until the secret exists, the workflow stops with a message telling you to add it.

## Step 3: Connect spectrumarch.org

In the Static Web App, go to **Settings → Custom domains → + Add**.

**`www.spectrumarch.org`**: at your DNS provider, add a `CNAME` record for `www` pointing to `<random-name>.azurestaticapps.net`.

**`spectrumarch.org` (apex/root)**: choose one:
- **Easiest and most secure: move DNS to Azure DNS.** Create a DNS zone for `spectrumarch.org`, change the name servers at your registrar to the four Azure name servers, then choose **Custom domain on Azure DNS**. Azure creates the TXT and ALIAS records for you.
- **Keep your current DNS provider:** choose **Custom domain on other DNS**, pick **TXT** validation, add the TXT record at `@`, then add an `ALIAS`/`ANAME` record at `@` pointing to `<random-name>.azurestaticapps.net`. Some registrars, including GoDaddy, don't support ALIAS records. In that case, forward the apex to `https://www.spectrumarch.org` or use Azure DNS.

Azure provides and renews the HTTPS certificate automatically. DNS changes can take up to 72 hours.

**Email:** if you use Microsoft 365 or Google Workspace for `@spectrumarch.org` mail, keep those MX, SPF, DKIM and DMARC records when you change DNS.

---

## Editing pages and writing blog posts

All pages are generated by `tools/build.py`. Don't edit the `.html` files at the root by hand; change `tools/build.py` (or a post file) and run:

```bash
python3 tools/build.py
```

**Blog posts** live in `content/blog/<slug>.html`. Copy an existing post, update the header block (title, description, date, author, tags), write the body in simple HTML, and set `status: published` when it is ready. Anything else (for example `status: draft`) is left out of the site. The blog index, post pages, and `sitemap.xml` update automatically.

The topic plan and writing rules are in `docs/blog-calendar.md`. `tools/`, `content/`, and `docs/` are never deployed.

## Security measures built into the site

- `staticwebapp.config.json` sends strict headers on every page: Content-Security-Policy (only files from this site can run), HSTS (forces HTTPS), `X-Frame-Options: DENY` (stops clickjacking), `nosniff`, a strict Referrer-Policy and a locked-down Permissions-Policy.
- There are no third-party scripts, trackers, fonts or CDNs, so nothing outside your control runs on the site.
- There are no forms and no data collection. Contact happens by email, and the contact page asks people not to email medical records.

If you later add a script, such as a donation widget or analytics, you must also allow its domain in the `Content-Security-Policy` header. Otherwise the browser will block it.

## Before going live

- [ ] **Content review.** Check the wording on every page, especially the Capital District need figures on the home page and the opening timeline on `about.html`.
- [ ] **Mailing address.** `contact.html` lists 29 Westbury Court as the mailing address. If that's a private residence, consider a PO box.
- [ ] **Donations.** The Donate card asks people to get in touch. Add a link to your payment provider when you have one.
- [ ] **Photos.** Add photos to `assets/img/` if you like. Get written consent before showing any resident or family member.

**Financial information is intentionally left off the site** (revenue projections, Medicaid rates, budgets). Keep it out of this repo too, because anything in this folder can end up published.
