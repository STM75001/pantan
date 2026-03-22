/* ═══════════════════════════════════════════
   PANTAN Technologies — Global JavaScript
   pan-tan.com
═══════════════════════════════════════════ */

/* ── Mobile nav toggle ── */
function toggleMobileMenu() {
  const menu = document.getElementById('mobile-menu');
  if (menu) menu.classList.toggle('open');
}

/* ── Active nav link — works on Vercel (cleanUrls) and local file:// preview ── */
function setActiveNav() {
  const path = window.location.pathname
    .replace(/\/index\.html$/, '/')   // treat /index.html same as /
    .replace(/\.html$/, '')           // strip .html for cleanUrls
    .replace(/\/$/, '') || '/';       // strip trailing slash, keep root as '/'

  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(link => {
    link.classList.remove('active');
    const href = (link.getAttribute('href') || '')
      .replace(/\/index\.html$/, '/')
      .replace(/\.html$/, '')
      .replace(/\/$/, '') || '/';

    // Exact match for home, prefix match for everything else
    if (href === '/' && path === '/') {
      link.classList.add('active');
    } else if (href !== '/' && path.startsWith('/' + href.replace(/^.*\//, ''))) {
      link.classList.add('active');
    } else if (href !== '/' && href !== '' && path.endsWith(href)) {
      link.classList.add('active');
    }
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
  const form = document.getElementById('contact-form');
  if (btn && form) {
    btn.textContent = '✓ Message Sent — We\'ll be in touch within 1 business day';
    btn.style.background = '#0D8C72';
    btn.disabled = true;
    form.querySelectorAll('input, select, textarea').forEach(el => el.disabled = true);
  }
}

/* ── Smooth scroll to top on internal navigation ── */
function scrollTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

/* ── On DOM ready ── */
document.addEventListener('DOMContentLoaded', function () {
  setActiveNav();

  /* Attach form submit handler */
  const form = document.getElementById('contact-form');
  if (form) form.addEventListener('submit', handleFormSubmit);

  /* Close mobile menu when any link is clicked */
  document.querySelectorAll('.mobile-menu a').forEach(link => {
    link.addEventListener('click', () => {
      const menu = document.getElementById('mobile-menu');
      if (menu) menu.classList.remove('open');
    });
  });

  /* Close mobile menu when clicking outside it */
  document.addEventListener('click', function(e) {
    const menu = document.getElementById('mobile-menu');
    const hamburger = document.querySelector('.hamburger');
    if (menu && menu.classList.contains('open')) {
      if (!menu.contains(e.target) && !hamburger.contains(e.target)) {
        menu.classList.remove('open');
      }
    }
  });
});
