// Waitlist form: builds a pre-filled email. Nothing is sent to the website.
(function () {
  var form = document.getElementById('waitlist-form');
  if (!form) return;
  var err = document.getElementById('wl-error');
  var done = document.getElementById('wl-done');
  var TO = 'info@spectrumarch.org';

  function val(id) { var el = document.getElementById(id); return el ? el.value.trim() : ''; }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var problems = [];
    if (!val('wl-name')) problems.push('your name');
    var email = val('wl-email');
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) problems.push('a valid email address');
    if (!val('wl-county')) problems.push('your county');
    if (!document.getElementById('wl-consent').checked) problems.push('the agreement checkbox');
    if (problems.length) {
      err.textContent = 'Please fill in: ' + problems.join(', ') + '.';
      err.hidden = false;
      err.focus && err.focus();
      return;
    }
    err.hidden = true;

    var lines = [
      'Please add me to the Support Brokerage waitlist.',
      '',
      'Name: ' + val('wl-name'),
      'Email: ' + email,
      'Phone: ' + (val('wl-phone') || '-'),
      'I am: ' + val('wl-role'),
      'County: ' + val('wl-county'),
      'Age of person: ' + val('wl-age'),
      'OPWDD eligibility: ' + val('wl-eligible'),
      'Self-Direction: ' + val('wl-sd'),
      'Need a broker: ' + val('wl-when'),
      'Best way to reach me: ' + val('wl-contact'),
      'Preferred language: ' + val('wl-lang'),
      '',
      'Notes: ' + (val('wl-notes') || '-'),
      '',
      'I agree that Spectrum Arch may contact me about Support Brokerage.'
    ];
    var subject = 'Waitlist: ' + val('wl-name') + ' (' + val('wl-county') + ')';
    window.location.href = 'mailto:' + TO + '?subject=' + encodeURIComponent(subject) +
      '&body=' + encodeURIComponent(lines.join('\n'));
    done.hidden = false;
    done.focus();
  });
})();
