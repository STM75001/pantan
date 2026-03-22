/* ═══════════════════════════════════════════
   PANTAN Technologies — Global JavaScript
   pan-tan.com
═══════════════════════════════════════════ */

/* ── Mobile nav toggle ── */
function toggleMobileMenu() {
  const menu = document.getElementById('mobile-menu');
  if (menu) menu.classList.toggle('open');
}

/* ── Mark active nav link based on current page ── */
function setActiveNav() {
  const path = window.location.pathname;
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(link => {
    link.classList.remove('active');
    const href = link.getAttribute('href');
    if (!href) return;
    if (path === '/' && href === '/') { link.classList.add('active'); return; }
    if (href !== '/' && path.startsWith(href)) link.classList.add('active');
  });
}

/* ── Job filter (careers page) ── */
function filterJobs(cat, btn) {
  document.querySelectorAll('.job-filter').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  document.querySelectorAll('.job-card').forEach(card => {
    card.style.display = (cat === 'all' || card.dataset.cat === cat) ? 'block' : 'none';
  });
}

/* ── Contact form submit ── */
function handleFormSubmit(e) {
  if (e) e.preventDefault();
  const btn = document.querySelector('.form-submit');
  if (btn) {
    btn.textContent = '✓ Message Sent — We\'ll be in touch within 1 business day';
    btn.style.background = '#0D8C72';
    btn.disabled = true;
  }
}

document.addEventListener('DOMContentLoaded', function () {
  setActiveNav();

  /* Attach form submit handler */
  const form = document.getElementById('contact-form');
  if (form) form.addEventListener('submit', handleFormSubmit);

  /* Mobile menu close on link click */
  document.querySelectorAll('.mobile-menu a').forEach(link => {
    link.addEventListener('click', () => {
      const menu = document.getElementById('mobile-menu');
      if (menu) menu.classList.remove('open');
    });
  });
});
