/* ═══════════════════════════════════════════
   PANTAN Technologies — Cookie Consent
   Google Analytics GA4 consent management
═══════════════════════════════════════════ */

(function() {
  const GA_ID = 'G-V06KVBM5NT';
  const CONSENT_KEY = 'pantan_cookie_consent';
  const CONSENT_VERSION = '1';

  /* ── Check existing consent ── */
  function getConsent() {
    try { return localStorage.getItem(CONSENT_KEY); } catch(e) { return null; }
  }
  function setConsent(val) {
    try { localStorage.setItem(CONSENT_KEY, val); } catch(e) {}
  }

  /* ── Load GA4 after consent ── */
  function loadGA() {
    if (window._gaLoaded) return;
    window._gaLoaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA_ID, { anonymize_ip: true });
  }

  /* ── Deny: load GA in anonymous mode only ── */
  function denyGA() {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    window.gtag = gtag;
    gtag('consent', 'default', {
      analytics_storage: 'denied',
      ad_storage: 'denied'
    });
  }

  /* ── Remove banner ── */
  function removeBanner() {
    var b = document.getElementById('pantan-cookie-banner');
    if (b) { b.style.opacity = '0'; setTimeout(function(){ b.remove(); }, 400); }
  }

  /* ── Accept handler ── */
  window.pantanAcceptCookies = function() {
    setConsent('accepted_' + CONSENT_VERSION);
    loadGA();
    removeBanner();
  };

  /* ── Decline handler ── */
  window.pantanDeclineCookies = function() {
    setConsent('declined_' + CONSENT_VERSION);
    denyGA();
    removeBanner();
  };

  /* ── Show banner ── */
  function showBanner() {
    var banner = document.createElement('div');
    banner.id = 'pantan-cookie-banner';
    banner.innerHTML = `
      <div class="pcb-inner">
        <div class="pcb-left">
          <div class="pcb-icon">🍪</div>
          <div class="pcb-text">
            <strong>We use cookies</strong>
            <p>PANTAN Technologies uses Google Analytics to understand how visitors use our site — helping us improve your experience. No personal data is sold. <a href="/legal/cookies" target="_blank">Cookie Policy</a> · <a href="/legal/privacy" target="_blank">Privacy Policy</a></p>
          </div>
        </div>
        <div class="pcb-actions">
          <button class="pcb-decline" onclick="pantanDeclineCookies()">Decline</button>
          <button class="pcb-accept" onclick="pantanAcceptCookies()">Accept Analytics</button>
        </div>
      </div>
    `;
    document.body.appendChild(banner);
    /* Animate in */
    requestAnimationFrame(function(){
      requestAnimationFrame(function(){
        banner.style.opacity = '1';
        banner.style.transform = 'translateY(0)';
      });
    });
  }

  /* ── Init ── */
  function init() {
    var consent = getConsent();
    if (consent && consent.startsWith('accepted_')) {
      loadGA();
      return;
    }
    if (consent && consent.startsWith('declined_')) {
      denyGA();
      return;
    }
    /* No consent yet — show banner */
    denyGA(); /* default deny until accepted */
    showBanner();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
