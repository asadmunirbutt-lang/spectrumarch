// Mobile navigation toggle. Kept in an external file so the
// Content-Security-Policy can forbid inline scripts.
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
