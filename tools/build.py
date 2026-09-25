"""Generates every page of spectrumarch.org. Run: python3 tools/build.py"""
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.spectrumarch.org"
EMAIL = "info@spectrumarch.org"
PHONE = "317-991-0361"
TEL = "+13179910361"
EIN = "42-3421753"

NAV = [("index.html","Home"),("about.html","About"),("services.html","Services"),("support-brokerage.html","Support Brokerage"),
       ("blog.html","Blog"),("resources.html","Resources"),("get-involved.html","Get Involved"),("contact.html","Contact")]

ICON = {
 "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>',
 "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M15 14.5c2.8 0 5 2.2 5 5"/></svg>',
 "path": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20V11a8 8 0 0 1 16 0v9"/><path d="M9 20v-8a3 3 0 0 1 6 0v8"/></svg>',
 "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5"/></svg>',
 "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg>',
 "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5h16v11H9l-5 4z"/></svg>',
}

def page(fname, title, desc, body, head_extra="", noindex=False, full_title=None):
    cur = ' aria-current="page"'
    nav = "\n".join(
        f'        <li><a href="/{"" if h=="index.html" else h}"{cur if h==fname else ""}>{t}</a></li>'
        for h,t in NAV)
    canon = SITE + "/" + ("" if fname=="index.html" else fname)
    if full_title is None:
        full_title = "Spectrum Arch, Inc. — Building the Arch to Independence" if fname=="index.html" else f"{title} | Spectrum Arch, Inc."
    if noindex:
        seo = '  <meta name="robots" content="noindex">\n'
    else:
        seo = f'  <link rel="canonical" href="{canon}">\n'
    og_url = "" if noindex else f'  <meta property="og:url" content="{canon}">\n'
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
{seo}  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
{og_url}  <meta property="og:type" content="website">
  <meta property="og:image" content="https://www.spectrumarch.org/assets/icons/icon-512.png">
  <meta name="theme-color" content="#2f6f8f">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="icon" href="/assets/icons/icon-192.png" type="image/png" sizes="192x192">
  <link rel="apple-touch-icon" href="/assets/icons/icon-180.png">
  <link rel="stylesheet" href="/assets/css/site.css">
  <script src="/assets/js/site.js" defer></script>
{head_extra}</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>

  <header class="site-header">
    <div class="container">
      <a class="brand" href="/"><img src="/assets/img/logo.svg" alt="" width="40" height="40">Spectrum Arch, Inc.</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav id="site-nav" class="site-nav" aria-label="Main">
        <ul>
{nav}
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="container">
      <div>
        <h2>Spectrum Arch, Inc.</h2>
        <p>Building the Arch to Independence. Person-centered residential services for adults with autism and developmental disabilities in Saratoga County and the Capital District.</p>
      </div>
      <div>
        <h2>Explore</h2>
        <ul>
          <li><a href="/services.html">Services</a></li>
          <li><a href="/support-brokerage.html">Support Brokerage</a></li>
          <li><a href="/resources.html">Resources</a></li>
          <li><a href="/get-involved.html">Get involved</a></li>
          <li><a href="/blog.html">Blog</a></li>
          <li><a href="/privacy.html">Privacy</a></li>
          <li><a href="/accessibility.html">Accessibility</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:{TEL}">{PHONE}</a></li>
          <li>Clifton Park, NY 12065</li>
        </ul>
      </div>
      <p class="legal">&copy; <span id="year">2026</span> Spectrum Arch, Inc. Spectrum Arch is a 501(c)(3) nonprofit organization (EIN {EIN}). Donations are tax-deductible to the extent allowed by law. This website shares general information and is not medical or legal advice.</p>
    </div>
  </footer>
</body>
</html>
'''
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)

def card(icon, h, p):
    return f'''        <div class="card">
          <div class="icon">{ICON[icon]}</div>
          <h3>{h}</h3>
          <p>{p}</p>
        </div>'''

ICON["shield"]='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/></svg>'
ICON["pulse"]='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12h4l3-7 4 14 3-7h4"/></svg>'
ICON["check"]='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 11l3 3 8-8"/><path d="M20 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>'

STATUS = '''        <div class="callout">
          <h3>Opening in 2027</h3>
          <p>Spectrum Arch is seeking OPWDD certification as a residential services provider, and we expect our first home to open in early 2027. We are not accepting placements yet, but families, care managers, and referral sources are welcome to <a href="/contact.html">contact us</a> now to join our interest list.</p>
        </div>'''

ORG_LD = '  <script type="application/ld+json">\n  {\n    "@context": "https://schema.org",\n    "@type": "NGO",\n    "name": "Spectrum Arch, Inc.",\n    "alternateName": "Spectrum Arch",\n    "slogan": "Building the Arch to Independence",\n    "url": "https://www.spectrumarch.org/",\n    "logo": "https://www.spectrumarch.org/assets/icons/icon-512.png",\n    "description": "Person-centered, community-integrated residential services for adults with autism spectrum disorder and developmental disabilities in Saratoga County and the Capital District of New York.",\n    "nonprofitStatus": "Nonprofit501c3",\n    "taxID": "42-3421753",\n    "foundingDate": "2026-06-15",\n    "email": "info@spectrumarch.org",\n    "telephone": "+1-317-991-0361",\n    "address": {\n      "@type": "PostalAddress",\n      "streetAddress": "29 Westbury Court",\n      "addressLocality": "Clifton Park",\n      "addressRegion": "NY",\n      "postalCode": "12065",\n      "addressCountry": "US"\n    },\n    "areaServed": ["Saratoga County, NY", "Capital District, NY"],\n    "founder": { "@type": "Person", "name": "Asad M. Butt" }\n  }\n  </script>\n'

# ---------------- Home ----------------
page("index.html", "Home",
 "Spectrum Arch, Inc. provides person-centered, community-integrated residential services for adults with autism and developmental disabilities in Saratoga County and the Capital District, NY.",
f'''    <section class="hero">
      <div class="container">
        <div>
          <span class="eyebrow">Building the Arch to Independence</span>
          <h1>A home, a community, and a future for adults with autism</h1>
          <p class="lead">Spectrum Arch provides safe, person-centered, community-integrated residential services that enable adults with autism spectrum disorder and developmental disabilities to live with dignity, independence, and purpose.</p>
          <div class="btn-row">
            <a class="btn btn-primary" href="/contact.html">Join our interest list</a>
            <a class="btn btn-ghost" href="/services.html">Our services</a>
          </div>
        </div>
        <img class="hero-art" src="/assets/img/logo.svg" alt="">
      </div>
    </section>

    <section class="section alt">
      <div class="container grid grid-2">
        <div>
          <span class="eyebrow">The need</span>
          <h2>At 21, school services end. Too often, there is nowhere to go next.</h2>
          <p>When young adults with autism turn 21, school-based services stop, and many families find there are no residential options waiting. Adults stay at home with parents who are now in their 70s and 80s, with no plan for the future.</p>
        </div>
        <div class="grid">
          <div class="card"><p class="stat">200&ndash;300</p><p>young adults aged 21&ndash;30 with autism in the Capital District estimated to need residential support</p></div>
          <div class="card"><p class="stat">Fewer than 50</p><p>residential openings currently available in the region</p></div>
          <div class="card"><p class="stat">18&ndash;36 months</p><p>typical OPWDD waitlist for residential services</p></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <span class="eyebrow">What we do</span>
        <h2>Individual Residential Alternative (IRA) homes</h2>
        <p class="lead">Homes in ordinary residential neighborhoods for 5&ndash;8 adults each, with trained staff on hand 24 hours a day, every day of the year.</p>
        <div class="grid grid-2">
{card("home","Residential support","Round-the-clock care, help with daily living skills, and positive behavioral support.")}
{card("pulse","Health &amp; wellness","Health care coordination, medication management, and preventive care.")}
{card("people","Community &amp; employment","Taking part in community life, and supported employment for residents who want to work.")}
{card("check","Person-centered planning","A service plan built around each person, regular communication with families, and quarterly reviews.")}
        </div>
        <div class="btn-row"><a class="btn btn-ghost" href="/services.html">Learn more about our services</a></div>
      </div>
    </section>

    <section class="section alt">
      <div class="container grid grid-2">
        <div>
          <span class="eyebrow">Self-Direction</span>
          <h2>Support Brokerage for families who self-direct</h2>
          <p>OPWDD Self-Direction lets people with developmental disabilities choose their own supports, staff, and schedule. A Support Broker helps you plan, build a budget, and put it all in place. Spectrum Arch is preparing to offer Support Brokerage across the Capital Region.</p>
          <div class="btn-row">
            <a class="btn btn-primary" href="/support-brokerage.html">About Support Brokerage</a>
            <a class="btn btn-ghost" href="/self-direction-guide.html">Self-Direction guide</a>
          </div>
        </div>
        <div class="card">
          <h3>Common questions</h3>
          <ul class="list-plain">
            <li><a href="/support-broker-faq.html#what-does-a-support-broker-do">What does a Support Broker do?</a></li>
            <li><a href="/support-broker-faq.html#how-much-does-it-cost">Do families pay for Support Brokerage?</a></li>
            <li><a href="/support-broker-faq.html#how-do-i-get-started">How do I get started with Self-Direction?</a></li>
            <li><a href="/support-broker-capital-region.html">Which counties do you serve?</a></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
{STATUS}
      </div>
    </section>
''', head_extra=ORG_LD)

# ---------------- About ----------------
page("about.html", "About us",
 "About Spectrum Arch, Inc.: our mission, vision, board of directors, and organizational status.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">About us</span>
        <h1>Building the Arch to Independence</h1>
        <p class="lead">Spectrum Arch, Inc. is a New York nonprofit based in Clifton Park that is creating community homes for adults with autism spectrum disorder and developmental disabilities.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container grid grid-2">
        <div class="card">
          <h2>Our mission</h2>
          <p>Spectrum Arch provides safe, person-centered, community-integrated residential services that enable adults with autism spectrum disorder and developmental disabilities to live with dignity, independence, and purpose.</p>
        </div>
        <div class="card">
          <h2>Our vision</h2>
          <p>To become the Capital District's leading provider of high-quality, innovative residential services that reflect best practices in autism support and developmental disabilities services.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Board of directors</h2>
        <div class="grid grid-3">
          <div class="card"><h3>Asad M. Butt</h3><p>President and Founder</p></div>
          <div class="card"><h3>Tyrone Crooks</h3><p>Director (Independent)</p></div>
          <div class="card"><h3>Khalid Rehman</h3><p>Director (Independent)</p></div>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container grid grid-2">
        <div>
          <h2>Our organization</h2>
          <ul class="list-plain">
            <li><strong>Legal status:</strong> 501(c)(3) tax-exempt nonprofit corporation</li>
            <li><strong>EIN:</strong> {EIN}</li>
            <li><strong>Incorporated:</strong> New York State, June 15, 2026</li>
            <li><strong>IRS 501(c)(3) determination:</strong> July 2, 2026</li>
            <li><strong>Service area:</strong> Saratoga County, expanding across the Capital District</li>
          </ul>
        </div>
        <div>
          <h2>Governance and readiness</h2>
          <ul class="check-list">
            <li>IRS-approved 501(c)(3) tax-exempt status</li>
            <li>New York State nonprofit incorporation</li>
            <li>Board of directors with independent members</li>
            <li>Corporate bylaws adopted</li>
            <li>Conflict of interest policy adopted</li>
            <li>Comprehensive business plan completed</li>
            <li>Compliance framework designed</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Our goals</h2>
        <div class="grid grid-2">
{card("home","Open our first IRA home","Open a six-person Individual Residential Alternative home in Saratoga County, with 24/7 staff, and grow to more homes across the Capital District.")}
{card("path","Offer Support Brokerage","Help families who self-direct their OPWDD services plan, budget, and hire staff. We are in the process of offering Support Brokerage now.")}
{card("check","Become a Fiscal Intermediary","In the future, seek OPWDD approval as a Fiscal Intermediary, so families can self-direct with one trusted local partner handling payroll and budget tracking.")}
{card("book","Educate and connect families","Publish clear, practical guides on adult services in New York, and connect families with the right local resources.")}
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>Our path to opening</h2>
        <ol class="timeline">
          <li><strong>Fall 2026</strong> &mdash; OPWDD new provider orientation and application for certification as a residential operator</li>
          <li><strong>Late 2026</strong> &mdash; OPWDD review and certification</li>
          <li><strong>Early 2027</strong> &mdash; First home opens in Saratoga County, serving 6 residents</li>
          <li><strong>Years 2&ndash;3</strong> &mdash; Additional homes across the Capital District</li>
        </ol>
      </div>
    </section>
''')

# ---------------- Services ----------------
page("services.html", "Services",
 "Spectrum Arch Individual Residential Alternative (IRA) homes: 24/7 residential support, health and wellness, community integration, and person-centered planning for adults 21+.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Services</span>
        <h1>Individual Residential Alternative (IRA) homes</h1>
        <p class="lead">Community homes where adults with autism and developmental disabilities live together with trained staff support, in typical residential neighborhoods close to community resources.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>Who we serve</h2>
        <div class="grid grid-3">
          <div class="card"><h3>Adults 21 and older</h3><p>People with autism spectrum disorder and related developmental disabilities who are eligible for OPWDD services.</p></div>
          <div class="card"><h3>5&ndash;8 residents per home</h3><p>Small homes, so every resident gets personal attention and a real sense of home.</p></div>
          <div class="card"><h3>24/7, all year</h3><p>Trained Direct Support Professionals on site at all times, including overnight.</p></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>What each resident receives</h2>
        <div class="grid grid-2">
          <div class="card">
            <div class="icon">{ICON["home"]}</div>
            <h3>1. Residential support services</h3>
            <ul class="check-list">
              <li>Care and supervision 24 hours a day</li>
              <li>Help with daily living: cooking, household tasks, personal care, and money skills</li>
              <li>Positive behavioral support</li>
            </ul>
          </div>
          <div class="card">
            <div class="icon">{ICON["pulse"]}</div>
            <h3>2. Health and wellness support</h3>
            <ul class="check-list">
              <li>Coordination with doctors, specialists, and clinicians</li>
              <li>Medication management</li>
              <li>Preventive care and healthy routines</li>
            </ul>
          </div>
          <div class="card">
            <div class="icon">{ICON["people"]}</div>
            <h3>3. Community integration and employment</h3>
            <ul class="check-list">
              <li>Regular participation in community life</li>
              <li>Supported employment for residents who want to work</li>
              <li>Friendships, recreation, and local connections</li>
            </ul>
          </div>
          <div class="card">
            <div class="icon">{ICON["check"]}</div>
            <h3>4. Person-centered planning</h3>
            <ul class="check-list">
              <li>An individualized service plan for each resident</li>
              <li>Ongoing communication with families</li>
              <li>Quarterly reviews of goals and progress</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <div class="callout">
          <h2>Self-directing instead?</h2>
          <p>Not every family chooses a residential home. If you are directing your own services through OPWDD Self-Direction, see our <a href="/support-brokerage.html">Support Brokerage</a> page and <a href="/self-direction-guide.html">step-by-step Self-Direction guide</a>.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container grid grid-2">
        <div>
          <h2>Where we serve</h2>
          <p>Our first home will be in <strong>Saratoga County</strong>. We plan to expand across the Capital District, including Albany, Schenectady, Troy, and the surrounding counties.</p>
        </div>
{STATUS}
      </div>
    </section>
''')

# ---------------- Resources ----------------
def res(name, url, desc):
    return f'''        <div class="resource-item">
          <h3><a href="{url}" rel="noopener" target="_blank">{name}</a></h3>
          <p>{desc}</p>
        </div>'''

page("resources.html", "Resources",
 "Trusted resources for families of adults with autism and developmental disabilities in New York State.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Resources</span>
        <h1>Trusted places to start</h1>
        <p class="lead">Planning for adult services takes time. These well-established organizations and public programs can help. Spectrum Arch is not affiliated with them. Links open in a new tab.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <div class="callout callout-spaced">
          <p><strong>In an emergency, call 911.</strong> For a mental-health crisis, call or text <strong>988</strong> (Suicide &amp; Crisis Lifeline).</p>
        </div>

        <div class="resource-group">
          <h2>New York State services</h2>
{res("NYS Office for People With Developmental Disabilities (OPWDD)","https://opwdd.ny.gov","The state agency for services and supports for people with developmental disabilities, including residential services. Start here to check eligibility (the &ldquo;front door&rdquo;).")}
        </div>

        <div class="resource-group">
          <h2>Capital Region</h2>
{res("Center for Autism and Related Disabilities (CARD) at the University at Albany","https://www.albany.edu/autism","Training, consultation, and information for families and professionals in the region.")}
        </div>

        <div class="resource-group">
          <h2>National information and advocacy</h2>
{res("Autism Society of America","https://autismsociety.org","Information, a national helpline, and a network of local affiliates.")}
{res("Autistic Self Advocacy Network","https://autisticadvocacy.org","An organization run by and for autistic people, with plain-language guides on rights and self-advocacy.")}
{res("Center for Parent Information and Resources","https://www.parentcenterhub.org","Helps families find their state's Parent Training and Information Center, including help planning the transition from school to adult life.")}
        </div>
      </div>
    </section>
''')

# ---------------- Get involved ----------------
page("get-involved.html", "Get involved",
 "Support Spectrum Arch, Inc., a 501(c)(3) nonprofit building community homes for adults with autism in the Capital District.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Get involved</span>
        <h1>Help us build the arch</h1>
        <p class="lead">Every home we open is a place where adults with autism can live with dignity and purpose, and where families can finally plan for the future.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container grid grid-3">
{card("heart","Donate","Spectrum Arch, Inc. is a 501(c)(3) nonprofit (EIN " + EIN + "). Donations are tax-deductible to the extent allowed by law. Contact us to find out how to give.")}
{card("people","Join our team","We will be hiring Direct Support Professionals ahead of our 2027 opening. If you want meaningful work supporting adults with autism, get in touch.")}
{card("path","Partner with us","Care managers, clinicians, schools, employers, and community groups: help us build strong connections for our residents.")}
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Ready to help?</h2>
        <p>Email or call us and tell us how you'd like to get involved. We'll reply with next steps.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="mailto:{EMAIL}?subject=Getting%20involved%20with%20Spectrum%20Arch">Email us</a>
          <a class="btn btn-ghost" href="tel:{TEL}">Call {PHONE}</a>
        </div>
      </div>
    </section>
''')

# ---------------- Contact ----------------
page("contact.html", "Contact",
 "Contact Spectrum Arch, Inc. in Clifton Park, NY about residential services, referrals, employment, and partnerships.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Contact</span>
        <h1>Get in touch</h1>
        <p class="lead">Families, care managers, referral sources, job seekers, and partners are all welcome to reach out.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container grid grid-3">
        <div class="card">
          <div class="icon">{ICON["chat"]}</div>
          <h3>Email</h3>
          <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <div class="card">
          <div class="icon">{ICON["chat"]}</div>
          <h3>Phone</h3>
          <p><a href="tel:{TEL}">{PHONE}</a></p>
        </div>
        <div class="card">
          <div class="icon">{ICON["home"]}</div>
          <h3>Mailing address</h3>
          <p>Spectrum Arch, Inc.<br>29 Westbury Court<br>Clifton Park, NY 12065</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container grid grid-2">
{STATUS}
        <div class="callout">
          <h3>Please protect your privacy</h3>
          <p>Don't email medical records, Medicaid numbers, or other ID numbers. A short description of what you need is enough to start, and we'll arrange a secure way to share details if needed.</p>
        </div>
      </div>
    </section>
''')

# ---------------- 404 ----------------
page("404.html", "Page not found", "The page you were looking for could not be found.",
'''    <section class="section">
      <div class="container">
        <h1>We couldn't find that page</h1>
        <p class="lead">The link may be old or mistyped.</p>
        <div class="btn-row"><a class="btn btn-primary" href="/">Go to the home page</a></div>
      </div>
    </section>
''', noindex=True)

# =====================================================================
# Support Brokerage section
# =====================================================================
import json

# One place to change once OPWDD approval for Support Brokerage is in hand.
SB_STATUS = '''        <div class="callout">
          <h3>Support Brokerage: in process</h3>
          <p>Spectrum Arch is in the process of offering Support Brokerage in Saratoga County and across the Capital Region. We are not accepting Self-Direction clients yet. Families and Care Managers can <a href="/contact.html">contact us</a> to join our interest list.</p>
        </div>'''

SB_LINKS = '''        <div class="grid grid-3">
          <a class="card card-link" href="/support-brokerage.html"><h3>Support Brokerage</h3><p>What a Support Broker does and how we help.</p></a>
          <a class="card card-link" href="/self-direction-guide.html"><h3>Self-Direction guide</h3><p>Every step, from OPWDD eligibility to hiring staff.</p></a>
          <a class="card card-link" href="/support-broker-faq.html"><h3>Questions and answers</h3><p>Cost, timing, choosing a broker, and more.</p></a>
        </div>'''

def ld(obj):
    return '  <script type="application/ld+json">\n' + json.dumps(obj, indent=2) + '\n  </script>\n'

def crumbs(*items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + u}
                                for i, (n, u) in enumerate(items)]}

COUNTIES = [
    ("Saratoga County", "Saratoga Springs, Clifton Park, Halfmoon, Malta, Ballston Spa, Wilton, Mechanicville, and Waterford"),
    ("Albany County", "Albany, Colonie, Latham, Guilderland, Bethlehem, Delmar, Cohoes, and Watervliet"),
    ("Schenectady County", "Schenectady, Niskayuna, Glenville, Scotia, and Rotterdam"),
    ("Rensselaer County", "Troy, Rensselaer, East Greenbush, North Greenbush, and Brunswick"),
    ("Warren County", "Glens Falls, Queensbury, and Lake George"),
    ("Washington County", "Hudson Falls, Fort Edward, Greenwich, and Granville"),
    ("Columbia County", "Hudson, Chatham, Kinderhook, and Valatie"),
    ("Greene County", "Catskill, Coxsackie, and Cairo"),
]

# ---------------- Support Brokerage (pillar) ----------------
page("support-brokerage.html", "Support Broker Services in Albany & the Capital Region, NY",
 "Support Broker services for OPWDD Self-Direction in Albany, Saratoga, Schenectady, Troy, and the Capital Region of New York. Learn how a Support Broker helps you plan, budget, and hire staff.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Support Brokerage &middot; OPWDD Self-Direction</span>
        <h1>Support Broker services in New York's Capital Region</h1>
        <p class="lead">Self-Direction puts people with developmental disabilities and their families in charge of their own supports. A Support Broker is your guide through it: planning, budgeting, hiring, and keeping everything running smoothly.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="/contact.html">Join our interest list</a>
          <a class="btn btn-ghost" href="/self-direction-guide.html">Read the Self-Direction guide</a>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container grid grid-2">
        <div>
          <h2>What is a Support Broker?</h2>
          <p>In New York, people who are eligible for OPWDD services can choose <strong>Self-Direction</strong>. Instead of fitting into an agency's schedule, you decide which supports you need, who provides them, and when.</p>
          <p>A <strong>Support Broker</strong> helps you make that happen. Your broker works for you: helping you understand your options, turn your goals into a self-direction plan and budget, and put the people and services in place to carry it out.</p>
          <p>People who self-direct with <strong>Budget Authority</strong> work with a Support Broker to develop and manage their Self-Direction Budget. Support Brokers complete OPWDD training and must be authorized by OPWDD. Your Care Manager can tell you what applies to your situation.</p>
        </div>
{SB_STATUS}
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>How a Support Broker helps</h2>
        <div class="grid grid-2">
{card("path","Learning your options","We explain how Self-Direction works in plain language, including employer authority and budget authority, so you can choose what fits your family.")}
{card("people","Building your Circle of Support","We help you bring together the people who know and care about you, and plan around your goals and routines.")}
{card("book","Creating your budget","We help turn your Life Plan goals into a self-direction budget, called your Personal Resource Account, and prepare it for approval.")}
{card("check","Hiring and managing staff","We help you recruit, interview, and hire staff, and set up payroll and paperwork with your Fiscal Intermediary.")}
{card("home","Finding services and supports","Community classes, respite, transportation, and other supports that match the plan you built.")}
{card("heart","Staying on track","Budget changes, staff turnover, annual renewals, and new goals: we help you adjust as life changes.")}
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container grid grid-2">
        <div>
          <h2>Who Self-Direction is for</h2>
          <ul class="check-list">
            <li>People found eligible for OPWDD services and enrolled in the OPWDD Home and Community-Based Services (HCBS) Waiver</li>
            <li>Adults who want more control over their day, their staff, and their goals</li>
            <li>Young adults leaving school services at 21 who want a flexible, community-based plan</li>
            <li>Families who already know someone they trust to provide support and want to hire them directly</li>
          </ul>
        </div>
        <div>
          <h2>Why Spectrum Arch</h2>
          <ul class="check-list">
            <li><strong>Local.</strong> Based in Clifton Park and focused on Saratoga County and the Capital Region.</li>
            <li><strong>Autism-focused.</strong> Our work centers on adults with autism and developmental disabilities.</li>
            <li><strong>Looking ahead.</strong> We plan to seek OPWDD approval as a Fiscal Intermediary, so self-directing families can work with one local partner.</li>
            <li><strong>Person-centered.</strong> Your goals drive the plan, not an agency's schedule.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Learn more</h2>
{SB_LINKS}
        <p class="mt-2">Serving families across <a href="/support-broker-capital-region.html">Albany, Saratoga, Schenectady, Rensselaer, Warren, Washington, Columbia, and Greene counties</a>.</p>
      </div>
    </section>
''', head_extra=ld({
    "@context": "https://schema.org", "@type": "Service",
    "name": "Support Brokerage for OPWDD Self-Direction",
    "serviceType": "Support Brokerage",
    "description": "Support Broker services for people who self-direct their OPWDD services in New York's Capital Region.",
    "provider": {"@type": "NGO", "name": "Spectrum Arch, Inc.", "url": SITE + "/"},
    "areaServed": [{"@type": "AdministrativeArea", "name": c + ", NY"} for c, _ in COUNTIES],
    "url": SITE + "/support-brokerage.html"}) + ld(crumbs(("Home", ""), ("Support Brokerage", "support-brokerage.html"))),
 full_title="Support Broker in Albany & the Capital Region, NY | Spectrum Arch")

# ---------------- Self-Direction guide ----------------
STEPS = [
 ("Confirm OPWDD eligibility", "Apply through the OPWDD Front Door to be found eligible for OPWDD services. This usually needs records showing a developmental disability that began before age 22."),
 ("Enroll in Medicaid and the HCBS Waiver", "Self-Direction is available to people enrolled in Medicaid and the OPWDD Home and Community-Based Services (HCBS) Waiver."),
 ("Choose a Care Manager", "Pick a Care Coordination Organization (CCO). Your Care Manager writes your Life Plan and is your main contact with OPWDD."),
 ("Tell your Care Manager you want to self-direct", "Your Care Manager will help you request Self-Direction and connect you with OPWDD's Self-Direction information and training."),
 ("Choose a Support Broker and a Fiscal Intermediary", "If you self-direct with Budget Authority, your Support Broker helps you plan and build your budget. Your Fiscal Intermediary (FI) handles payroll, pays approved expenses, and tracks your budget."),
 ("Build your Circle of Support and your plan", "With your broker, bring together people who know you well, set goals, and decide which supports and staff you need."),
 ("Develop and submit your budget", "Your broker helps you turn the plan into a self-direction budget (your Personal Resource Account) and submit it for approval."),
 ("Hire staff and start services", "Once your budget is approved, you hire staff through your FI and your services begin. Your broker helps you adjust as needs change."),
]
steps_html = "\n".join(f'          <li><h3>{h}</h3><p>{p}</p></li>' for h, p in STEPS)
GLOSSARY = [
 ("OPWDD", "The New York State Office for People With Developmental Disabilities, which oversees services for people with developmental disabilities."),
 ("Front Door", "OPWDD's process for applying for eligibility and learning about service options."),
 ("HCBS Waiver", "Home and Community-Based Services Waiver: the Medicaid program that pays for most OPWDD community services, including Self-Direction."),
 ("Care Manager / CCO", "Your Care Manager works for a Care Coordination Organization and writes and updates your Life Plan."),
 ("Life Plan", "Your person-centered plan describing your goals and the services that support them."),
 ("Personal Resource Account (PRA)", "The self-direction budget available to you, based on your assessed needs."),
 ("Fiscal Intermediary (FI)", "The organization that processes payroll for your self-hired staff and pays for approved goods and services."),
 ("Employer authority", "You recruit, hire, train, schedule, and supervise your own staff."),
 ("Budget authority", "You decide how your approved budget is spent on supports and services."),
 ("Circle of Support", "Family, friends, and others who help you plan and make decisions."),
]
gloss_html = "\n".join(f'            <dt>{t}</dt><dd>{d}</dd>' for t, d in GLOSSARY)

page("self-direction-guide.html", "OPWDD Self-Direction in New York: Step-by-Step Guide",
 "A plain-language, step-by-step guide to OPWDD Self-Direction in New York: eligibility, the HCBS Waiver, Care Managers, Support Brokers, Fiscal Intermediaries, budgets, and hiring staff.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Guide</span>
        <h1>OPWDD Self-Direction in New York: a step-by-step guide</h1>
        <p class="lead">Self-Direction can feel complicated at first. Here is the whole path in eight steps, plus the terms you will hear along the way.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>The eight steps</h2>
        <ol class="steps">
{steps_html}
        </ol>
        <p class="mt-2">Timing varies. Eligibility, waiver enrollment, and budget approval each take time, so it helps to start early, ideally well before school services end at 21.</p>
      </div>
    </section>

    <section class="section">
      <div class="container grid grid-2">
        <div>
          <h2>Terms you will hear</h2>
          <dl class="glossary">
{gloss_html}
          </dl>
        </div>
        <div>
{SB_STATUS}
          <div class="card mt-2">
            <h3>Official information</h3>
            <p>Program rules change. For the latest details, see OPWDD's <a href="https://opwdd.ny.gov/providers/self-direction-providers" rel="noopener" target="_blank">Self-Direction information</a> and <a href="https://opwdd.ny.gov/support-broker-authorization-faq" rel="noopener" target="_blank">Support Broker FAQ</a>, or ask your Care Manager.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>Keep reading</h2>
{SB_LINKS}
      </div>
    </section>
''', head_extra=ld({
    "@context": "https://schema.org", "@type": "HowTo",
    "name": "How to start OPWDD Self-Direction in New York",
    "step": [{"@type": "HowToStep", "position": i + 1, "name": h, "text": p} for i, (h, p) in enumerate(STEPS)]})
  + ld(crumbs(("Home", ""), ("Support Brokerage", "support-brokerage.html"), ("Self-Direction guide", "self-direction-guide.html"))),
 full_title="OPWDD Self-Direction Guide for New York | Spectrum Arch")

# ---------------- FAQ ----------------
FAQ = [
 ("what-does-a-support-broker-do", "What does a Support Broker do?",
  "A Support Broker helps people who self-direct their OPWDD services with Budget Authority. That includes explaining your options, building your Circle of Support, turning your goals into a self-direction budget, helping you hire and manage staff with your Fiscal Intermediary, and adjusting your plan as your needs change."),
 ("support-broker-vs-care-manager", "How is a Support Broker different from a Care Manager?",
  "Your Care Manager, from a Care Coordination Organization, writes your Life Plan and coordinates all of your services. Your Support Broker focuses on Self-Direction: designing your self-direction budget and helping you run it day to day. The two work together."),
 ("how-much-does-it-cost", "Do families pay for Support Brokerage?",
  "Support Brokerage is an OPWDD waiver service funded through Medicaid, so families do not usually pay out of pocket. Brokerage during the start-up phase is funded separately and does not count against your Personal Resource Account. After that, ongoing brokerage is paid from your Self-Direction Budget, and you and your Circle of Support decide how much of the budget to use for it. Your Care Manager can confirm the details for your situation."),
 ("who-is-eligible", "Who can self-direct?",
  "People who are eligible for OPWDD services and enrolled in Medicaid and the OPWDD HCBS Waiver can choose Self-Direction. A parent, guardian, or other trusted person can help direct services when needed."),
 ("how-do-i-get-started", "How do I get started with Self-Direction?",
  "Start with your Care Manager. Tell them you want to self-direct, and they will help you request it and connect you with OPWDD's Self-Direction information. Our step-by-step guide walks through the whole process."),
 ("how-long-does-it-take", "How long does it take?",
  "It varies. Eligibility, waiver enrollment, and budget approval can each take weeks to months. Starting early, especially before school services end at age 21, makes a big difference."),
 ("can-i-hire-family", "Can I hire someone I already know as staff?",
  "Often, yes. With Employer Authority you recruit and hire your own staff, and many people hire someone they already know, including some relatives. There are limits: a parent or legal guardian of an adult generally cannot be paid to provide services, except in extraordinary circumstances approved by OPWDD, and a Live-in Caregiver cannot be related to the person by blood or marriage. Your Support Broker or Care Manager can explain what applies to you."),
 ("can-i-change-broker", "Can I change Support Brokers?",
  "Yes. You choose your Support Broker, and you can change if the fit is not right. Your Care Manager can help with the switch."),
 ("which-areas", "Which areas does Spectrum Arch serve?",
  "We are based in Clifton Park and focus on Saratoga County and the Capital Region, including Albany, Schenectady, Rensselaer, Warren, Washington, Columbia, and Greene counties."),
 ("are-you-accepting-clients", "Is Spectrum Arch accepting Support Brokerage clients now?",
  "Not yet. We are preparing to offer Support Brokerage and welcome families and Care Managers to join our interest list now, so we can reach out as soon as we can begin."),
]
faq_html = "\n".join(f'''          <details class="faq" id="{i}">
            <summary>{q}</summary>
            <p>{a}</p>
          </details>''' for i, q, a in FAQ)

page("support-broker-faq.html", "Support Broker & Self-Direction FAQ",
 "Answers to common questions about Support Brokers and OPWDD Self-Direction in New York: what a broker does, cost, eligibility, timing, hiring staff, and changing brokers.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Questions and answers</span>
        <h1>Support Broker and Self-Direction FAQ</h1>
        <p class="lead">Straight answers to the questions families ask most. Select a question to see the answer.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <div class="faq-list">
{faq_html}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container grid grid-2">
        <div>
          <h2>Still have a question?</h2>
          <p>Get in touch and we will do our best to help, even if the answer is another organization.</p>
          <div class="btn-row"><a class="btn btn-primary" href="/contact.html">Contact us</a></div>
        </div>
{SB_STATUS}
      </div>
    </section>
''', head_extra=ld({
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for _, q, a in FAQ]})
  + ld(crumbs(("Home", ""), ("Support Brokerage", "support-brokerage.html"), ("FAQ", "support-broker-faq.html"))),
 full_title="Support Broker & Self-Direction FAQ (NY) | Spectrum Arch")

# ---------------- Areas served ----------------
county_html = "\n".join(f'''          <div class="card">
            <h3>{c}</h3>
            <p>Including {towns}.</p>
          </div>''' for c, towns in COUNTIES)

page("support-broker-capital-region.html", "Support Brokers in Saratoga, Albany & the Capital Region",
 "Support Brokerage for OPWDD Self-Direction across New York's Capital Region: Saratoga, Albany, Schenectady, Rensselaer, Warren, Washington, Columbia, and Greene counties.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Areas we serve</span>
        <h1>Support Brokerage across the Capital Region</h1>
        <p class="lead">Spectrum Arch is based in Clifton Park, Saratoga County. We are building Support Brokerage services for families throughout the Capital Region of New York.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>Counties and communities</h2>
        <div class="grid grid-2">
{county_html}
        </div>
        <p class="mt-2">Don't see your town? <a href="/contact.html">Contact us</a>. If we can't help, we will point you to someone who can.</p>
      </div>
    </section>

    <section class="section">
      <div class="container grid grid-2">
        <div>
          <h2>Local help matters</h2>
          <p>A Support Broker who knows the area can connect you with nearby community activities, day programs, respite options, and staff, and can meet in person when that helps. Spectrum Arch is based in Clifton Park and focused on the Capital Region.</p>
        </div>
{SB_STATUS}
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>Learn more</h2>
{SB_LINKS}
      </div>
    </section>
''', head_extra=ld(crumbs(("Home", ""), ("Support Brokerage", "support-brokerage.html"), ("Areas we serve", "support-broker-capital-region.html"))),
 full_title="Support Brokers in Saratoga & Albany Counties, NY | Spectrum Arch")

# =====================================================================
# Policies
# =====================================================================
page("privacy.html", "Privacy policy",
 "How spectrumarch.org handles information: no cookies, no tracking, no forms. What we do with emails and phone calls you send us.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Privacy</span>
        <h1>Privacy policy</h1>
        <p class="lead">Last updated September 23, 2026.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>What this website collects</h2>
        <p>Very little. This website has no sign-up forms, no advertising, no analytics or tracking scripts, and it does not set cookies.</p>
        <p>Like almost every website, our hosting provider, Microsoft Azure, keeps standard technical logs (such as IP address, browser type, and the pages requested) to keep the site running and secure. We do not use these logs to identify visitors.</p>

        <h2>When you contact us</h2>
        <p>If you email or call us, we use what you share only to respond to you and, if you ask, to add you to our interest list. We do not sell, rent, or trade your information.</p>
        <p>Please do not send medical records, Medicaid numbers, or other ID numbers by email. If we need sensitive details, we will arrange a secure way to share them.</p>

        <h2>Links to other websites</h2>
        <p>We link to other organizations, such as OPWDD, for your convenience. Their privacy practices are their own.</p>

        <h2>Children</h2>
        <p>This website is intended for adults. We do not knowingly collect information from children.</p>

        <h2>Questions</h2>
        <p>Contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{TEL}">{PHONE}</a>, or write to Spectrum Arch, Inc., 29 Westbury Court, Clifton Park, NY 12065.</p>
      </div>
    </section>
''')

page("accessibility.html", "Accessibility",
 "Spectrum Arch's commitment to an accessible, low-sensory website, and how to tell us about a barrier.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Accessibility</span>
        <h1>Accessibility statement</h1>
        <p class="lead">Our website should work for everyone, including the people we exist to serve.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>What we do</h2>
        <ul class="check-list">
          <li>We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.1, level AA.</li>
          <li>Pages work with a keyboard alone, and a "Skip to main content" link appears on the first Tab press.</li>
          <li>Text has strong contrast, and the site follows your device's light or dark mode.</li>
          <li>No flashing, auto-playing video, or pop-ups. If your device is set to reduce motion, we turn animation off.</li>
          <li>Plain language wherever we can, with terms explained the first time they appear.</li>
        </ul>

        <h2>Found a barrier?</h2>
        <p>Tell us what page you were on and what happened. Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{TEL}">{PHONE}</a>. We will reply and work to fix it.</p>
      </div>
    </section>
''')

# =====================================================================
# Blog
# Each post is a file in content/blog/<slug>.html:
#   <!--
#   title: ...
#   description: ...        (one or two sentences, shown in search results)
#   date: YYYY-MM-DD
#   author: ...
#   author_title: ...
#   tags: Tag one, Tag two
#   status: published       (anything else = draft, not built)
#   -->
#   <p>Body HTML...</p>
# =====================================================================
import glob, re, datetime, html as htmlmod

BLOG_DIR = os.path.join(OUT, "content", "blog")
os.makedirs(os.path.join(OUT, "blog"), exist_ok=True)

def read_post(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"\s*<!--(.*?)-->\s*(.*)", raw, re.S)
    meta = {}
    for line in m.group(1).strip().splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    meta["body"] = m.group(2).strip()
    meta["slug"] = os.path.splitext(os.path.basename(path))[0]
    meta["tags"] = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
    return meta

POSTS = sorted((p for p in map(read_post, glob.glob(os.path.join(BLOG_DIR, "*.html")))
                if p.get("status") == "published"), key=lambda p: p["date"], reverse=True)

def nice_date(d):
    dt = datetime.date.fromisoformat(d)
    return f"{dt.strftime('%B')} {dt.day}, {dt.year}"

def words(p):
    return len(re.sub(r"<[^>]+>", " ", p["body"]).split())

for i, p in enumerate(POSTS):
    older = POSTS[i + 1] if i + 1 < len(POSTS) else None
    newer = POSTS[i - 1] if i > 0 else None
    pager = ""
    if newer or older:
        pager = '        <nav class="post-pager" aria-label="More posts">\n'
        if older:
            pager += f'          <a href="/blog/{older["slug"]}.html"><span>Older</span>{older["title"]}</a>\n'
        if newer:
            pager += f'          <a class="newer" href="/blog/{newer["slug"]}.html"><span>Newer</span>{newer["title"]}</a>\n'
        pager += '        </nav>\n'
    minutes = max(1, round(words(p) / 220))
    tags = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
    page(f"blog/{p['slug']}.html", p["title"], p["description"],
f'''    <article class="section post">
      <div class="container narrow">
        <p class="eyebrow"><a href="/blog.html">Blog</a></p>
        <h1>{p["title"]}</h1>
        <p class="post-meta">By {p["author"]}, {p["author_title"]} &middot; <time datetime="{p["date"]}">{nice_date(p["date"])}</time> &middot; {minutes} min read</p>
        <div class="tags">{tags}</div>
        <div class="post-body">
{p["body"]}
        </div>
        <div class="callout post-cta">
          <p><strong>Questions about your family's situation?</strong> <a href="/contact.html">Get in touch</a>. We are happy to talk it through, even if the right answer is another organization.</p>
        </div>
{pager}      </div>
    </article>
''', head_extra=ld({
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": p["title"], "description": p["description"],
        "datePublished": p["date"], "dateModified": p.get("updated", p["date"]),
        "author": {"@type": "Person", "name": p["author"], "jobTitle": p["author_title"]},
        "publisher": {"@type": "NGO", "name": "Spectrum Arch, Inc.", "logo": {"@type": "ImageObject", "url": SITE + "/assets/icons/icon-512.png"}},
        "mainEntityOfPage": SITE + f"/blog/{p['slug']}.html",
        "keywords": ", ".join(p["tags"])})
      + ld(crumbs(("Home", ""), ("Blog", "blog.html"), (p["title"], f"blog/{p['slug']}.html"))),
     full_title=f'{p["title"]} | Spectrum Arch')

post_cards = "\n".join(f'''          <article class="card post-card">
            <p class="post-meta"><time datetime="{p["date"]}">{nice_date(p["date"])}</time></p>
            <h2><a href="/blog/{p["slug"]}.html">{p["title"]}</a></h2>
            <p>{p["description"]}</p>
          </article>''' for p in POSTS)

page("blog.html", "Blog",
 "Practical guides for families of adults with autism and developmental disabilities in New York: turning 21, OPWDD services, Self-Direction, Support Brokers, and housing.",
f'''    <section class="page-head">
      <div class="container">
        <span class="eyebrow">Blog</span>
        <h1>Guides for families</h1>
        <p class="lead">Plain-language articles on adult services in New York: what to expect, what to ask, and where to start.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <div class="post-list">
{post_cards}
        </div>
      </div>
    </section>
''', head_extra=ld(crumbs(("Home", ""), ("Blog", "blog.html"))))

# =====================================================================
# Sitemap (every indexable page, newest content date)
# =====================================================================
STATIC_PAGES = ["", "about.html", "services.html", "support-brokerage.html", "self-direction-guide.html",
                "support-broker-faq.html", "support-broker-capital-region.html", "blog.html",
                "resources.html", "get-involved.html", "contact.html", "privacy.html", "accessibility.html"]
SITE_UPDATED = "2026-09-23"
entries = [(u, SITE_UPDATED) for u in STATIC_PAGES] + [(f"blog/{p['slug']}.html", p.get("updated", p["date"])) for p in POSTS]
urls = "\n".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{d}</lastmod></url>" for u, d in entries)
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
print(f"Built {len(STATIC_PAGES)} pages and {len(POSTS)} blog posts.")
