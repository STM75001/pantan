#!/usr/bin/env python3
"""
PANTAN Technologies — Static Site Generator
Generates all HTML pages from shared templates.
Run: python3 build.py
"""

import os

OUT = "/home/claude/pantan-v2"

# ─────────────────────────────────────────────
# SHARED SNIPPETS
# ─────────────────────────────────────────────

FAVICON = """<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%230B1F3A'/%3E%3Cpath d='M10 50V14h13a10 10 0 0 1 0 20H18v16z' fill='none' stroke='%2312B08E' stroke-width='3' stroke-linejoin='round'/%3E%3Cline x1='10' y1='34' x2='23' y2='34' stroke='%2312B08E' stroke-width='3'/%3E%3Cline x1='34' y1='14' x2='54' y2='14' stroke='%23D4A017' stroke-width='3' stroke-linecap='round'/%3E%3Cline x1='44' y1='14' x2='44' y2='50' stroke='%23D4A017' stroke-width='3' stroke-linecap='round'/%3E%3Ccircle cx='54' cy='50' r='3' fill='%2312B08E' opacity='0.8'/%3E%3C/svg%3E">"""

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&display=swap" rel="stylesheet">"""

LOGO_SVG = """<svg width="42" height="42" viewBox="0 0 42 42" xmlns="http://www.w3.org/2000/svg">
        <rect width="42" height="42" rx="10" fill="#0B1F3A"/>
        <rect x="1" y="1" width="40" height="40" rx="9" fill="none" stroke="rgba(13,140,114,0.5)" stroke-width="1"/>
        <path d="M7 31V11h8.5a6.5 6.5 0 0 1 0 13H11v7z" fill="none" stroke="#12B08E" stroke-width="2" stroke-linejoin="round"/>
        <line x1="7" y1="24" x2="15.5" y2="24" stroke="#12B08E" stroke-width="2"/>
        <line x1="22" y1="11" x2="36" y2="11" stroke="#D4A017" stroke-width="2" stroke-linecap="round"/>
        <line x1="29" y1="11" x2="29" y2="31" stroke="#D4A017" stroke-width="2" stroke-linecap="round"/>
        <circle cx="36" cy="31" r="2" fill="#12B08E" opacity="0.7"/>
      </svg>"""

def css_path(depth=0):
    prefix = "../" * depth
    return f'{prefix}assets/css/styles.css'

def js_path(depth=0):
    prefix = "../" * depth
    return f'{prefix}assets/js/main.js'

def nav_html(depth=0):
    p = "../" * depth
    return f"""<nav class="site-nav">
  <div class="nav-inner">
    <a class="nav-logo" href="{p}index.html">
      {LOGO_SVG}
      <span class="nav-logo-text">PANTAN Technologies</span>
    </a>
    <ul class="nav-links">
      <li><a href="{p}index.html">Home</a></li>
      <li><a href="{p}services/index.html">Services</a></li>
      <li><a href="{p}careers.html">Careers</a></li>
      <li><a href="{p}about.html">About</a></li>
      <li><a href="{p}partners.html">Partners</a></li>
      <li><a href="{p}contact.html" class="nav-cta">Get in Touch</a></li>
    </ul>
    <button class="hamburger" onclick="toggleMobileMenu()" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
<div class="mobile-menu" id="mobile-menu">
  <a href="{p}index.html">Home</a>
  <a href="{p}services/index.html">Services</a>
  <a href="{p}careers.html">Careers</a>
  <a href="{p}about.html">About</a>
  <a href="{p}partners.html">Partners</a>
  <a href="{p}contact.html">Get in Touch</a>
</div>"""

def footer_html(depth=0):
    p = "../" * depth
    return f"""<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:.5rem;">
          {LOGO_SVG}
          <span style="font-family:var(--font-display);font-size:1.1rem;font-weight:700;color:white;">PANTAN Technologies</span>
        </div>
        <p>High-end compliance documentation, contract preparation, PAF management SaaS, and government procurement support. U.S.-managed. Offshore-supported. Accuracy-guaranteed.</p>
        <p style="margin-top:.75rem;font-size:.8rem;color:rgba(255,255,255,0.35);">5080 Spectrum Drive, Suite 575E<br>Addison, TX 75001<br>info@pan-tan.com</p>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        <a href="{p}services/contract-review.html">Contract Review &amp; Templates</a>
        <a href="{p}services/regulatory-compliance.html">Regulatory Compliance Docs</a>
        <a href="{p}services/paf-management.html">PAF Management SaaS</a>
        <a href="{p}services/government-procurement.html">Government Procurement Docs</a>
      </div>
      <div class="footer-col">
        <h5>Company</h5>
        <a href="{p}about.html">About PANTAN</a>
        <a href="{p}partners.html">Partners &amp; Case Studies</a>
        <a href="{p}careers.html">Careers</a>
        <a href="{p}contact.html">Contact Us</a>
      </div>
      <div class="footer-col">
        <h5>Industries</h5>
        <a href="{p}services/regulatory-compliance.html">Healthcare</a>
        <a href="{p}services/regulatory-compliance.html">Information Technology</a>
        <a href="{p}services/regulatory-compliance.html">Drone / UAV</a>
        <a href="{p}services/government-procurement.html">Government Contracting</a>
        <a href="{p}services/paf-management.html">Staffing Firms</a>
      </div>
    </div>
    <div class="footer-trust">
      <div class="trust-badge"><span class="tb-icon">🔒</span> 256-bit SSL Encrypted</div>
      <div class="trust-badge"><span class="tb-icon">✅</span> GDPR Compliant</div>
      <div class="trust-badge"><span class="tb-icon">✅</span> FTC Compliant</div>
      <div class="trust-badge"><span class="tb-icon">⚖️</span> 29 CFR § 1625.2 Compliant</div>
      <div class="trust-badge"><span class="tb-icon">🛡️</span> WBE / DBE Certification In Progress</div>
    </div>
    <div class="footer-bottom">
      <span>© 2025 PANTAN Technologies, LLC. All rights reserved.</span>
      <div class="footer-legal-links">
        <a href="{p}legal/terms.html">Terms of Service</a>
        <a href="{p}legal/privacy.html">Privacy Policy</a>
        <a href="{p}legal/cookies.html">Cookie Policy</a>
        <a href="{p}legal/ai-terms.html">AI Terms</a>
        <a href="{p}legal/disclaimer.html">Disclaimer</a>
        <a href="{p}legal/accessibility.html">Accessibility</a>
      </div>
    </div>
  </div>
</footer>"""

def page(title, description, body, depth=0, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  {FAVICON}
  {FONTS}
  <link rel="stylesheet" href="{css_path(depth)}">
  {extra_head}
</head>
<body>
{nav_html(depth)}
{body}
{footer_html(depth)}
<script src="{js_path(depth)}"></script>
</body>
</html>"""

def write(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ {filepath.replace(OUT+'/', '')}")

# ─────────────────────────────────────────────
# HOME PAGE
# ─────────────────────────────────────────────
home_body = """
<section class="hero">
  <div class="hero-inner">
    <div>
      <div class="hero-eyebrow">High-End Compliance &amp; Documentation Services</div>
      <h1>Precision Documentation for <em>Enterprise</em> and Government Clients</h1>
      <p class="hero-sub">PANTAN Technologies delivers contract preparation, regulatory compliance documentation, Public Access File management, and government procurement support — with offshore depth and U.S.-based oversight that high-stakes environments demand.</p>
      <div class="hero-ctas">
        <a href="contact.html" class="btn-primary">Request a Consultation</a>
        <a href="services/index.html" class="btn-outline">Explore Services</a>
      </div>
    </div>
    <div>
      <div class="hero-panel">
        <div class="panel-title">Delivery at a Glance</div>
        <div class="panel-stats">
          <div class="panel-stat"><div class="num">10+</div><div class="lbl">Years Compliance &amp; Docs</div></div>
          <div class="panel-stat"><div class="num">4</div><div class="lbl">Integrated Service Verticals</div></div>
          <div class="panel-stat"><div class="num">24/7</div><div class="lbl">Offshore Documentation Capacity</div></div>
          <div class="panel-stat"><div class="num">SaaS</div><div class="lbl">PAF Management Platform</div></div>
        </div>
        <hr class="panel-divider">
        <div class="panel-tags">
          <span class="panel-tag">Contract Review</span>
          <span class="panel-tag">Regulatory Compliance</span>
          <span class="panel-tag">PAF SaaS</span>
          <span class="panel-tag">Gov. Procurement</span>
          <span class="panel-tag">Drone / UAV</span>
          <span class="panel-tag">HIPAA · IT Governance</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-inner">
    <div class="section-head centered">
      <div class="section-label">Our Services</div>
      <h2 class="section-title">Four Verticals. One Premium Compliance Partner.</h2>
      <p class="section-intro">From contract lifecycle support to a proprietary SaaS platform, PANTAN delivers documentation and compliance solutions built for the complexity of enterprise and government environments.</p>
    </div>
    <div class="services-grid">
      <a href="services/contract-review.html" class="service-card">
        <div class="service-icon">📄</div>
        <h3>Contract Review &amp; Template Preparation</h3>
        <p>Standard agreements, NDAs, SOWs, and MSAs — reviewed, structured, and delivered with precision. Version control frameworks and compliance-aligned templates built for organizations executing at scale.</p>
        <span class="card-link">Explore Service →</span>
      </a>
      <a href="services/regulatory-compliance.html" class="service-card">
        <div class="service-icon">🛡️</div>
        <h3>Regulatory Compliance &amp; Documentation Support</h3>
        <p>High-end compliance documentation for healthcare, IT, and drone/UAV — built to withstand audit and satisfy regulators across HIPAA, IT governance frameworks, and FAA Part 107.</p>
        <span class="card-link">Explore Service →</span>
      </a>
      <a href="services/paf-management.html" class="service-card saas-card">
        <div class="service-icon gold-icon">🗂️</div>
        <div class="saas-badge">⬡ SaaS Platform</div>
        <h3>Public Access File (PAF) Management</h3>
        <p>A purpose-built SaaS platform that tracks, organizes, and manages PAF compliance documentation for staffing firms and contractors — eliminating audit risk with automated workflows and audit-ready exports.</p>
        <span class="card-link gold">Schedule a Demo →</span>
      </a>
      <a href="services/government-procurement.html" class="service-card">
        <div class="service-icon">🏛️</div>
        <h3>Government Vendor &amp; Procurement Documentation</h3>
        <p>RFP/RFQ response preparation, certification submissions, capability statements, and SAM.gov documentation — built to win contracts and satisfy procurement evaluators.</p>
        <span class="card-link">Explore Service →</span>
      </a>
    </div>
  </div>
</section>

<section class="section section-navy">
  <div class="section-inner">
    <div class="section-head">
      <div class="section-label section-label-light">Why PANTAN</div>
      <h2 class="section-title section-title-light">Built to Deliver. Built for Accuracy.</h2>
      <p class="section-intro section-intro-light">Enterprise and government clients cannot afford documentation errors. PANTAN combines offshore delivery depth with U.S.-managed quality control to ensure every document is accurate, audit-ready, and on time.</p>
    </div>
    <div class="why-grid">
      <div class="why-card"><div class="why-icon">🌐</div><h4>24/7 Offshore Documentation Team</h4><p>Our trained offshore specialists operate around the clock — faster turnaround on high-volume documentation without extending your timelines.</p></div>
      <div class="why-card"><div class="why-icon">🎯</div><h4>Accuracy-First Delivery</h4><p>Every deliverable passes through a structured U.S.-based review layer before release. QA is non-negotiable.</p></div>
      <div class="why-card"><div class="why-icon">⚙️</div><h4>SaaS + Services Integration</h4><p>Our PAF platform integrates directly with our documentation services — from compliance gap identification to document resolution in one workflow.</p></div>
      <div class="why-card"><div class="why-icon">🏛️</div><h4>Government &amp; Enterprise Fluency</h4><p>We understand the language and evaluative expectations of federal procurement, healthcare regulation, and enterprise contracting.</p></div>
      <div class="why-card"><div class="why-icon">🔒</div><h4>Multi-Industry Regulatory Expertise</h4><p>HIPAA, IT governance, FAA Part 107 — working expertise in the frameworks governing healthcare, IT, and drone/UAV operations.</p></div>
      <div class="why-card"><div class="why-icon">📊</div><h4>Diverse Supplier Advantage</h4><p>As a WBE/DBE-in-progress firm, PANTAN helps prime contractors and agencies meet supplier diversity requirements with high-caliber documentation.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="section-inner">
    <div class="section-head centered">
      <div class="section-label">Industries We Serve</div>
      <h2 class="section-title">Built for the Most Demanding Compliance Environments</h2>
      <p class="section-intro">Our services are purpose-built for organizations where documentation errors carry real consequences — regulatory penalties, contract losses, and audit failures.</p>
    </div>
    <div class="industries-grid">
      <div class="industry-item"><div class="i-icon">🏥</div><h5>Healthcare</h5><p>HIPAA compliance packages, staffing PAF management, and clinical admin documentation.</p></div>
      <div class="industry-item"><div class="i-icon">🖥️</div><h5>Information Technology</h5><p>IT governance, data privacy, vendor management, and technology policy documentation.</p></div>
      <div class="industry-item"><div class="i-icon">🚁</div><h5>Drone / UAV</h5><p>FAA Part 107 compliance packages, CONOPS, waiver packages, and UAS operational procedures.</p></div>
      <div class="industry-item"><div class="i-icon">🏛️</div><h5>Government Contracting</h5><p>RFP responses, capability statements, certification submissions, and procurement documentation.</p></div>
    </div>
  </div>
</section>

<div class="cta-band">
  <div style="max-width:580px;margin:0 auto;">
    <h2>Ready to Elevate Your Compliance Documentation?</h2>
    <p>Whether you need a contract review, an ongoing compliance partner, or a demo of our PAF platform — PANTAN is ready to deliver.</p>
    <a href="contact.html" class="btn-white">Request a Free Consultation</a>
  </div>
</div>"""

write(f"{OUT}/index.html",
      page("PANTAN Technologies | High-End Compliance & Documentation Services",
           "PANTAN Technologies delivers contract preparation, regulatory compliance documentation, PAF SaaS, and government procurement documentation for enterprise and government clients.",
           home_body, depth=0))

# ─────────────────────────────────────────────
# SERVICES INDEX
# ─────────────────────────────────────────────
services_index_body = """
<section class="service-hero">
  <div class="service-hero-inner">
    <h1>Compliance &amp; Documentation Services for Enterprise and Government</h1>
    <p>Four integrated service lines — each built for the precision, regulatory depth, and accountability that high-stakes compliance environments require.</p>
    <a href="../contact.html" class="btn-primary">Talk to a Specialist</a>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="services-grid">
      <a href="contract-review.html" class="service-card">
        <div class="service-icon">📄</div>
        <h3>Contract Review &amp; Template Preparation</h3>
        <p>NDAs, MSAs, SOWs reviewed for compliance gaps and delivered as version-controlled, reusable templates ready for execution at scale.</p>
        <span class="card-link">View Service →</span>
      </a>
      <a href="regulatory-compliance.html" class="service-card">
        <div class="service-icon">🛡️</div>
        <h3>Regulatory Compliance &amp; Documentation</h3>
        <p>Healthcare, IT governance, and drone/UAV compliance documentation structured to satisfy regulators and withstand audit.</p>
        <span class="card-link">View Service →</span>
      </a>
      <a href="paf-management.html" class="service-card saas-card">
        <div class="service-icon gold-icon">🗂️</div>
        <div class="saas-badge">⬡ SaaS Platform</div>
        <h3>Public Access File (PAF) Management</h3>
        <p>Purpose-built SaaS for staffing firms and contractors to manage PAF compliance with automated workflows and audit-ready reporting.</p>
        <span class="card-link gold">Schedule a Demo →</span>
      </a>
      <a href="government-procurement.html" class="service-card">
        <div class="service-icon">🏛️</div>
        <h3>Government Vendor &amp; Procurement Documentation</h3>
        <p>RFP/RFQ responses, capability statements, and certification packages built to win contracts and satisfy procurement standards.</p>
        <span class="card-link">View Service →</span>
      </a>
    </div>
  </div>
</section>
<div class="cta-band">
  <div style="max-width:560px;margin:0 auto;">
    <h2>Not Sure Where to Begin?</h2>
    <p>Our specialists will assess your documentation environment and recommend the right service combination for your needs.</p>
    <a href="../contact.html" class="btn-white">Book a Free Assessment</a>
  </div>
</div>"""

write(f"{OUT}/services/index.html",
      page("Services | PANTAN Technologies",
           "Compliance documentation, contract review, PAF SaaS, and government procurement documentation services.",
           services_index_body, depth=1))

# ─────────────────────────────────────────────
# SERVICE: CONTRACT REVIEW
# ─────────────────────────────────────────────
contract_body = """
<section class="service-hero">
  <div class="service-hero-inner">
    <p class="crumb"><a href="index.html">← Services</a> / Contract Review &amp; Template Preparation</p>
    <h1>Contract Preparation Services USA — Precise, Compliant, Ready to Execute</h1>
    <p>Expert contract review, template development, and version control for consulting firms, enterprises, and government-adjacent organizations that cannot afford ambiguity in their agreements.</p>
    <div class="hero-ctas">
      <a href="../contact.html" class="btn-primary">Request Contract Support</a>
      <a href="../partners.html" class="btn-outline">Explore Partnership</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="section-inner two-col">
    <div>
      <div class="content-block">
        <div class="problem-box">
          <h3>The Challenge</h3>
          <p>Organizations executing contracts at scale face agreements that are inconsistent, non-compliant, or outdated. Templates drift. Version control fails. A single missed clause in an NDA can trigger costly disputes, regulatory violations, or contract voidance — usually discovered only after the damage is done.</p>
        </div>
      </div>
      <div class="content-block">
        <h3>How PANTAN Delivers Contract Precision</h3>
        <p>We review existing contracts for compliance gaps, ambiguity, and risk exposure. We develop standardized, compliance-aligned templates tailored to your industry and jurisdiction. Our offshore-supported team handles high-volume review at speed, while U.S.-based compliance leads verify accuracy before every delivery.</p>
      </div>
      <div class="content-block">
        <h3>What Clients Gain</h3>
        <ul class="benefits-list">
          <li>Standardized, compliance-aligned templates across NDAs, SOWs, MSAs, and service agreements</li>
          <li>Gap analysis and risk flagging with a clear remediation summary</li>
          <li>Version control frameworks that eliminate document confusion across teams</li>
          <li>Jurisdiction-aware language review for multi-state and federal compliance</li>
          <li>Rapid turnaround — offshore capacity enables 24/7 processing</li>
          <li>Retainer options for continuous, high-volume contract activity</li>
        </ul>
      </div>
      <div class="content-block">
        <h3>Why PANTAN</h3>
        <div class="diff-grid">
          <div class="diff-item"><h5>Offshore Speed, U.S. Quality</h5><p>Round-the-clock processing without sacrificing review accuracy or compliance depth.</p></div>
          <div class="diff-item"><h5>Compliance-First Review</h5><p>We review through a regulatory lens — not just legal language, but industry-specific compliance implications.</p></div>
          <div class="diff-item"><h5>Template Library Development</h5><p>Reusable, version-controlled template libraries — never start from a blank page again.</p></div>
          <div class="diff-item"><h5>Enterprise &amp; Government Fluency</h5><p>Experience with federal contracting language, healthcare compliance, and enterprise procurement standards.</p></div>
        </div>
      </div>
    </div>
    <div>
      <div class="sidebar-card">
        <h4>Ready for Contract Support?</h4>
        <p>Share your contract challenge and we'll outline a solution within 48 hours.</p>
        <div class="sidebar-cta-group">
          <a href="../contact.html" class="btn-teal">Submit a Contract Request</a>
          <a href="../contact.html" class="btn-navy">Explore Partnership</a>
        </div>
        <div class="sidebar-meta">
          <strong>Agreements We Support:</strong>
          NDAs · MSAs · SOWs · Contractor Agreements · Staffing &amp; Vendor Agreements · SaaS Terms · Government Subcontracts · Teaming Agreements
        </div>
      </div>
    </div>
  </div>
</section>
<div class="cta-band">
  <div style="max-width:560px;margin:0 auto;">
    <h2>Agreements That Hold Up Under Scrutiny.</h2>
    <p>Compliant, consistent, and clearly drafted contracts — every time.</p>
    <a href="../contact.html" class="btn-white">Request a Consultation</a>
  </div>
</div>"""

write(f"{OUT}/services/contract-review.html",
      page("Contract Review & Template Preparation | PANTAN Technologies",
           "Expert contract review, NDA and MSA template preparation, version control, and compliance-aligned documentation for enterprise and government organizations.",
           contract_body, depth=1))

# ─────────────────────────────────────────────
# SERVICE: REGULATORY COMPLIANCE
# ─────────────────────────────────────────────
regulatory_body = """
<section class="service-hero">
  <div class="service-hero-inner">
    <p class="crumb"><a href="index.html">← Services</a> / Regulatory Compliance &amp; Documentation</p>
    <h1>Regulatory Compliance Documentation Support — Built to Withstand Audit</h1>
    <p>High-end compliance documentation for healthcare, IT governance, and drone/UAV — structured to satisfy regulators and protect your organization when it matters most.</p>
    <div class="hero-ctas">
      <a href="../contact.html" class="btn-primary">Request Compliance Support</a>
      <a href="../contact.html" class="btn-outline">Schedule a Gap Assessment</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="section-inner two-col">
    <div>
      <div class="content-block">
        <div class="problem-box">
          <h3>The Compliance Documentation Problem</h3>
          <p>An audit-ready compliance document is not simply a policy written in formal language — it is a structured, versioned, evidence-linked artifact. Most organizations lack the internal expertise to produce documentation at that standard. The consequence: failed audits, regulatory findings, and costly remediation cycles.</p>
        </div>
      </div>
      <div class="content-block">
        <h3>PANTAN's Approach</h3>
        <p>We build compliance documentation packages that reflect how regulators actually evaluate evidence. Our team includes specialists in healthcare (HIPAA), IT governance (data privacy, vendor management, access control policy), and drone/UAV operations (FAA Part 107, LAANC). Every engagement begins with a gap analysis — identifying what exists, what's missing, and what needs to be rewritten.</p>
      </div>
      <div class="content-block">
        <h3>Outcomes Clients Achieve</h3>
        <ul class="benefits-list">
          <li>Audit-ready documentation packages structured to the evidentiary standards of your regulators</li>
          <li>Gap analysis reports identifying missing, outdated, and non-compliant documentation</li>
          <li>Policy and procedure development across HIPAA, IT governance, and FAA Part 107 frameworks</li>
          <li>Drone/UAV: risk assessments, CONOPS, waiver packages, and operational procedure manuals</li>
          <li>IT policy suites: access control policies, data retention schedules, vendor management frameworks</li>
          <li>Ongoing documentation maintenance retainers as regulations evolve</li>
        </ul>
      </div>
      <div class="content-block">
        <h3>Frameworks We Work In</h3>
        <div class="diff-grid">
          <div class="diff-item"><h5>Healthcare: HIPAA / HITECH</h5><p>Privacy and security policies, risk assessments, BAA frameworks, breach response documentation.</p></div>
          <div class="diff-item"><h5>IT Governance &amp; Data Privacy</h5><p>IT policy frameworks, data privacy documentation, vendor management policies, access control standards.</p></div>
          <div class="diff-item"><h5>Drone / UAV: FAA Part 107</h5><p>CONOPS, airspace authorization packages, safety case reports, and UAS procedure manuals.</p></div>
          <div class="diff-item"><h5>Staffing &amp; HR Compliance</h5><p>PAF documentation, employment policy frameworks, 29 CFR compliance documentation, and audit-ready HR records.</p></div>
        </div>
      </div>
    </div>
    <div>
      <div class="sidebar-card">
        <h4>Start with a Gap Assessment</h4>
        <p>Tell us your regulatory environment and current documentation status. We'll map a path to close every gap.</p>
        <div class="sidebar-cta-group">
          <a href="../contact.html" class="btn-teal">Request a Gap Assessment</a>
          <a href="../contact.html" class="btn-navy">Discuss a Retainer</a>
        </div>
        <div class="sidebar-meta">
          <strong>Industries We Document For:</strong>
          Healthcare Providers · IT Service Companies · Managed Service Providers · Drone / UAS Operators · Staffing Firms · Government Contractors · SaaS Companies
        </div>
      </div>
    </div>
  </div>
</section>
<div class="cta-band">
  <div style="max-width:560px;margin:0 auto;">
    <h2>Documentation That Holds Up Under Scrutiny.</h2>
    <p>When regulators come calling, your compliance documentation either works or it doesn't. PANTAN makes sure it works.</p>
    <a href="../contact.html" class="btn-white">Begin Your Assessment</a>
  </div>
</div>"""

write(f"{OUT}/services/regulatory-compliance.html",
      page("Regulatory Compliance & Documentation Support | PANTAN Technologies",
           "High-end regulatory compliance documentation for healthcare (HIPAA), IT governance, and drone/UAV (FAA Part 107) — structured to withstand audit.",
           regulatory_body, depth=1))

# ─────────────────────────────────────────────
# SERVICE: PAF MANAGEMENT
# ─────────────────────────────────────────────
paf_body = """
<section class="service-hero" style="border-bottom:3px solid var(--gold);">
  <div class="service-hero-inner">
    <p class="crumb"><a href="index.html">← Services</a> / PAF Management Platform</p>
    <div style="display:inline-flex;align-items:center;gap:8px;background:rgba(184,134,11,0.15);border:1px solid rgba(184,134,11,0.35);color:var(--gold-light);font-size:.72rem;font-weight:700;padding:4px 12px;border-radius:4px;letter-spacing:.6px;text-transform:uppercase;margin-bottom:1rem;">⬡ SaaS Product</div>
    <h1>Public Access File Management SaaS — Compliance on Autopilot for Staffing Firms</h1>
    <p>PANTAN's PAF Management Platform eliminates the audit risk of manual Public Access File management — replacing spreadsheet chaos with automated workflows, real-time dashboards, and audit-ready documentation, integrated with PANTAN's documentation team.</p>
    <div class="hero-ctas">
      <a href="../contact.html" class="btn-gold">Schedule a Platform Demo</a>
      <a href="../contact.html" class="btn-outline">Request Pricing</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="section-inner two-col">
    <div>
      <div class="content-block">
        <div class="problem-box">
          <h3>The PAF Compliance Problem</h3>
          <p>Staffing firms sponsoring H-1B workers are legally required to maintain accurate, complete Public Access Files. Most manage PAFs through shared drives and manual checklists — creating dangerous gaps that only surface when a DOL audit begins. Non-compliant PAFs carry significant penalty exposure.</p>
        </div>
      </div>
      <div class="content-block">
        <h3>How the PANTAN PAF Platform Solves It</h3>
        <p>Our PAF Management SaaS creates a structured, searchable, version-controlled repository for every PAF — with automated completeness checks, expiration alerts, and one-click audit-ready exports. When the platform flags a gap, PANTAN's compliance team resolves it within the same workflow.</p>
      </div>
      <div class="content-block">
        <h3>Platform Features</h3>
        <div class="feature-grid">
          <div class="feature-item"><div class="f-icon">📁</div><h5>Structured PAF Repository</h5><p>Organized, searchable storage for all required PAF components by position and employee.</p></div>
          <div class="feature-item"><div class="f-icon">✅</div><h5>Automated Completeness Checks</h5><p>Flags missing or expiring documents before they become audit liabilities.</p></div>
          <div class="feature-item"><div class="f-icon">📊</div><h5>Real-Time Compliance Dashboard</h5><p>Portfolio-wide PAF status across all positions, locations, and placements.</p></div>
          <div class="feature-item"><div class="f-icon">⏰</div><h5>Expiration &amp; Renewal Alerts</h5><p>Automated notifications for LCA renewals, posting expirations, and document updates.</p></div>
          <div class="feature-item"><div class="f-icon">📤</div><h5>Audit-Ready Export</h5><p>One-click DOL audit response packages formatted to regulatory specification.</p></div>
          <div class="feature-item"><div class="f-icon">🔗</div><h5>PANTAN Services Integration</h5><p>Flagged gaps connect directly to PANTAN's compliance team for same-workflow resolution.</p></div>
        </div>
      </div>
      <div class="content-block">
        <h3>Why PANTAN PAF vs. General Document Tools</h3>
        <div class="diff-grid">
          <div class="diff-item"><h5>H-1B Native Design</h5><p>Built specifically for PAF compliance — not a generic document tool retrofitted for visa compliance use.</p></div>
          <div class="diff-item"><h5>Services-Integrated</h5><p>The only PAF platform where flagged gaps are resolved by the same company that built the platform.</p></div>
          <div class="diff-item"><h5>Audit Simulation Mode</h5><p>Run a mock DOL audit against your current PAF portfolio — identify exposure before regulators do.</p></div>
          <div class="diff-item"><h5>Multi-Client Architecture</h5><p>Designed for staffing firms managing compliance across multiple employer clients and job sites.</p></div>
        </div>
      </div>
    </div>
    <div>
      <div class="sidebar-card gold-sidebar">
        <h4>See the PAF Platform in Action</h4>
        <p>Schedule a 30-minute live demo. We'll walk through your PAF environment and show how the platform eliminates your audit exposure.</p>
        <div class="sidebar-cta-group">
          <a href="../contact.html" class="btn-teal">Schedule a Demo</a>
          <a href="../contact.html" class="btn-navy">Request Platform Pricing</a>
        </div>
        <div class="sidebar-meta">
          <strong>Designed For:</strong>
          H-1B Sponsoring Staffing Firms · IT Consulting &amp; Placement Firms · Healthcare Staffing Agencies · Multi-Site Contractors · Compliance Officers &amp; HR Leaders
        </div>
      </div>
    </div>
  </div>
</section>
<div class="cta-band gold-band">
  <div style="max-width:560px;margin:0 auto;">
    <h2>Stop Managing PAFs in Spreadsheets.</h2>
    <p>The next DOL audit won't wait for you to get organized. PANTAN's PAF platform puts your compliance on autopilot.</p>
    <a href="../contact.html" class="btn-white btn-white-gold">Book Your Demo Now</a>
  </div>
</div>"""

write(f"{OUT}/services/paf-management.html",
      page("Public Access File (PAF) Management SaaS | PANTAN Technologies",
           "Purpose-built PAF Management SaaS for H-1B staffing firms. Automated completeness checks, real-time compliance dashboards, and audit-ready DOL export packages.",
           paf_body, depth=1))

# ─────────────────────────────────────────────
# SERVICE: GOVERNMENT PROCUREMENT
# ─────────────────────────────────────────────
gov_body = """
<section class="service-hero">
  <div class="service-hero-inner">
    <p class="crumb"><a href="index.html">← Services</a> / Government Vendor &amp; Procurement Documentation</p>
    <h1>Government Vendor Document Prep — Submissions That Win. Documentation That Complies.</h1>
    <p>PANTAN prepares RFP/RFQ responses, certification submissions, capability statements, and compliance documentation for vendors competing for federal, state, and local government contracts.</p>
    <div class="hero-ctas">
      <a href="../contact.html" class="btn-primary">Start a Document Project</a>
      <a href="../partners.html" class="btn-outline">Explore Teaming</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="section-inner two-col">
    <div>
      <div class="content-block">
        <div class="problem-box">
          <h3>What Costs Vendors Government Contracts</h3>
          <p>Government procurement is won and lost on documentation quality. Vendors with superior capabilities routinely lose contracts because their proposals fail to address evaluation criteria with precision or include non-compliant certification declarations. The documentation is the differentiator.</p>
        </div>
      </div>
      <div class="content-block">
        <h3>How PANTAN Prepares Winning Documentation</h3>
        <p>We analyze solicitation requirements, evaluation factors, and agency context before drafting. Every RFP response is structured to address mandatory requirements and score well against evaluation criteria. We also support the full certification ecosystem — WBE, DBE, MBE, SBA 8(a), HUBZone — applying the same expertise PANTAN uses for our own government positioning.</p>
      </div>
      <div class="content-block">
        <h3>What We Deliver</h3>
        <ul class="benefits-list">
          <li>RFP and RFQ response preparation — compliant with solicitation structure and formatting requirements</li>
          <li>Capability statements and company profiles for specific agency contexts</li>
          <li>WBE, DBE, MBE, SBA 8(a), and HUBZone certification application packages</li>
          <li>SAM.gov registration, maintenance, and annual renewal documentation</li>
          <li>Subcontracting plans and small business utilization documentation for prime contractors</li>
          <li>Past performance narratives, technical approach sections, and management plans</li>
        </ul>
      </div>
      <div class="content-block">
        <h3>PANTAN's Government Documentation Advantage</h3>
        <div class="diff-grid">
          <div class="diff-item"><h5>We've Done This for Ourselves</h5><p>PANTAN is actively pursuing WBE/DBE certifications — bringing firsthand process knowledge, not theoretical expertise.</p></div>
          <div class="diff-item"><h5>Evaluation-Criteria Alignment</h5><p>Every proposal is structured to speak directly to how evaluators score — not how vendors prefer to present themselves.</p></div>
          <div class="diff-item"><h5>Multi-Agency Familiarity</h5><p>Experience with federal civilian, state, and local procurement standards and the documentation differences that matter.</p></div>
          <div class="diff-item"><h5>Deadline-Driven Delivery</h5><p>Offshore capacity means solicitation deadlines are met — even when internal teams are stretched across multiple opportunities.</p></div>
        </div>
      </div>
    </div>
    <div>
      <div class="sidebar-card">
        <h4>Working on a Government Opportunity?</h4>
        <p>Share your solicitation or certification goal. We'll assess scope and respond within 48 hours with a clear plan.</p>
        <div class="sidebar-cta-group">
          <a href="../contact.html" class="btn-teal">Submit a Documentation Request</a>
          <a href="../contact.html" class="btn-navy">Discuss Ongoing Support</a>
        </div>
        <div class="sidebar-meta">
          <strong>Documents We Prepare:</strong>
          RFP / RFQ Responses · Capability Statements · Technical Approach Narratives · WBE / DBE Applications · SBA 8(a) Submissions · SAM.gov Profiles · Subcontracting Plans
        </div>
      </div>
    </div>
  </div>
</section>
<div class="cta-band">
  <div style="max-width:560px;margin:0 auto;">
    <h2>Documentation That Competes. Submissions That Win.</h2>
    <p>Give your organization the documentation advantage government contracts demand.</p>
    <a href="../contact.html" class="btn-white">Begin Your Document Project</a>
  </div>
</div>"""

write(f"{OUT}/services/government-procurement.html",
      page("Government Vendor & Procurement Documentation | PANTAN Technologies",
           "RFP/RFQ response preparation, WBE/DBE certification packages, capability statements, and SAM.gov documentation for government vendors.",
           gov_body, depth=1))

# ─────────────────────────────────────────────
# CAREERS
# ─────────────────────────────────────────────
careers_body = """
<section class="service-hero">
  <div class="service-hero-inner">
    <h1>Careers at PANTAN Technologies</h1>
    <p>Join a fast-growing compliance and documentation firm serving enterprise, healthcare, and government clients. We offer internships, clinical placements, IT roles, and more — in a mission-driven environment built for growth.</p>
    <div class="hero-ctas">
      <a href="contact.html" class="btn-primary">Submit Your Resume</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-head">
      <div class="section-label">Open Positions</div>
      <h2 class="section-title">Current Openings</h2>
      <p class="section-intro">We partner with enterprise clients and healthcare networks to place qualified professionals in contract, travel, and internship roles. All positions are actively recruiting.</p>
    </div>
    <div class="job-filters">
      <button class="job-filter active" onclick="filterJobs('all',this)">All Openings</button>
      <button class="job-filter" onclick="filterJobs('healthcare',this)">Healthcare</button>
      <button class="job-filter" onclick="filterJobs('it',this)">Information Technology</button>
      <button class="job-filter" onclick="filterJobs('internship',this)">Internships</button>
    </div>
    <div class="jobs-grid" id="jobs-grid">

      <div class="job-card" data-cat="healthcare">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">🔬</span><span class="job-status">Open</span><span class="job-category-badge">Healthcare — Allied Health</span></div>
          <div class="job-title">Cardiac Catheterization Technician</div>
          <div class="job-meta"><span>🏢 Henry Ford Jackson Hospital</span><span>📍 Jackson, MI</span><span>💼 Contract · 13 weeks (renewable)</span><span>💰 Competitive</span></div>
          <p class="job-desc">Skilled Cardiac Cath Lab Technician needed for a busy cardiac catheterization lab. Must have experience in diagnostic and interventional procedures. RCIS certification preferred.</p>
          <div class="job-tags"><span class="job-tag">Cath Lab</span><span class="job-tag">Interventional</span><span class="job-tag">RCIS</span><span class="job-tag">BLS</span><span class="job-tag">ACLS</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

      <div class="job-card" data-cat="healthcare">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">🩺</span><span class="job-status">Open</span><span class="job-category-badge">Healthcare — Nursing</span></div>
          <div class="job-title">Registered Nurse — ICU (Travel)</div>
          <div class="job-meta"><span>🏢 HWL Health System</span><span>📍 Utica, NY</span><span>💼 Travel Contract · 13 weeks</span><span>💰 Competitive</span></div>
          <p class="job-desc">Experienced ICU Travel RN needed for a high-acuity critical care unit. Must have minimum 2 years recent ICU experience. BLS and ACLS required. Compact license preferred.</p>
          <div class="job-tags"><span class="job-tag">ICU</span><span class="job-tag">Critical Care</span><span class="job-tag">BLS</span><span class="job-tag">ACLS</span><span class="job-tag">Travel RN</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

      <div class="job-card" data-cat="healthcare">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">🧠</span><span class="job-status">Open</span><span class="job-category-badge">Healthcare — Behavioral Health</span></div>
          <div class="job-title">Mental Health Clinician</div>
          <div class="job-meta"><span>🏢 NYC Health + Hospitals</span><span>📍 New York, NY (Rikers Island)</span><span>💼 Contract · 6 months</span><span>💰 Competitive</span></div>
          <p class="job-desc">Licensed mental health clinician needed for a correctional healthcare setting. LCSW or LMHC license required. Experience with forensic or correctional populations strongly preferred.</p>
          <div class="job-tags"><span class="job-tag">LCSW</span><span class="job-tag">LMHC</span><span class="job-tag">Behavioral Health</span><span class="job-tag">Correctional</span><span class="job-tag">Mental Health</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

      <div class="job-card" data-cat="healthcare">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">🏥</span><span class="job-status">Open</span><span class="job-category-badge">Healthcare — Pharmacy</span></div>
          <div class="job-title">Clinical Pharmacist — Hospital (Travel)</div>
          <div class="job-meta"><span>🏢 Regional Medical Center</span><span>📍 Detroit, MI</span><span>💼 Travel Contract · 13 weeks</span><span>💰 Competitive</span></div>
          <p class="job-desc">Clinical Pharmacist needed to support inpatient hospital pharmacy operations. PharmD required. Must hold active state licensure. Experience in acute care or critical care pharmacy preferred.</p>
          <div class="job-tags"><span class="job-tag">PharmD</span><span class="job-tag">Inpatient Pharmacy</span><span class="job-tag">Acute Care</span><span class="job-tag">Travel</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

      <div class="job-card" data-cat="it">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">🏥</span><span class="job-status">Open</span><span class="job-category-badge">Information Technology — Healthcare IT</span></div>
          <div class="job-title">EHR Systems Analyst — Epic (Remote)</div>
          <div class="job-meta"><span>🏢 Integrated Health System</span><span>📍 Remote (U.S.)</span><span>💼 Contract · 12 months</span><span>💰 $75–95/hr</span></div>
          <p class="job-desc">Experienced EHR Systems Analyst to support Epic implementation, optimization, and end-user support. Must have hands-on Epic build and configuration experience. Epic certification(s) required. HIPAA environment experience essential.</p>
          <div class="job-tags"><span class="job-tag">Epic EHR</span><span class="job-tag">HL7 / FHIR</span><span class="job-tag">HIPAA</span><span class="job-tag">Clinical Workflow</span><span class="job-tag">Healthcare IT</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

      <div class="job-card" data-cat="it">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">☁️</span><span class="job-status">Open</span><span class="job-category-badge">Information Technology — Cloud</span></div>
          <div class="job-title">Cloud Infrastructure Engineer (AWS / Azure)</div>
          <div class="job-meta"><span>🏢 Federal Agency Contractor</span><span>📍 Hybrid — Washington, DC</span><span>💼 Contract · 6 months (renewable)</span><span>💰 $100–125/hr</span></div>
          <p class="job-desc">Cloud Infrastructure Engineer to design, deploy, and manage cloud environments for a federal agency IT modernization program. Must hold active Secret clearance or be clearance-eligible. AWS Solutions Architect or Azure Expert certification required.</p>
          <div class="job-tags"><span class="job-tag">AWS</span><span class="job-tag">Azure</span><span class="job-tag">IaC / Terraform</span><span class="job-tag">FedRAMP</span><span class="job-tag">Secret Clearance</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

      <div class="job-card" data-cat="it">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">🗄️</span><span class="job-status">Open</span><span class="job-category-badge">Information Technology — Data Engineering</span></div>
          <div class="job-title">Senior Data Engineer (Healthcare Analytics)</div>
          <div class="job-meta"><span>🏢 Regional Health Network</span><span>📍 Remote (U.S.)</span><span>💼 Contract · 12 months</span><span>💰 $90–115/hr</span></div>
          <p class="job-desc">Senior Data Engineer to build and maintain enterprise healthcare data pipelines. Must have deep experience with Python, SQL, Apache Spark, and cloud data platforms (Snowflake, Databricks, or Redshift). HIPAA data environment experience required.</p>
          <div class="job-tags"><span class="job-tag">Python</span><span class="job-tag">SQL</span><span class="job-tag">Apache Spark</span><span class="job-tag">Snowflake</span><span class="job-tag">HIPAA</span><span class="job-tag">ETL/ELT</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

      <div class="job-card" data-cat="internship">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">🎓</span><span class="job-status">Open</span><span class="job-category-badge">Internship — STEM</span><span class="internship-tag">Internship</span></div>
          <div class="job-title">Software Engineering Intern (Full-Stack)</div>
          <div class="job-meta"><span>🏢 PANTAN Technologies</span><span>📍 Remote / Addison, TX</span><span>💼 Summer · 10–12 weeks</span><span>💰 Stipend</span></div>
          <p class="job-desc">Work alongside our engineering team to build features for our PAF Management SaaS platform. You'll contribute to production code in a React/Node.js stack, write tests, and participate in code review. Rising junior or senior in CS, Software Engineering, or related STEM degree.</p>
          <div class="job-tags"><span class="job-tag">React</span><span class="job-tag">Node.js</span><span class="job-tag">JavaScript</span><span class="job-tag">REST APIs</span><span class="job-tag">Git</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

      <div class="job-card" data-cat="internship">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">🎓</span><span class="job-status">Open</span><span class="job-category-badge">Internship — STEM</span><span class="internship-tag">Internship</span></div>
          <div class="job-title">Data Science &amp; Analytics Intern</div>
          <div class="job-meta"><span>🏢 PANTAN Technologies</span><span>📍 Remote / Addison, TX</span><span>💼 Summer · 10–12 weeks</span><span>💰 Stipend</span></div>
          <p class="job-desc">Work with PANTAN's product and operations teams to analyze compliance tracking data, build dashboards, and develop predictive models for audit risk scoring. Rising junior/senior in Data Science, Mathematics, Statistics, or Computer Science.</p>
          <div class="job-tags"><span class="job-tag">Python</span><span class="job-tag">SQL</span><span class="job-tag">Pandas</span><span class="job-tag">Tableau / Power BI</span><span class="job-tag">Machine Learning</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

      <div class="job-card" data-cat="internship">
        <div class="job-card-top"><div class="job-left">
          <div class="job-category-row"><span class="job-dept-icon">🎓</span><span class="job-status">Open</span><span class="job-category-badge">Internship — Healthcare IT</span><span class="internship-tag">Internship</span></div>
          <div class="job-title">Healthcare IT &amp; Compliance Intern</div>
          <div class="job-meta"><span>🏢 PANTAN Technologies</span><span>📍 Remote / Addison, TX</span><span>💼 Summer · 10–12 weeks</span><span>💰 Stipend</span></div>
          <p class="job-desc">Support PANTAN's compliance team in preparing HIPAA documentation packages, PAF audits, and IT governance policy drafts. You'll conduct literature reviews, help draft control documentation, and participate in client gap assessment projects. Rising junior/senior in Health Informatics, Information Systems, or Healthcare Administration.</p>
          <div class="job-tags"><span class="job-tag">HIPAA</span><span class="job-tag">PAF Compliance</span><span class="job-tag">IT Governance</span><span class="job-tag">Policy Writing</span><span class="job-tag">Health Informatics</span></div>
          <div class="job-actions"><a href="contact.html" class="btn-sm btn-sm-teal">Apply Now →</a></div>
        </div></div>
      </div>

    </div>
  </div>
</section>
<div class="cta-band">
  <div style="max-width:560px;margin:0 auto;">
    <h2>Don't See Your Role?</h2>
    <p>We're always looking for exceptional talent in compliance, documentation, healthcare, and technology. Send us your resume and we'll reach out when the right opening appears.</p>
    <a href="contact.html" class="btn-white">Submit an Open Application</a>
  </div>
</div>"""

write(f"{OUT}/careers.html",
      page("Careers | PANTAN Technologies",
           "Open positions in healthcare staffing, IT, and STEM internships at PANTAN Technologies — Addison, TX and remote.",
           careers_body, depth=0))

# ─────────────────────────────────────────────
# ABOUT
# ─────────────────────────────────────────────
about_body = """
<section class="service-hero">
  <div class="service-hero-inner">
    <h1>Precision. Expertise. Accountability.</h1>
    <p>PANTAN Technologies was built to serve organizations that operate in high-stakes compliance environments — where documentation quality is not a preference, it is an operational and legal requirement.</p>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="about-grid">
      <div>
        <div class="section-label">Our Story</div>
        <h2 class="section-title">A Compliance Partner Built for the Most Demanding Clients</h2>
        <p style="color:var(--slate-600);line-height:1.8;margin-bottom:1.25rem;">PANTAN Technologies was founded to address a persistent gap: organizations operating in regulated, government-adjacent, and enterprise environments consistently lacked access to documentation and compliance support at the standard those environments actually require. Internal teams were stretched. Generic vendors couldn't match the specificity of regulatory frameworks. And the cost of documentation failures was far too high to accept.</p>
        <p style="color:var(--slate-600);line-height:1.8;margin-bottom:1.25rem;">Over more than a decade, PANTAN developed deep expertise across contract documentation, regulatory compliance, government procurement, and — most recently — a purpose-built SaaS product for Public Access File management. Our client base spans healthcare organizations, IT firms, drone/UAV operators, staffing companies, and government contractors.</p>
        <p style="color:var(--slate-600);line-height:1.8;">Today PANTAN operates a hybrid delivery model: U.S.-based compliance leadership manages every client engagement and reviews every deliverable, while our trained offshore documentation team provides the depth, speed, and 24/7 capacity that high-volume compliance work demands.</p>
      </div>
      <div>
        <div class="about-visual">
          <div class="big-stat">10+</div>
          <div class="big-label">Years in Compliance &amp; Documentation</div>
          <div class="about-pills">
            <span class="about-pill">Contract Review</span>
            <span class="about-pill">Regulatory Documentation</span>
            <span class="about-pill">PAF SaaS Platform</span>
            <span class="about-pill">Government Procurement</span>
            <span class="about-pill">HIPAA · IT Governance</span>
            <span class="about-pill">FAA Part 107 / UAV</span>
            <span class="about-pill">RFP Response Writing</span>
            <span class="about-pill">24/7 Offshore Delivery</span>
            <span class="about-pill">U.S.-Based Oversight</span>
            <span class="about-pill">WBE In Progress</span>
            <span class="about-pill">DBE In Progress</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="section-inner">
    <div class="section-head centered">
      <div class="section-label">Our Delivery Model</div>
      <h2 class="section-title">Offshore Depth. U.S. Accountability.</h2>
      <p class="section-intro">What separates PANTAN from traditional documentation outsourcing is the architecture of our oversight — and the depth of regulatory specialization at every layer.</p>
    </div>
    <div class="trust-grid">
      <div class="trust-card"><div class="t-icon">🇺🇸</div><h4>U.S.-Based Compliance Leadership</h4><p>All client relationships and final document review are managed by U.S.-based compliance leads. Every deliverable is reviewed before release.</p></div>
      <div class="trust-card"><div class="t-icon">🌐</div><h4>Offshore Documentation Team</h4><p>Our trained offshore specialists handle drafting, organization, and version control — operating 24/7 to meet aggressive client timelines.</p></div>
      <div class="trust-card"><div class="t-icon">🔍</div><h4>Structured QA Process</h4><p>Every deliverable passes through a defined quality checkpoint ensuring regulatory accuracy and structural completeness.</p></div>
      <div class="trust-card"><div class="t-icon">⚙️</div><h4>SaaS + Services Integration</h4><p>Our PAF platform works in tandem with our documentation services — seamless from gap identification to document resolution.</p></div>
      <div class="trust-card"><div class="t-icon">📋</div><h4>Industry-Specific Expertise</h4><p>Healthcare, IT governance, UAV, and government procurement — deep working knowledge of the regulatory frameworks governing each.</p></div>
      <div class="trust-card"><div class="t-icon">🤝</div><h4>Dedicated Client Engagement</h4><p>Every client has a named account lead. Direct access to the person accountable for your engagement, every time.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-head centered">
      <div class="section-label">Certifications</div>
      <h2 class="section-title">Transparent About Where We Stand</h2>
      <p class="section-intro">We are a WBE/DBE-in-progress firm actively pursuing certifications. Here is exactly what that means for clients who need diverse supplier documentation today.</p>
    </div>
    <div class="cert-grid">
      <div class="cert-card"><div class="cert-status status-progress">In Progress</div><h5>WBE Certification</h5><p>WBENC certification application is actively in process. Many enterprise diversity programs accept in-progress status — contact us for a current status letter.</p></div>
      <div class="cert-card"><div class="cert-status status-progress">In Progress</div><h5>DBE Certification</h5><p>State transportation agency DBE filing in progress. Supports transportation-funded contract diversity goals and select federal procurement vehicles.</p></div>
      <div class="cert-card"><div class="cert-status status-active">Available</div><h5>Supplier Diversity Letters</h5><p>We provide ownership documentation and in-progress certification evidence for clients who need supplier diversity credit now.</p></div>
      <div class="cert-card"><div class="cert-status status-active">Committed</div><h5>Transparency First</h5><p>We will never overstate our certification status. What is documented here is accurate and can be used for supplier diversity reporting with confidence.</p></div>
      <div class="cert-card"><div class="cert-status status-active">Verified</div><h5>WBE/DBE In-Progress Documentation</h5><p>Contact us to request a formal letter documenting our certification application status, suitable for prime contractor subcontracting plan submissions.</p></div>
      <div class="cert-card"><div class="cert-status status-active">Active</div><h5>Government Vendor Registration</h5><p>SAM.gov registered and maintained. DUNS/UEI verified. Available for federal and state procurement vehicle participation upon contract award.</p></div>
    </div>
  </div>
</section>
<div class="cta-band">
  <div style="max-width:560px;margin:0 auto;">
    <h2>Ready to Work with a High-End Compliance Partner?</h2>
    <p>Whether you need documentation support, the PAF platform, or a certified-diverse subcontractor — PANTAN is ready to engage.</p>
    <a href="contact.html" class="btn-white">Start the Conversation</a>
  </div>
</div>"""

write(f"{OUT}/about.html",
      page("About | PANTAN Technologies",
           "PANTAN Technologies — 10+ years in compliance documentation, U.S.-managed offshore delivery, WBE/DBE certification in progress. Addison, TX.",
           about_body, depth=0))

# ─────────────────────────────────────────────
# PARTNERS
# ─────────────────────────────────────────────
partners_body = """
<section class="service-hero">
  <div class="service-hero-inner">
    <h1>Partner with PANTAN Technologies</h1>
    <p>Whether you're a prime contractor seeking a diverse documentation subcontractor, an enterprise organization needing ongoing compliance support, or a government vendor looking for a procurement documentation partner — PANTAN is built for that engagement.</p>
    <div class="hero-ctas">
      <a href="contact.html" class="btn-primary">Initiate a Partnership</a>
      <a href="about.html" class="btn-outline">About Our Firm</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-head centered">
      <div class="section-label">How It Works</div>
      <h2 class="section-title">A Clear Path from First Contact to Full Delivery</h2>
    </div>
    <div class="process-steps">
      <div class="step"><div class="step-num">1</div><h4>Discovery Consultation</h4><p>A focused call to understand your documentation environment, compliance obligations, and timeline. No sales pitch — just an honest assessment.</p></div>
      <div class="step"><div class="step-num">2</div><h4>Scope &amp; Proposal</h4><p>A clear, itemized proposal covering deliverables, timeline, and pricing — within 48 hours of the discovery call.</p></div>
      <div class="step"><div class="step-num">3</div><h4>Engagement Launch</h4><p>Agreement executed, account lead assigned, kickoff scheduled. Work begins typically within five business days of signature.</p></div>
      <div class="step"><div class="step-num">4</div><h4>Delivery &amp; Ongoing Support</h4><p>Documents delivered on schedule, reviewed before release, and supported post-delivery. Retainer clients receive priority response SLAs.</p></div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="section-inner">
    <div class="section-head centered">
      <div class="section-label">Case Studies</div>
      <h2 class="section-title">Results That Speak for Themselves</h2>
    </div>
    <div class="case-studies-grid">
      <div class="case-card">
        <div class="case-header"><span class="case-tag">Contract Documentation</span><h4>MSA &amp; SOW Template Library for a Mid-Size IT Consulting Firm</h4></div>
        <div class="case-body"><p>A 60-person IT consulting firm was executing contracts using five different legacy MSA templates — none reviewed for regulatory alignment. Contract disputes were creating friction with enterprise clients.</p><p>PANTAN conducted a gap analysis, produced a consolidated MSA with compliant SOW modules, and implemented version control protocols.</p><div class="case-result">✓ Legal review cycle: 14 days → 3. Zero contract disputes in 12 months following.</div></div>
      </div>
      <div class="case-card">
        <div class="case-header"><span class="case-tag gold">PAF SaaS</span><h4>H-1B PAF Compliance Overhaul for a Healthcare Staffing Firm</h4></div>
        <div class="case-body"><p>A healthcare staffing firm with 40+ active H-1B sponsorships had no centralized PAF management. Files scattered across four shared drives. A DOL audit was initiated with 10 days notice.</p><p>PANTAN deployed the PAF Platform in emergency mode, consolidated all PAF folders, identified and remediated 17 documentation gaps, and assembled a complete audit response package in 8 days.</p><div class="case-result">✓ 17 gaps closed in 8 days. DOL audit closed with no findings.</div></div>
      </div>
      <div class="case-card">
        <div class="case-header"><span class="case-tag">Government Procurement</span><h4>First RFP Response for a UAS Services Company</h4></div>
        <div class="case-body"><p>A drone services company identified a state agency RFP for UAS inspection services with a 21-day response window and no internal documentation capability.</p><p>PANTAN developed a complete RFP response package — technical approach, past performance, pricing narrative, and a FAA Part 107 compliance appendix. The firm was awarded a 12-month pilot contract.</p><div class="case-result">✓ First government submission. Contract awarded. 12-month pilot secured.</div></div>
      </div>
    </div>
  </div>
</section>
<div class="cta-band">
  <div style="max-width:560px;margin:0 auto;">
    <h2>Ready to Start a Partnership?</h2>
    <p>Tell us about your organization and documentation need. We respond within one business day.</p>
    <a href="contact.html" class="btn-white">Initiate a Partnership →</a>
  </div>
</div>"""

write(f"{OUT}/partners.html",
      page("Partners & Case Studies | PANTAN Technologies",
           "Partner with PANTAN Technologies for high-end compliance documentation. See case studies in contract review, PAF SaaS, and government procurement.",
           partners_body, depth=0))

# ─────────────────────────────────────────────
# CONTACT
# ─────────────────────────────────────────────
contact_body = """
<section class="service-hero">
  <div class="service-hero-inner">
    <h1>Let's Talk About What You Need</h1>
    <p>Our compliance specialists will assess your situation and recommend a clear path forward. We respond within one business day.</p>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="contact-3col">
      <div class="contact-cta-card">
        <div class="cta-icon">📋</div>
        <h4>Request a Capabilities Statement</h4>
        <p>Need our company profile or certification letters for a procurement submission? Request it here.</p>
        <a href="#" onclick="document.getElementById('contact-subject').value='Capabilities Statement Request'" class="btn-teal" style="width:100%;margin-bottom:.75rem;">Request Capabilities Statement</a>
        <hr style="border:none;border-top:1px solid rgba(255,255,255,0.12);width:100%;margin:.5rem 0;">
        <div class="cta-icon" style="margin-top:.75rem;">🗂️</div>
        <h4>Schedule a PAF Demo</h4>
        <p>See our PAF Management SaaS platform in action. 30-minute live session with a compliance specialist.</p>
        <a href="#" onclick="document.getElementById('contact-subject').value='PAF Management SaaS — Demo Request'" class="btn-gold" style="width:100%;text-align:center;border-radius:8px;">Schedule a Demo</a>
        <hr style="border:none;border-top:1px solid rgba(255,255,255,0.12);width:100%;margin:.75rem 0;">
        <div style="font-size:.78rem;color:rgba(255,255,255,0.45);line-height:1.6;">
          📍 5080 Spectrum Drive, Suite 575E<br>Addison, TX 75001<br><br>
          📧 info@pan-tan.com<br><br>
          ⏱️ Response within 1 business day
        </div>
      </div>
      <div class="form-card">
        <h4>Send Us a Message</h4>
        <form id="contact-form" class="form-grid" onsubmit="handleFormSubmit(event)">
          <div class="form-group"><label>First Name *</label><input type="text" required placeholder="Jane"></div>
          <div class="form-group"><label>Last Name *</label><input type="text" required placeholder="Smith"></div>
          <div class="form-group"><label>Organization *</label><input type="text" required placeholder="Your Organization Name"></div>
          <div class="form-group"><label>Work Email *</label><input type="email" required placeholder="jane@company.com"></div>
          <div class="form-group"><label>Phone</label><input type="tel" placeholder="(555) 000-0000"></div>
          <div class="form-group"><label>Subject / Service *</label>
            <select id="contact-subject" required>
              <option value="">Select a subject...</option>
              <option>Contract Review &amp; Template Preparation</option>
              <option>Regulatory Compliance Documentation — HIPAA</option>
              <option>Regulatory Compliance Documentation — IT Governance</option>
              <option>Regulatory Compliance Documentation — Drone / FAA Part 107</option>
              <option>PAF Management SaaS — Demo Request</option>
              <option>PAF Management SaaS — Pricing Inquiry</option>
              <option>Government Vendor / RFP Documentation</option>
              <option>Government Certification Application (WBE/DBE/SBA)</option>
              <option>Teaming / Subcontracting Inquiry</option>
              <option>Capabilities Statement Request</option>
              <option>Retainer / Ongoing Compliance Support</option>
              <option>Careers / Employment Inquiry</option>
              <option>General Inquiry</option>
            </select>
          </div>
          <div class="form-group full"><label>How Can We Help? *</label><textarea required placeholder="Describe your compliance environment, documentation challenge, regulatory deadlines, or any other relevant context..."></textarea></div>
          <p class="form-note">By submitting this form, you agree to be contacted by PANTAN Technologies. We do not sell or share your information. See our <a href="legal/privacy.html">Privacy Policy</a>.</p>
          <div class="full" style="grid-column:1/-1;"><button type="submit" class="form-submit">Submit Your Message →</button></div>
        </form>
      </div>
      <div class="contact-cta-card">
        <div class="cta-icon">🏛️</div>
        <h4>Government &amp; Procurement Documentation</h4>
        <p>Working on a federal, state, or local solicitation? We prep RFP responses, capability statements, and certification packages fast.</p>
        <a href="#" onclick="document.getElementById('contact-subject').value='Government Vendor / RFP Documentation'" class="btn-teal" style="width:100%;margin-bottom:.75rem;">Start a Document Project</a>
        <hr style="border:none;border-top:1px solid rgba(255,255,255,0.12);width:100%;margin:.5rem 0;">
        <div class="cta-icon" style="margin-top:.75rem;">💼</div>
        <h4>Careers &amp; Open Roles</h4>
        <p>Healthcare, IT, or STEM internship? Browse our current openings or submit an open application.</p>
        <a href="careers.html" class="btn-outline" style="width:100%;text-align:center;">View Open Positions</a>
        <hr style="border:none;border-top:1px solid rgba(255,255,255,0.12);width:100%;margin:.75rem 0;">
        <div style="font-size:.78rem;color:rgba(255,255,255,0.45);line-height:1.6;">
          🔒 256-bit SSL Encrypted<br>
          ✅ GDPR Compliant<br>
          ✅ FTC Compliant<br>
          ⚖️ 29 CFR § 1625.2 Compliant<br><br>
          All submissions are secure and confidential.
        </div>
      </div>
    </div>
  </div>
</section>"""

write(f"{OUT}/contact.html",
      page("Contact | PANTAN Technologies",
           "Contact PANTAN Technologies for compliance documentation, contract review, PAF SaaS demos, or government procurement support. Addison, TX.",
           contact_body, depth=0))

# ─────────────────────────────────────────────
# LEGAL PAGES
# ─────────────────────────────────────────────

def legal_page(title, desc, h1, content, depth=1):
    body = f"""
<section class="service-hero">
  <div class="service-hero-inner">
    <p class="crumb"><a href="../index.html">← Home</a> / {h1}</p>
    <h1>{h1}</h1>
    <p>PANTAN Technologies, LLC · 5080 Spectrum Drive, Suite 575E, Addison, TX 75001 · info@pan-tan.com</p>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="legal-content">
      {content}
    </div>
  </div>
</section>"""
    return page(f"{title} | PANTAN Technologies", desc, body, depth=depth)

write(f"{OUT}/legal/terms.html", legal_page("Terms of Service", "Terms of Service for PANTAN Technologies.", "Terms of Service", """
<div class="last-updated">Effective Date: January 1, 2025</div>
<h2>1. Acceptance of Terms</h2><p>By accessing or using pan-tan.com or any services offered by PANTAN Technologies, LLC ("PANTAN"), you agree to be bound by these Terms of Service. If you do not agree, please do not use our Site or services.</p>
<h2>2. Description of Services</h2><p>PANTAN Technologies provides compliance documentation, contract review and template preparation, Public Access File (PAF) management services and SaaS platform access, government vendor and procurement documentation, regulatory compliance support, and related professional services. Specific scope, deliverables, timelines, and pricing for any engagement shall be governed by a separate written Service Agreement or Statement of Work.</p>
<h2>3. Use of the Site</h2><p>You agree to use the Site only for lawful purposes. You may not use the Site to damage, disable, overburden, or impair the Site; gain unauthorized access to any system or network; or violate any applicable local, state, national, or international laws or regulations.</p>
<h2>4. Intellectual Property</h2><p>All content on this Site is the property of PANTAN Technologies, LLC or its content suppliers and is protected by applicable intellectual property laws. You may not reproduce, distribute, or create derivative works of any Site content without prior written permission. No deliverable constitutes legal advice. PANTAN is not a law firm.</p>
<h2>5. Disclaimer of Warranties</h2><p>The Site and all Services are provided on an "as is" and "as available" basis without warranties of any kind, either express or implied. Documentation and compliance services are professional support services; they do not constitute legal advice and should not substitute for qualified legal counsel.</p>
<h2>6. Limitation of Liability</h2><p>To the fullest extent permitted by applicable law, PANTAN Technologies, LLC shall not be liable for any indirect, incidental, special, consequential, or punitive damages arising out of or related to your use of the Site or Services. PANTAN's total liability for any claim shall not exceed the amount paid by you to PANTAN in the three months preceding the claim.</p>
<h2>7. Governing Law</h2><p>These Terms shall be governed by the laws of the State of Texas. Any disputes shall be resolved exclusively in the state or federal courts located in Dallas County, Texas.</p>
<h2>8. Changes to Terms</h2><p>PANTAN reserves the right to modify these Terms at any time. Continued use of the Site following the posting of changes constitutes your acceptance of the revised Terms.</p>
<h2>9. Contact</h2><p>PANTAN Technologies, LLC · 5080 Spectrum Drive, Suite 575E, Addison, TX 75001 · info@pan-tan.com</p>"""))

write(f"{OUT}/legal/privacy.html", legal_page("Privacy Policy", "Privacy Policy for PANTAN Technologies — GDPR, CCPA, and FTC compliant.", "Privacy Policy", """
<div class="last-updated">Effective Date: January 1, 2025</div>
<div class="info-box"><p>This Privacy Policy is designed to comply with GDPR, CCPA, and applicable U.S. federal privacy frameworks. PANTAN Technologies is committed to protecting your personal information and your right to privacy.</p></div>
<h2>1. Information We Collect</h2><p>We collect information you voluntarily provide when you use our Site, submit contact forms, or request services. This may include name, email address, phone number, organization name, job title, and inquiry content. We also collect certain technical information automatically, including IP address, browser type, and pages visited, through standard server logs and analytics tools.</p>
<h2>2. How We Use Your Information</h2><p>We use collected information to respond to inquiries and service requests; provide, manage, and improve our Services; send relevant communications (with your consent where required); comply with applicable legal obligations; and prevent fraud and maintain system security.</p>
<h2>3. Legal Basis for Processing (GDPR)</h2><p>For individuals in the European Economic Area, our legal bases for processing personal data include your consent, performance of a contract with you, compliance with a legal obligation, and our legitimate interests in operating our business.</p>
<h2>4. Information Sharing</h2><p>We do not sell, trade, or rent your personal information to third parties. We may share information with trusted service providers who assist us in operating our Site and delivering Services, subject to confidentiality agreements. We may disclose information when required by law or court order.</p>
<h2>5. Data Security</h2><p>We implement 256-bit SSL encryption on all data transmissions. We employ administrative, technical, and physical safeguards designed to protect your personal information. However, no method of transmission over the internet is 100% secure.</p>
<h2>6. Your Rights</h2><p>Depending on your location, you may have the right to access, correct, or delete personal information we hold about you; opt out of certain uses of your data; and lodge a complaint with your applicable data protection authority. Contact us at info@pan-tan.com to exercise these rights.</p>
<h2>7. California Privacy Rights (CCPA)</h2><p>California residents have the right to know what personal information we collect, the right to request deletion, and the right not to be discriminated against for exercising these rights. Submit CCPA requests to info@pan-tan.com with the subject line "CCPA Privacy Request."</p>
<h2>8. Contact</h2><p>PANTAN Technologies, LLC · 5080 Spectrum Drive, Suite 575E, Addison, TX 75001 · info@pan-tan.com</p>"""))

write(f"{OUT}/legal/cookies.html", legal_page("Cookie Policy", "Cookie Policy for PANTAN Technologies.", "Cookie Policy", """
<div class="last-updated">Effective Date: January 1, 2025</div>
<h2>1. What Are Cookies?</h2><p>Cookies are small text files placed on your device by websites you visit. This Cookie Policy explains how PANTAN Technologies, LLC uses cookies and similar tracking technologies on pan-tan.com.</p>
<h2>2. Cookies We Use</h2>
<h3>Strictly Necessary Cookies</h3><p>These cookies are essential for the Site to function. They enable core functionality such as security and accessibility. You cannot opt out of these cookies as they are required for the Site to operate.</p>
<h3>Analytics Cookies</h3><p>We may use analytics cookies (such as Google Analytics) to understand how visitors interact with our Site — including pages visited, time on site, and referral sources. This information helps us improve our Site and Services. Analytics data is collected in aggregate and anonymized where possible.</p>
<h3>Functional Cookies</h3><p>Functional cookies enable enhanced functionality and personalization, such as remembering your preferences or form inputs.</p>
<h2>3. Managing Cookies</h2><p>Most web browsers allow you to control cookies through their settings preferences. If you disable cookies, some parts of the Site may not function properly. To opt out of Google Analytics, use the Google Analytics Opt-Out Browser Add-on.</p>
<h2>4. GDPR Compliance</h2><p>For users in the European Economic Area, we obtain consent before placing non-essential cookies on your device. You may withdraw consent at any time by adjusting your cookie settings or contacting us at info@pan-tan.com.</p>
<h2>5. Contact</h2><p>PANTAN Technologies, LLC · 5080 Spectrum Drive, Suite 575E, Addison, TX 75001 · info@pan-tan.com</p>"""))

write(f"{OUT}/legal/ai-terms.html", legal_page("AI Tools & Technology Use Policy", "PANTAN Technologies policy on artificial intelligence use in service delivery.", "AI Tools & Technology Use Policy", """
<div class="last-updated">Effective Date: January 1, 2025</div>
<div class="info-box"><p>PANTAN Technologies is committed to responsible, transparent use of artificial intelligence tools in our service delivery workflow.</p></div>
<h2>1. AI Use in Service Delivery</h2><p>PANTAN Technologies may use AI-assisted tools to support — not replace — the professional judgment of our compliance specialists in tasks such as document drafting, research, gap analysis, and template development. All AI-assisted work product is reviewed, edited, and approved by qualified human professionals before delivery to clients.</p>
<h2>2. Human Oversight Requirement</h2><p>No AI-generated content is delivered to clients without review and approval by a qualified PANTAN compliance professional. AI tools are used as productivity aids. Final responsibility for the accuracy, completeness, and regulatory alignment of all deliverables rests with PANTAN's human team members.</p>
<h2>3. Data Privacy in AI Tools</h2><p>PANTAN does not input personally identifiable information (PII), protected health information (PHI), or confidential client data into publicly available AI language models that retain, train on, or share user inputs. Only anonymized or de-identified content is processed where AI tools are used in compliance documentation workflows.</p>
<h2>4. Limitations of AI-Assisted Work</h2><p>AI-assisted documentation tools may not reflect the most current regulatory guidance or recent legal developments. All documentation produced for clients should be reviewed by qualified legal counsel prior to reliance for legal or regulatory compliance purposes. PANTAN's services constitute professional compliance support — not legal advice.</p>
<h2>5. Transparency to Clients</h2><p>Clients may request disclosure of whether AI tools were used in the preparation of specific deliverables. We will provide transparent disclosure upon request.</p>
<h2>6. Contact</h2><p>PANTAN Technologies, LLC · 5080 Spectrum Drive, Suite 575E, Addison, TX 75001 · info@pan-tan.com</p>"""))

write(f"{OUT}/legal/disclaimer.html", legal_page("Legal Disclaimer", "Legal disclaimer for PANTAN Technologies services and website content.", "Legal Disclaimer", """
<div class="last-updated">Effective Date: January 1, 2025</div>
<h2>Not Legal Advice</h2><p>PANTAN Technologies, LLC is not a law firm and does not provide legal advice. Nothing on this Site or in any deliverable prepared by PANTAN constitutes legal advice, creates an attorney-client relationship, or should be relied upon as a substitute for qualified legal counsel. Clients are strongly encouraged to have all documents reviewed by qualified legal counsel prior to execution or reliance for regulatory compliance purposes.</p>
<h2>Regulatory Compliance Disclaimer</h2><p>While PANTAN Technologies makes reasonable efforts to ensure that compliance documentation is accurate and aligned with applicable regulatory frameworks, regulations change frequently and may vary by jurisdiction. PANTAN cannot guarantee that any document or compliance package will satisfy the requirements of any specific regulatory body, agency, or auditor.</p>
<h2>No Guarantee of Outcomes</h2><p>PANTAN Technologies does not guarantee specific outcomes from the use of our services, including but not limited to audit clearance, contract award, certification approval, or regulatory approval. Past performance examples on this Site are representative and do not guarantee similar results for future clients.</p>
<h2>Age Discrimination Compliance — 29 CFR § 1625.2</h2><p>PANTAN Technologies is an equal opportunity employer and complies with the Age Discrimination in Employment Act (ADEA) and 29 CFR § 1625.2. PANTAN does not discriminate against applicants or employees on the basis of age (40 or older) in any employment practice, including hiring, promotion, compensation, or termination. All job postings, staffing placements, and employment communications are conducted in compliance with applicable federal and state anti-discrimination laws.</p>
<h2>FTC Compliance</h2><p>PANTAN Technologies complies with Federal Trade Commission (FTC) guidelines regarding advertising, endorsements, testimonials, and AI disclosure. Case studies and client outcomes described on this Site are representative examples based on actual engagements. Results are not guaranteed and may vary based on client circumstances.</p>
<h2>Contact</h2><p>PANTAN Technologies, LLC · 5080 Spectrum Drive, Suite 575E, Addison, TX 75001 · info@pan-tan.com</p>"""))

write(f"{OUT}/legal/accessibility.html", legal_page("Accessibility Statement", "PANTAN Technologies commitment to digital accessibility and WCAG 2.1 compliance.", "Accessibility Statement", """
<div class="last-updated">Effective Date: January 1, 2025</div>
<div class="info-box"><p>PANTAN Technologies is committed to ensuring digital accessibility for all users, including individuals with disabilities. We continually improve the user experience for everyone and apply relevant accessibility standards.</p></div>
<h2>Our Commitment</h2><p>PANTAN Technologies strives to ensure that pan-tan.com is accessible to people with disabilities. We are working toward conformance with the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA.</p>
<h2>Accessibility Features</h2>
<ul>
  <li>Semantic HTML structure for screen reader compatibility</li>
  <li>Text alternatives for non-text content</li>
  <li>Sufficient color contrast ratios for text legibility</li>
  <li>Keyboard navigability for all interactive elements</li>
  <li>Responsive design that adapts to various screen sizes and zoom levels</li>
  <li>Descriptive link text and button labels</li>
</ul>
<h2>Requesting Accessible Alternatives</h2><p>If you need information from our Site or services in an alternative accessible format, please contact us at info@pan-tan.com. We will make reasonable efforts to provide the requested information in a timely manner.</p>
<h2>Feedback &amp; Contact</h2><p>We welcome your feedback on the accessibility of pan-tan.com. PANTAN Technologies, LLC · 5080 Spectrum Drive, Suite 575E, Addison, TX 75001 · info@pan-tan.com. We aim to respond to accessibility feedback within five business days.</p>"""))

print("\n✅ All pages generated successfully!")
print(f"\nOutput directory: {OUT}")
