# PANTAN Technologies — Website

**High-End Compliance & Documentation Services**  
[pan-tan.com](https://pan-tan.com) · Addison, TX · info@pan-tan.com

---

## Project Structure

```
pantan/
├── index.html                          ← Home page
├── about.html
├── careers.html
├── contact.html
├── partners.html
│
├── services/
│   ├── index.html                      ← Services overview
│   ├── contract-review.html
│   ├── regulatory-compliance.html
│   ├── paf-management.html
│   └── government-procurement.html
│
├── legal/
│   ├── terms.html
│   ├── privacy.html
│   ├── cookies.html
│   ├── ai-terms.html
│   ├── disclaimer.html
│   └── accessibility.html
│
├── assets/
│   ├── css/styles.css                  ← All shared styles (edit once)
│   └── js/main.js                      ← Nav, mobile menu, form handler
│
├── build.py                            ← Regenerates all pages from templates
├── vercel.json                         ← Deployment config + security headers
├── robots.txt
└── sitemap.xml
```

---

## Real URLs (with cleanUrls enabled in Vercel)

| Page | URL |
|---|---|
| Home | `pan-tan.com` |
| Services | `pan-tan.com/services` |
| Contract Review | `pan-tan.com/services/contract-review` |
| Regulatory Compliance | `pan-tan.com/services/regulatory-compliance` |
| PAF Management SaaS | `pan-tan.com/services/paf-management` |
| Government Procurement | `pan-tan.com/services/government-procurement` |
| Careers | `pan-tan.com/careers` |
| About | `pan-tan.com/about` |
| Partners | `pan-tan.com/partners` |
| Contact | `pan-tan.com/contact` |
| Terms | `pan-tan.com/legal/terms` |
| Privacy | `pan-tan.com/legal/privacy` |

---

## Making Changes

### Edit shared styles (affects all pages)
```
assets/css/styles.css
```

### Edit shared JavaScript (nav, forms, filters)
```
assets/js/main.js
```

### Edit a specific page
Open and edit the `.html` file directly.

### Regenerate all pages from the Python template
```bash
python3 build.py
```
Use this when you want to update nav, footer, or head tags across all pages at once.

---

## Git Workflow

```bash
# After any change
git add .
git commit -m "Brief description of what changed"
git push origin main
```

Vercel auto-deploys within ~30 seconds of every push to `main`.

---

## First-Time Deployment to Vercel

```bash
npm install -g vercel
vercel login          # use Info@srikanthmerianda.com
vercel --prod
```

Then in **Vercel Dashboard → Settings → Domains** → add `pan-tan.com` and `www.pan-tan.com`.

---

## DNS: Bluehost → Vercel

### Step 1 — Delete WordPress from Bluehost
1. cPanel → File Manager → `public_html` → delete all files
2. cPanel → MySQL Databases → drop the WordPress database
3. cPanel → Softaculous → remove WordPress installation

### Step 2 — Update DNS Records
| Type | Host | Value | TTL |
|---|---|---|---|
| A | `@` | `76.76.21.21` | 300 |
| CNAME | `www` | `cname.vercel-dns.com` | 300 |

Delete any existing A records pointing to old Bluehost IPs first.

---

## Git Config

```bash
git config user.name "Srikanth"
git config user.email "Info@srikanthmerianda.com"
git remote add origin https://github.com/STM75001/pantan.git
git branch -M main
git push -u origin main
```
