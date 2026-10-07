// Google tag (GA4 / Google Ads), loaded only when an ID is set on this script's
// data attributes. Records Ad Grants conversions: waitlist requests, and clicks
// on our email address and phone number. No form contents are sent.
(function () {
  var me = document.currentScript;
  var ga = me && me.getAttribute('data-ga');
  var ads = me && me.getAttribute('data-ads');
  if (!ga && !ads) return;

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  if (ga) gtag('config', ga);
  if (ads) gtag('config', ads);

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(ga || ads);
  document.head.appendChild(s);

  function track(name, params) { gtag('event', name, params || {}); }
  window.saTrack = track;

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    if (href.indexOf('mailto:') === 0) track('contact_email_click', { link_url: href.split('?')[0] });
    else if (href.indexOf('tel:') === 0) track('contact_phone_click', { link_url: href });
  });
})();
