/* ═══════════════════════════════════════════
   PANTAN Technologies — Cookie Consent
   GA4: G-V06KVBM5NT  |  Self-contained styles
═══════════════════════════════════════════ */
(function () {
  var GA_ID = 'G-V06KVBM5NT';
  var KEY = 'pantan_cookie_consent';

  function getConsent() { try { return localStorage.getItem(KEY); } catch(e) { return null; } }
  function setConsent(v) { try { localStorage.setItem(KEY, v); } catch(e) {} }

  function loadGA() {
    if (window._gaLoaded) return;
    window._gaLoaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag(){ dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA_ID, { anonymize_ip: true });
  }

  function denyGA() {
    window.dataLayer = window.dataLayer || [];
    function gtag(){ dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('consent', 'default', { analytics_storage: 'denied', ad_storage: 'denied' });
  }

  function removeBanner() {
    var b = document.getElementById('_pcb');
    if (b) { b.style.opacity = '0'; b.style.transform = 'translateY(10px)'; setTimeout(function(){ b.remove(); }, 350); }
  }

  window.pantanAccept = function () { setConsent('yes'); loadGA(); removeBanner(); };
  window.pantanDecline = function () { setConsent('no'); denyGA(); removeBanner(); };

  function injectStyles() {
    if (document.getElementById('_pcb_css')) return;
    var st = document.createElement('style');
    st.id = '_pcb_css';
    st.textContent = [
      '#_pcb{position:fixed;bottom:0;left:0;right:0;z-index:99999;',
        'background:#1E2E45;border-top:3px solid #0D8C72;',
        'padding:1rem 1.5rem;box-shadow:0 -4px 20px rgba(0,0,0,.35);',
        'opacity:0;transform:translateY(12px);',
        'transition:opacity .35s ease,transform .35s ease;}',
      '#_pcb .pcb-w{max-width:1160px;margin:0 auto;display:flex;',
        'align-items:center;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;}',
      '#_pcb .pcb-l{display:flex;align-items:flex-start;gap:.85rem;flex:1;min-width:260px;}',
      '#_pcb .pcb-ico{font-size:1.4rem;flex-shrink:0;margin-top:1px;}',
      '#_pcb .pcb-t strong{display:block;color:#fff;font-size:.92rem;',
        'font-weight:700;margin-bottom:.2rem;font-family:system-ui,sans-serif;}',
      '#_pcb .pcb-t p{color:rgba(255,255,255,.62);font-size:.8rem;line-height:1.6;',
        'margin:0;font-family:system-ui,sans-serif;}',
      '#_pcb .pcb-t a{color:#12B08E;text-decoration:underline;}',
      '#_pcb .pcb-btns{display:flex;gap:.6rem;flex-shrink:0;align-items:center;}',
      '#_pcb .pcb-yes{background:#0D8C72;color:#fff;font-size:.85rem;font-weight:700;',
        'padding:.6rem 1.3rem;border-radius:7px;border:none;cursor:pointer;',
        'font-family:system-ui,sans-serif;transition:background .2s;}',
      '#_pcb .pcb-yes:hover{background:#12B08E;}',
      '#_pcb .pcb-no{background:transparent;color:rgba(255,255,255,.55);font-size:.85rem;',
        'font-weight:500;padding:.6rem .9rem;border-radius:7px;',
        'border:1.5px solid rgba(255,255,255,.2);cursor:pointer;',
        'font-family:system-ui,sans-serif;transition:border-color .2s,color .2s;}',
      '#_pcb .pcb-no:hover{border-color:rgba(255,255,255,.5);color:#fff;}',
      '@media(max-width:640px){#_pcb .pcb-w{flex-direction:column;gap:.85rem;}',
        '#_pcb .pcb-btns{width:100%;justify-content:flex-end;}}'
    ].join('');
    document.head.appendChild(st);
  }

  function showBanner() {
    injectStyles();
    var b = document.createElement('div');
    b.id = '_pcb';
    b.innerHTML =
      '<div class="pcb-w">' +
        '<div class="pcb-l">' +
          '<div class="pcb-ico">🍪</div>' +
          '<div class="pcb-t">' +
            '<strong>We use cookies</strong>' +
            '<p>PANTAN Technologies uses Google Analytics to understand how visitors use our site — helping us improve your experience. No personal data is sold. ' +
            '<a href="/legal/cookies" target="_blank">Cookie Policy</a> · <a href="/legal/privacy" target="_blank">Privacy Policy</a></p>' +
          '</div>' +
        '</div>' +
        '<div class="pcb-btns">' +
          '<button class="pcb-no" onclick="pantanDecline()">Decline</button>' +
          '<button class="pcb-yes" onclick="pantanAccept()">Accept Analytics</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(b);
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        b.style.opacity = '1';
        b.style.transform = 'translateY(0)';
      });
    });
  }

  function init() {
    var c = getConsent();
    if (c === 'yes') { loadGA(); return; }
    if (c === 'no')  { denyGA(); return; }
    denyGA();
    showBanner();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
