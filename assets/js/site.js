// Mobile menu toggle and dropdown behaviour. External file so the
// Content-Security-Policy can forbid inline scripts.
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  // Only one dropdown open at a time; close on outside click or Escape.
  var groups = Array.prototype.slice.call(document.querySelectorAll('.site-nav details'));
  groups.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) groups.forEach(function (o) { if (o !== d) o.open = false; });
    });
  });
  document.addEventListener('click', function (e) {
    groups.forEach(function (d) { if (d.open && !d.contains(e.target)) d.open = false; });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') groups.forEach(function (d) {
      if (d.open) { d.open = false; d.querySelector('summary').focus(); }
    });
  });
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
