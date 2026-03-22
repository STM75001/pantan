# PANTAN Technologies — Website

**High-End Compliance & Documentation Services**  
[pan-tan.com](https://pan-tan.com) · Addison, TX · info@pan-tan.com

---

## How This Site Works

All changes are made by the development team and delivered as a `.zip` file.

**Your workflow is always 3 commands:**
```bash
cd /c/Users/PanTan-Sancus/Projects/pantan-v2
git add .
git commit -m "Description of what changed"
git push
```
Vercel auto-deploys within ~30 seconds of every push to `main`.

---

## Project Structure

```
pantan-v2/
├── index.html                     ← pan-tan.com/
├── about.html                     ← pan-tan.com/about
├── careers.html                   ← pan-tan.com/careers
├── contact.html                   ← pan-tan.com/contact
├── partners.html                  ← pan-tan.com/partners
├── 404.html                       ← Custom not-found page
│
├── services/
│   ├── index.html                 ← pan-tan.com/services
│   ├── contract-review.html       ← pan-tan.com/services/contract-review
│   ├── regulatory-compliance.html ← pan-tan.com/services/regulatory-compliance
│   ├── paf-management.html        ← pan-tan.com/services/paf-management
│   └── government-procurement.html← pan-tan.com/services/government-procurement
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
│   ├── css/styles.css             ← ALL shared styles (one file, all pages)
│   └── js/main.js                 ← Nav, mobile menu, job filters, form handler
│
├── vercel.json                    ← Deployment config + security headers + 404
├── robots.txt                     ← Search engine directives
└── sitemap.xml                    ← 15 canonical URLs for Google
```

---

## First-Time Vercel Deployment

```bash
npm install -g vercel
vercel login          # use Info@srikanthmerianda.com
vercel --prod         # run from inside pantan-v2 folder
```

Then in **Vercel Dashboard → Settings → Domains** → add `pan-tan.com` and `www.pan-tan.com`.

---

## DNS: Bluehost → Vercel

### Step 1 — Delete WordPress from Bluehost FIRST
1. Bluehost cPanel → File Manager → `public_html` → select all → Delete
2. cPanel → MySQL Databases → drop the WordPress database
3. cPanel → Softaculous → remove the WordPress installation

### Step 2 — Set DNS records in Bluehost Zone Editor
| Type  | Host  | Value                  | TTL |
|-------|-------|------------------------|-----|
| A     | @     | 76.76.21.21            | 300 |
| CNAME | www   | cname.vercel-dns.com   | 300 |

Delete any existing A records pointing to old Bluehost IPs before adding these.

### Step 3 — Add domain in Vercel
Vercel Dashboard → Settings → Domains → Add `pan-tan.com`

---

## Git Config

```bash
git config user.name "Srikanth"
git config user.email "Info@srikanthmerianda.com"
```

GitHub repo: [github.com/STM75001/pantan](https://github.com/STM75001/pantan)
