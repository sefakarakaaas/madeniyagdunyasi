# -*- coding: utf-8 -*-
"""
Madeni Yağ Dünyası - statik site üreticisi.
Kullanım:  python3 build.py   ->  dist/ klasörünü üretir.
Cloudflare: Build command = python3 build.py, Deploy = npx wrangler deploy (wrangler.jsonc -> dist)
Sadece Python standart kütüphanesi kullanır.
"""
import json
import os
import shutil
from datetime import date
from html import escape
from urllib.parse import quote

from data import (BRANDS, CATEGORIES, OIL_FAQ, PROVINCES, PROVINCES_BY_KM,
                  REGION_NOTES, SECTORS, SITE, ZONES)

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "dist")
TODAY = date.today().isoformat()
PAGES = []  # sitemap için


def asset_version(name):
    """CSS/JS değiştiğinde tarayıcı önbelleğini kırmak için kısa içerik özeti."""
    import hashlib
    with open(os.path.join(ROOT, name), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


CSS_V = asset_version("style.css")
JS_V = asset_version("app.js")

ICONS = {
    "hydraulic": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 4c6 9 12 16 12 24a12 12 0 0 1-24 0c0-8 6-15 12-24z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M18 30a6 6 0 0 0 6 6" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>',
    "gear": '<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="7" fill="none" stroke="currentColor" stroke-width="3"/><path d="M24 4v7M24 37v7M4 24h7M37 24h7M9.9 9.9l5 5M33.1 33.1l5 5M9.9 38.1l5-5M33.1 14.9l5-5" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="24" cy="24" r="15" fill="none" stroke="currentColor" stroke-width="3"/></svg>',
    "bucket": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M6 14h30l6 10-8 14H12L6 24z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M14 38v5M22 38v5M30 38v5" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M20 14l4-9h12" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>',
    "filter": '<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="12" y="6" width="24" height="36" rx="5" fill="none" stroke="currentColor" stroke-width="3"/><path d="M12 14h24M12 34h24M18 14v20M24 14v20M30 14v20" stroke="currentColor" stroke-width="3"/></svg>',
    "truck": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M3 12h26v22H3zM29 20h9l7 8v6H29z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="12" cy="36" r="4" fill="var(--bg,#fff)" stroke="currentColor" stroke-width="3"/><circle cx="37" cy="36" r="4" fill="var(--bg,#fff)" stroke="currentColor" stroke-width="3"/></svg>',
}

def logo_mark(uid="h", shadow=True):
    """Kullanıcının verdiği logodaki parlak madeni yağ damlası (logo.svg ile aynı)."""
    sh = (f'<ellipse cx="140" cy="390" rx="78" ry="16" fill="url(#fs-{uid})"/>' if shadow else "")
    vb = "40 80 200 330" if shadow else "44 84 192 282"
    d = ("M140,90 C196,168 230,222 230,268 C230,320 189,360 140,360 "
         "C91,360 50,320 50,268 C50,222 84,168 140,90 Z")
    return (
        f'<svg class="logo-svg" viewBox="{vb}" aria-hidden="true"><defs>'
        f'<linearGradient id="db-{uid}" x1="20%" y1="0%" x2="80%" y2="100%">'
        '<stop offset="0%" stop-color="#3A2408"/><stop offset="30%" stop-color="#6B3E10"/>'
        '<stop offset="55%" stop-color="#8C4E12"/><stop offset="75%" stop-color="#3F2609"/>'
        '<stop offset="100%" stop-color="#120B03"/></linearGradient>'
        f'<radialGradient id="dh-{uid}" cx="32%" cy="24%" r="35%">'
        '<stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.95"/>'
        '<stop offset="45%" stop-color="#FFE9B8" stop-opacity="0.35"/>'
        '<stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="dr-{uid}" cx="70%" cy="75%" r="45%">'
        '<stop offset="0%" stop-color="#C9852E" stop-opacity="0.55"/>'
        '<stop offset="100%" stop-color="#C9852E" stop-opacity="0"/></radialGradient>'
        f'<radialGradient id="fs-{uid}" cx="50%" cy="50%" r="50%">'
        '<stop offset="0%" stop-color="#000000" stop-opacity="0.35"/>'
        '<stop offset="100%" stop-color="#000000" stop-opacity="0"/></radialGradient></defs>'
        f'{sh}<path d="{d}" fill="url(#db-{uid})"/><path d="{d}" fill="url(#dr-{uid})"/>'
        f'<ellipse cx="105" cy="210" rx="34" ry="58" fill="url(#dh-{uid})"/>'
        '<ellipse cx="150" cy="320" rx="10" ry="6" fill="#FFE9B8" opacity="0.25"/></svg>'
    )


def logo_html(uid="h"):
    return (f'<span class="logo-mark">{logo_mark(uid)}</span>'
            '<span class="logo-text"><span class="logo-name">Madeni Yağ<br>Dünyası</span>'
            '<span class="logo-tag">MOTOR VE ENDÜSTRİYEL YAĞLAR</span></span>')


WA_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>'


def wa_link(text):
    return f"https://wa.me/{SITE['whatsapp']}?text={quote(text)}"


def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def url_of(path):
    """dist içindeki dosya yolundan temiz URL üretir."""
    p = "/" + path
    if p.endswith("index.html"):
        p = p[: -len("index.html")]
    return p


def chat_widget():
    return f"""<div class="wchat" data-chat>
  <div class="wchat-teaser" data-chat-teaser hidden>
    <button type="button" class="wchat-teaser-x" data-chat-teaser-close aria-label="Kapat">×</button>
    <b>Petromia Madeni Yağ</b>
    <span data-chat-teaser-text>Merhaba 👋 Size nasıl yardımcı olabiliriz?</span>
  </div>
  <section class="wchat-panel" data-chat-panel hidden role="dialog" aria-label="WhatsApp ile mesaj gönderin">
    <header class="wchat-head">
      <span class="wchat-avatar">{logo_mark("c", shadow=False)}</span>
      <span class="wchat-who"><b>Petromia Madeni Yağ</b><small><i class="wchat-online"></i> Çevrimiçi · genellikle birkaç dakikada yanıt verir</small></span>
      <button type="button" class="wchat-x" data-chat-close aria-label="Sohbeti kapat">×</button>
    </header>
    <div class="wchat-body">
      <div class="wchat-bubble">Merhaba 👋<br>Size nasıl yardımcı olabiliriz? Aşağıdan bir konu seçin veya mesajınızı yazın.<span class="wchat-time" data-chat-time></span></div>
      <div class="wchat-options" data-chat-options></div>
    </div>
    <form class="wchat-foot" data-chat-form>
      <textarea rows="1" data-chat-input placeholder="Mesajınızı yazın…" aria-label="Mesajınız"></textarea>
      <button type="submit" class="wchat-send" aria-label="WhatsApp ile gönder"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M2 21 23 12 2 3v7l15 2-15 2z"/></svg></button>
    </form>
  </section>
  <button type="button" class="wchat-fab" data-chat-toggle aria-expanded="false" aria-label="WhatsApp ile yazın">{WA_SVG}<span class="wchat-badge" data-chat-badge hidden>1</span></button>
</div>"""


def layout(path, title, description, body, schema=None, active="", chat_topic="", chat_city=""):
    url = SITE["domain"] + url_of(path)
    PAGES.append(url_of(path))
    schemas = [{
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": SITE["domain"] + "/#organization",
        "name": SITE["name"],
        "legalName": SITE["company"],
        "url": SITE["domain"] + "/",
        "logo": {"@type": "ImageObject", "url": SITE["domain"] + "/logo.png", "width": 1320, "height": 760},
        "telephone": SITE["phone_tel"],
    }, {
        "@context": "https://schema.org",
        "@type": "Store",
        "name": SITE["name"],
        "legalName": SITE["company"],
        "brand": [{"@type": "Brand", "name": b} for b in BRANDS],
        "url": SITE["domain"] + "/",
        "telephone": SITE["phone_tel"],
        "priceRange": "₺₺",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "1229 Sokak No:7 Ostim OSB",
            "addressLocality": "Yenimahalle",
            "addressRegion": "Ankara",
            "addressCountry": "TR",
        },
        "areaServed": {"@type": "Country", "name": "Türkiye"},
        "openingHours": "Mo-Sa 08:30-19:00",
    }]
    if schema:
        schemas.extend(schema if isinstance(schema, list) else [schema])
    schema_html = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>'
        for s in schemas)

    def nav(href, label, key):
        cls = ' class="active"' if key == active else ""
        return f'<a href="{href}"{cls}>{label}</a>'

    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#11161d">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:image" content="{SITE['domain']}/logo.png">
<link rel="stylesheet" href="/style.css?v={CSS_V}">
{schema_html}
</head>
<body data-chat-topic="{escape(chat_topic)}" data-chat-city="{escape(chat_city)}">
<div class="topbar">
  <div class="wrap topbar-in">
    <span>📍 Ostim / Ankara çıkışlı · 81 ile sevkiyat</span>
    <span class="topbar-links">
      <a href="tel:{SITE['phone_tel']}">📞 {SITE['phone']}</a>
      <a href="{wa_link('Merhaba, toptan madeni yağ / yedek parça için bilgi almak istiyorum.')}" target="_blank" rel="noopener">💬 WhatsApp</a>
    </span>
  </div>
</div>
<header class="header">
  <div class="wrap header-in">
    <a class="logo" href="/" aria-label="{SITE['name']} ana sayfa">{logo_html()}</a>
    <button class="menu-btn" aria-label="Menüyü aç" aria-expanded="false" data-menu>☰</button>
    <nav class="nav" data-nav>
      {nav('/', 'Ana Sayfa', 'home')}
      {nav('/urunler/', 'Ürünler', 'urunler')}
      {nav('/iller/', 'Sevkiyat İlleri', 'iller')}
      {nav('/iletisim/', 'İletişim', 'iletisim')}
      <a class="nav-cart" href="/teklif/">🛒 Teklif Sepeti <span class="cart-count" data-cart-count>0</span></a>
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="footer">
  <div class="wrap footer-grid">
    <div>
      <div class="logo logo-footer">{logo_html("f")}</div>
      <p>İnşaat, yol, hafriyat firmaları ve şantiyeler için toptan hidrolik yağ, dişli yağı, iş makinesi yedek parça ve filtre tedariki. Ankara Ostim deposundan Türkiye'nin 81 iline sevkiyat.</p>
      <p><b>{SITE['company']}</b></p>
    </div>
    <div>
      <h4>Ürün Grupları</h4>
      {''.join(f'<a href="/urunler/{c["slug"]}/">{c["name"]}</a>' for c in CATEGORIES)}
    </div>
    <div>
      <h4>Yakın İller</h4>
      {''.join(f'<a href="/iller/{p["slug"]}/">{p["name"]}</a>' for p in PROVINCES_BY_KM[1:9])}
      <a href="/iller/"><b>Tüm iller →</b></a>
    </div>
    <div>
      <h4>İletişim</h4>
      <p>📍 {SITE['address']}</p>
      <p>📞 <a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></p>
      <p>🕗 {SITE['hours']}</p>
      <a href="{SITE['maps']}" target="_blank" rel="noopener">Yol tarifi al →</a>
    </div>
  </div>
  <div class="wrap footer-bottom">© {date.today().year} {SITE['name']} · {SITE['company']} · Tüm hakları saklıdır. Fiyatlar için güncel teklif alınız.</div>
</footer>
{chat_widget()}
<div class="toast" data-toast role="status" aria-live="polite"></div>
<script src="/app.js?v={JS_V}" defer></script>
</body>
</html>
"""


def breadcrumbs(items):
    parts = []
    schema_items = []
    for i, (label, href) in enumerate(items, 1):
        if href:
            parts.append(f'<a href="{href}">{escape(label)}</a>')
        else:
            parts.append(f'<span>{escape(label)}</span>')
        schema_items.append({"@type": "ListItem", "position": i, "name": label,
                             "item": SITE["domain"] + (href or "")})
    html = '<nav class="crumbs wrap" aria-label="Sayfa yolu">' + ' <i>/</i> '.join(parts) + '</nav>'
    return html, {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": schema_items}


def product_card(item, cat):
    packs = "".join(f'<option>{escape(p)}</option>' for p in item["pack"])
    data = escape(json.dumps({"name": item["name"], "cat": cat["short"]}, ensure_ascii=False))
    is_oil = item["brand_label"] == "Markalar"
    rows = []
    for b in item["brands"]:
        label = b if is_oil else f"{b} uyumlu"
        stock_msg = (f"Merhaba, {label} {item['name']} ürününün stok durumu hakkında bilgi almak istiyorum.")
        rows.append(
            f'<li class="brand-row"><span class="brand-name">{escape(label)}</span>'
            f'<a class="btn-stock" href="{wa_link(stock_msg)}" target="_blank" rel="noopener" '
            f'data-stock>{WA_SVG}<span>Stok için bilgilendir</span></a>'
            f'<button class="btn-add" type="button" data-add data-brand="{escape(label)}" '
            f'aria-label="{escape(label)} {escape(item["name"])} sepete ekle">+ Sepet</button></li>')
    return f"""<article class="product">
  <span class="tag">{escape(cat['short'])}</span>
  <h3>{escape(item['name'])}</h3>
  <p class="spec">{escape(item['spec'])}</p>
  <p>{escape(item['use'])}</p>
  <div class="product-form" data-product="{data}">
    <div class="product-opts">
      <label>Ambalaj<select data-pack>{packs}</select></label>
      <label>Adet<input type="number" min="1" value="1" inputmode="numeric" data-qty></label>
    </div>
    <p class="brand-label">{escape(item['brand_label'])}</p>
    <ul class="brand-list">{''.join(rows)}</ul>
  </div>
</article>"""


def category_cards(prefix_text=""):
    out = []
    for c in CATEGORIES:
        out.append(f"""<a class="cat" href="/urunler/{c['slug']}/">
  <span class="cat-icon">{ICONS[c['icon']]}</span>
  <h3>{escape(c['name'])}{escape(prefix_text)}</h3>
  <p>{escape(c['desc'])}</p>
  <span class="more">Ürünleri gör →</span>
</a>""")
    return '<div class="cats">' + "".join(out) + "</div>"


def province_chip(p):
    return (f'<a class="chip chip-{p["tier"]["key"]}" href="/iller/{p["slug"]}/">'
            f'<b>{p["plate"]:02d}</b> {escape(p["name"])}'
            f'<small>{escape(p["zone"])} · {p["tier"]["eta"]}</small></a>')


def sectors_html():
    return '<div class="sectors">' + "".join(
        f'<div class="sector"><h3>{escape(t)}</h3><p>{escape(d)}</p></div>' for t, d in SECTORS) + '</div>'


def faq_html(qas):
    html = '<div class="faq">' + "".join(
        f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q, a in qas) + '</div>'
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}
    return html, schema


def cta(title, text, wa_text):
    return f"""<section class="cta">
  <div class="wrap cta-in">
    <div><h2>{escape(title)}</h2><p>{escape(text)}</p></div>
    <div class="cta-btns">
      <a class="btn btn-wa" href="{wa_link(wa_text)}" target="_blank" rel="noopener">{WA_SVG} WhatsApp'tan Teklif Al</a>
      <a class="btn btn-ghost" href="tel:{SITE['phone_tel']}">📞 {SITE['phone']}</a>
    </div>
  </div>
</section>"""


# ------------------------------------------------------------------ SAYFALAR

def build_home():
    near = [p for p in PROVINCES_BY_KM if 0 < p["km"] <= 300]
    faq, faq_schema = faq_html([
        ("Sadece Ankara'ya mı satış yapıyorsunuz?", "Hayır. Ankara Ostim deposundan Türkiye'nin 81 iline sevkiyat yapıyoruz. Ankara'ya yakın illere ertesi iş günü, diğer illere 1–3 iş günü içinde, en uzak illere bile en geç 2–3 iş günü içinde teslimat hedefliyoruz."),
        ("Sipariş nasıl verilir?", "Ürünleri teklif sepetine ekleyip WhatsApp üzerinden gönderebilir veya bizi arayabilirsiniz. Size il, miktar ve ambalaja göre güncel fiyat ve sevkiyat teklifi iletiyoruz."),
        ("Minimum sipariş miktarı var mı?", "Toptan odaklı çalışıyoruz; teneke, bidon, varil ve IBC bazında satış yapıyoruz. Küçük miktarlı acil ihtiyaçlarınız için de bizi arayabilirsiniz."),
        ("Sevkiyat hangi yöntemle yapılıyor?", "İlinize ve sipariş hacmine göre anlaşmalı kargo, şehirlerarası ambar, parsiyel ya da komple nakliye ile gönderim yapıyoruz. Yakın illerde kendi aracımızla teslimat da planlanabilir."),
        ("Kamu ihalesi yapan firmalara faturalı satış var mı?", "Evet. Tüm satışlar faturalıdır. Kamu projelerinde çalışan taşeron firmalar için düzenli tedarik ve toplu sipariş planı oluşturuyoruz."),
        ("İş makinesi parçası için neyi bilmem gerekiyor?", "Makine marka-modeli ve mümkünse parça numarası yeterli. Parçanın fotoğrafını WhatsApp'tan göndermeniz de doğru ürünü bulmamızı hızlandırır."),
    ])
    body = f"""
<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-text">
      <span class="eyebrow">Ankara çıkışlı · Türkiye geneli toptan tedarik</span>
      <h1>Şantiyeniz durmasın.<br><em>Yağ ve yedek parça</em> kapınıza gelsin.</h1>
      <p class="lead">İnşaat, yol yapım, hafriyat firmaları ve kamu projelerinde çalışan taşeronlar için <b>hidrolik yağ, dişli yağı, iş makinesi yedek parçası ve filtre</b> tedariki. Ostim deposundan anlaşmalı kargo, ambar ve nakliye ağıyla 81 ile sevkiyat.</p>
      <div class="hero-btns">
        <a class="btn" href="/urunler/">Ürünleri İncele</a>
        <a class="btn btn-wa" href="{wa_link('Merhaba, şantiyemiz için toptan teklif almak istiyoruz.')}" target="_blank" rel="noopener">{WA_SVG} Hızlı Teklif</a>
      </div>
      <ul class="hero-points">
        <li>✔ Varil, IBC ve teneke bazında toptan</li>
        <li>✔ Yakın illere ertesi gün sevkiyat</li>
        <li>✔ Yağ + filtre + parça tek sevkiyatta</li>
      </ul>
    </div>
    <form class="finder card" data-finder>
      <h2>İlinize sevkiyat süresini görün</h2>
      <label>Şantiyenizin bulunduğu il
        <select data-province-select required>
          <option value="">— İl seçiniz —</option>
          {''.join(f'<option value="{p["slug"]}">{p["plate"]:02d} · {escape(p["name"])}</option>' for p in sorted(PROVINCES, key=lambda x: x["plate"]))}
        </select>
      </label>
      <div class="finder-result" data-finder-result hidden></div>
      <button class="btn btn-block" type="submit">İl Sayfasına Git →</button>
      <p class="muted">Her il için sevkiyat yöntemi, tahmini süre ve ürün listesi ayrı sayfada.</p>
    </form>
  </div>
</section>

<section class="stats wrap">
  <div><b>81</b><span>İle sevkiyat</span></div>
  <div><b>4</b><span>Ana ürün grubu</span></div>
  <div><b>{len(near)}</b><span>İlde ertesi gün sevkiyat</span></div>
  <div><b>2–3 gün</b><span>En uzak ile teslim</span></div>
</section>

<section class="section wrap">
  <div class="section-head"><span class="eyebrow">Ürün grupları</span><h2>Makine parkınızın ihtiyacı tek yerden</h2></div>
  {category_cards()}
</section>

<section class="brands-strip wrap" aria-label="Satışını yaptığımız markalar">
  <span>Satışını yaptığımız markalar</span>
  <ul>{''.join(f'<li>{escape(b)}</li>' for b in BRANDS)}</ul>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Nasıl çalışıyoruz?</span><h2>Siparişten şantiyeye 4 adım</h2></div>
    <ol class="steps">
      <li><b>Teklif isteyin</b><span>Sepete ekleyin veya WhatsApp'tan ürün, miktar ve il bilgisini iletin.</span></li>
      <li><b>Fiyat + nakliye teklifi</b><span>İlinize en uygun kargo, ambar veya nakliye seçeneğiyle toplam teklifi iletiyoruz.</span></li>
      <li><b>Ostim'de hazırlık</b><span>Onay sonrası ürünler Ankara depomuzda paketlenir, faturası kesilir.</span></li>
      <li><b>Sevkiyat ve takip</b><span>Ürün yola çıkar; takip numarası veya araç bilgisi size iletilir.</span></li>
    </ol>
  </div>
</section>

<section class="section wrap">
  <div class="section-head"><span class="eyebrow">Öncelikli sevkiyat bölgesi</span><h2>Ankara'ya yakın illere ertesi gün sevkiyat</h2>
  <p>Ankara'ya yaklaşık 300 km mesafedeki illere siparişler ertesi iş günü yola çıkar. <a href="/iller/">Tüm illeri gör →</a></p></div>
  <div class="chips">{''.join(province_chip(p) for p in near)}</div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Kimlere hizmet veriyoruz?</span><h2>Sahada çalışan firmaların tedarikçisi</h2></div>
    {sectors_html()}
  </div>
</section>

<section class="section wrap narrow">
  <div class="section-head"><span class="eyebrow">Sık sorulanlar</span><h2>Merak edilenler</h2></div>
  {faq}
</section>
{cta('Toplu siparişiniz mi var?', 'Makine listenizi gönderin, yıllık yağ ve filtre ihtiyacınızı birlikte planlayalım.', 'Merhaba, makine parkımız için toplu yağ ve filtre teklifi almak istiyoruz.')}
"""
    write("index.html", layout(
        "index.html",
        "Toptan Madeni Yağ, Hidrolik Yağ ve İş Makinesi Parçası | Madeni Yağ Dünyası",
        "İnşaat, yol ve hafriyat firmaları için toptan hidrolik yağ, dişli yağı, iş makinesi yedek parça ve filtre. Ankara Ostim'den 81 ile hızlı sevkiyat. WhatsApp'tan teklif alın.",
        body, schema=faq_schema, active="home"))


def build_products():
    crumbs, crumb_schema = breadcrumbs([("Ana Sayfa", "/"), ("Ürünler", None)])
    body = f"""{crumbs}
<section class="page-head wrap">
  <h1>Toptan Ürün Gruplarımız</h1>
  <p class="lead">Şantiye ve iş makinesi odaklı dört ana ürün grubunda, teneke adetten IBC tanka kadar toptan tedarik. Ürünleri sepete ekleyin, WhatsApp'tan tek mesajla teklif alın.</p>
</section>
<section class="section wrap">{category_cards()}</section>
"""
    for c in CATEGORIES:
        body += f"""<section class="section wrap" id="{c['slug']}">
  <div class="section-head row"><h2>{escape(c['name'])}</h2><a href="/urunler/{c['slug']}/">Detaylı sayfa →</a></div>
  <div class="products">{''.join(product_card(i, c) for i in c['items'])}</div>
</section>"""
    body += cta("Aradığınız ürünü bulamadınız mı?", "Listede olmayan viskozite, marka veya parça için bize yazın.", "Merhaba, listede olmayan bir ürün için bilgi almak istiyorum: ")
    write("urunler/index.html", layout(
        "urunler/index.html",
        "Ürünler: Hidrolik Yağ, Dişli Yağı, Yedek Parça, Filtre | Madeni Yağ Dünyası",
        "Hidrolik yağ (HM 32/46/68), dişli yağı (80W-90, 85W-140, EP 220), TO-4 şanzıman yağı, kova dişi, pim-burç, hidrolik hortum ve iş makinesi filtreleri toptan.",
        body, schema=crumb_schema, active="urunler", chat_topic="ürünleriniz"))

    for c in CATEGORIES:
        crumbs, crumb_schema = breadcrumbs([("Ana Sayfa", "/"), ("Ürünler", "/urunler/"), (c["name"], None)])
        item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": c["name"],
                     "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": it["name"]}
                                         for i, it in enumerate(c["items"])]}
        others = "".join(f'<a class="chip" href="/urunler/{o["slug"]}/">{escape(o["name"])}</a>'
                         for o in CATEGORIES if o is not c)
        body = f"""{crumbs}
<section class="page-head wrap">
  <span class="cat-icon big">{ICONS[c['icon']]}</span>
  <h1>Toptan {escape(c['name'])}</h1>
  <p class="lead">{escape(c['intro'])}</p>
</section>
<section class="section wrap">
  <div class="products">{''.join(product_card(i, c) for i in c['items'])}</div>
</section>
<section class="section wrap">
  <div class="section-head"><h2>{escape(c['name'])} hangi illere gönderiliyor?</h2>
  <p>Ankara Ostim deposundan tüm Türkiye'ye gönderim yapıyoruz. Öncelikli bölgemizdeki iller:</p></div>
  <div class="chips">{''.join(province_chip(p) for p in PROVINCES_BY_KM[1:19])}</div>
  <p><a href="/iller/">81 ilin tamamını gör →</a></p>
</section>
<section class="section wrap"><h2>Diğer ürün grupları</h2><div class="chips">{others}</div></section>
{cta(c['name'] + ' için teklif alın', 'Ürün, ambalaj, miktar ve il bilgisini iletin; aynı gün fiyat verelim.', 'Merhaba, ' + c['name'] + ' için toptan teklif almak istiyorum.')}
"""
        write(f"urunler/{c['slug']}/index.html", layout(
            f"urunler/{c['slug']}/index.html",
            f"Toptan {c['name']} | Ankara'dan 81 İle Sevkiyat | Madeni Yağ Dünyası",
            c["desc"] + " Ankara Ostim'den Türkiye geneline toptan satış.",
            body, schema=[crumb_schema, item_list], active="urunler", chat_topic=c["name"]))


def dative(name):
    """Türkçe yönelme hâli: Konya'ya, Bolu'ya, Sivas'a, İzmir'e."""
    vowels = [ch for ch in name.lower() if ch in "aıoueiöü"]
    back = vowels[-1] in "aıou" if vowels else True
    suffix = "a" if back else "e"
    if name[-1].lower() in "aıoueiöü":
        suffix = "y" + suffix
    return f"{name}'{suffix}"


def nearest(p, n=6):
    others = [o for o in PROVINCES if o is not p and o["km"] > 0]
    same = sorted([o for o in others if o["region"] == p["region"]], key=lambda o: abs(o["km"] - p["km"]))
    rest = sorted([o for o in others if o["region"] != p["region"]], key=lambda o: abs(o["km"] - p["km"]))
    return (same + rest)[:n]


def build_provinces():
    zone_list = sorted(ZONES.items(),
                       key=lambda z: sum(p["km"] for p in PROVINCES if p["zone"] == z[0]) / len(z[1]))
    crumbs, crumb_schema = breadcrumbs([("Ana Sayfa", "/"), ("Sevkiyat İlleri", None)])
    legend = "".join(
        f'<span class="legend legend-{k}">{escape(t)}</span>' for k, t in
        [("merkez", "Aynı gün"), ("yakin", "Ertesi iş günü"), ("orta", "1–2 iş günü"), ("uzak", "2–3 iş günü")])
    body = f"""{crumbs}
<section class="page-head wrap">
  <h1>81 İle Toptan Madeni Yağ ve Yedek Parça Sevkiyatı</h1>
  <p class="lead">Tüm siparişler Ankara Ostim deposundan çıkar. Ankara'ya yakın illere ertesi iş günü, en uzak illere en geç 2–3 iş günü içinde teslimat hedefliyoruz. İller sevkiyat bölgelerine göre, Ankara'ya yakınlık sırasıyla listelenmiştir.</p>
  <div class="legends">{legend}</div>
  <input class="search" type="search" placeholder="İl ara… (ör. Karabük)" data-filter aria-label="İl ara">
</section>
"""
    for zone, _ in zone_list:
        items = sorted([p for p in PROVINCES if p["zone"] == zone], key=lambda p: p["km"])
        body += (f'<section class="section section-tight wrap" data-group><h2>{escape(zone)} <small class="count">{len(items)} il</small></h2>'
                 f'<div class="chips">{"".join(province_chip(p) for p in items)}</div></section>')
    body += cta("İlinizi listede göremediniz mi?", "Tüm Türkiye'ye gönderim yapıyoruz; ilçe ve şantiye adresi için bize yazın.", "Merhaba, şantiyemize sevkiyat için bilgi almak istiyorum. İl/ilçe: ")
    write("iller/index.html", layout(
        "iller/index.html",
        "Sevkiyat Yapılan İller | 81 İle Toptan Madeni Yağ | Madeni Yağ Dünyası",
        "Ankara Ostim'den 81 ile toptan hidrolik yağ, dişli yağı, iş makinesi yedek parça ve filtre sevkiyatı. Yakın illere ertesi gün, en uzak illere 2–3 iş günü.",
        body, schema=crumb_schema, active="iller"))

    for p in PROVINCES:
        build_province(p)


def shipping_methods(p):
    k = p["tier"]["key"]
    if k == "merkez":
        return [
            ("Kendi aracımızla teslimat", "Ankara içi şantiye ve depolara aynı gün teslimat planlanır."),
            ("Depodan teslim", "Ostim deposundan ürünlerinizi kendi aracınızla teslim alabilirsiniz."),
            ("Komple araç", "Toplu varil ve IBC siparişlerinde tek seferde komple sevkiyat."),
        ]
    if k == "yakin":
        return [
            ("Şehirlerarası ambar", f"Ankara – {p['name']} hattında çalışan ambarlarla ertesi iş günü teslim."),
            ("Anlaşmalı kargo", "Teneke, bidon ve parça gönderimlerinde kapıya teslim."),
            ("Parsiyel / komple nakliye", "Varil ve IBC siparişlerinde şantiyeye doğrudan araç. Uygun hacimlerde kendi aracımızla teslimat planlanabilir."),
        ]
    if k == "orta":
        return [
            ("Şehirlerarası ambar", f"{p['name']} ambar hattıyla ekonomik ve hızlı toplu gönderim, 1–2 iş günü."),
            ("Anlaşmalı kargo", "Küçük ve orta hacimli siparişlerde 1–2 iş günü içinde kapıya teslim."),
            ("Parsiyel / komple nakliye", "Yüksek hacimli siparişlerde doğrudan şantiye adresine sevkiyat."),
        ]
    return [
        ("Anlaşmalı kargo", "Filtre, parça ve teneke ürünlerde 2–3 iş günü içinde kapıya teslim."),
        ("Şehirlerarası ambar", f"Varil siparişlerinde {p['name']} ambarına teslim; en ekonomik seçenek."),
        ("Parsiyel / komple nakliye", "Birden fazla varil veya IBC içeren siparişlerde doğrudan araçla 2–3 iş günü."),
    ]


def dative(name):
    """Türkçe yönelme hâli: Konya'ya, Bolu'ya, Sivas'a, İzmir'e."""
    vowels = [ch for ch in name.lower() if ch in "aıoueiöü"]
    back = vowels[-1] in "aıou" if vowels else True
    suffix = "a" if back else "e"
    if name[-1].lower() in "aıoueiöü":
        suffix = "y" + suffix
    return f"{name}'{suffix}"


def nearest(p, n=6):
    others = [o for o in PROVINCES if o is not p and o["km"] > 0]
    same = sorted([o for o in others if o["zone"] == p["zone"]], key=lambda o: abs(o["km"] - p["km"]))
    rest = sorted([o for o in others if o["zone"] != p["zone"]], key=lambda o: abs(o["km"] - p["km"]))
    return (same + rest)[:n]


def build_province(p):
    name = p["name"]
    t = p["tier"]
    is_center = p["km"] == 0
    loc = "Ankara merkez depomuzdan" if is_center else f"Ankara'dan yaklaşık {p['km']} km"
    note = REGION_NOTES[p["region"]]
    methods = "".join(f'<li><b>{escape(a)}</b><span>{escape(b)}</span></li>' for a, b in shipping_methods(p))
    near = nearest(p)
    faq, faq_schema = faq_html([(q.replace("{il}", name), a.replace("{il}", name)) for q, a in OIL_FAQ])
    crumbs, crumb_schema = breadcrumbs([("Ana Sayfa", "/"), ("Sevkiyat İlleri", "/iller/"), (name, None)])
    wa_text = f"Merhaba, {name} ilindeki şantiyemiz için toptan teklif almak istiyoruz."
    ship_title = ("Ankara içinde nasıl teslim ediyoruz?" if is_center
                  else f"Ankara'dan {dative(name)} nasıl gönderiyoruz?")
    service = {
        "@context": "https://schema.org", "@type": "Service",
        "name": f"{name} Toptan Madeni Yağ ve İş Makinesi Yedek Parça Tedariki",
        "provider": {"@type": "Store", "name": SITE["name"], "telephone": SITE["phone_tel"]},
        "areaServed": {"@type": "AdministrativeArea", "name": name},
        "serviceType": "Toptan madeni yağ, hidrolik yağ, dişli yağı, iş makinesi yedek parça ve filtre satışı",
    }
    body = f"""{crumbs}
<section class="hero hero-il">
  <div class="wrap hero-in">
    <div class="hero-text">
      <span class="eyebrow">{p['plate']:02d} · {escape(name)} · {escape(p['zone'])}</span>
      <h1>{escape(name)} Toptan Madeni Yağ ve <em>İş Makinesi Yedek Parça</em></h1>
      <p class="lead">{escape(name)} ve ilçelerindeki inşaat, yol yapım ve hafriyat firmalarına; {escape(note)} için <b>hidrolik yağ, dişli yağı, iş makinesi yedek parçası ve filtre</b> sevkiyatı yapıyoruz. Siparişleriniz {escape(loc)} {'' if is_center else 'mesafedeki '}Ostim deposundan {'aynı gün' if is_center else 'kargo, ambar ve nakliye ile'} şantiyenize ulaşır.</p>
      <div class="hero-btns">
        <a class="btn btn-wa" href="{wa_link(wa_text)}" target="_blank" rel="noopener">{WA_SVG} {escape(name)} için Teklif Al</a>
        <a class="btn btn-ghost" href="tel:{SITE['phone_tel']}">📞 Hemen Ara</a>
      </div>
    </div>
    <div class="card il-card" data-set-province="{escape(name)}">
      <span class="badge badge-{t['key']}">{escape(t['badge'])}</span>
      <dl>
        <div><dt>Çıkış noktası</dt><dd>Ostim / Ankara</dd></div>
        <div><dt>Mesafe</dt><dd>{'Merkez' if is_center else '≈ ' + str(p['km']) + ' km'}</dd></div>
        <div><dt>Tahmini teslim</dt><dd>{escape(t['eta'])}</dd></div>
        <div><dt>Sevkiyat bölgesi</dt><dd>{escape(p['zone'])}</dd></div>
      </dl>
      <p class="muted">Mesafe ve süreler yaklaşık değerlerdir; kesin bilgi teklifle birlikte verilir.</p>
    </div>
  </div>
</section>

<section class="section wrap">
  <div class="about-il">
    <div class="about-plate"><small>Plaka</small><b>{p['plate']:02d}</b></div>
    <div>
      <span class="eyebrow">{escape(name)} hakkında</span>
      <h2>Kısaca {escape(name)}</h2>
      <p>{escape(p['info'])}</p>
      <ul class="about-facts">
        <li><b>Coğrafi bölge</b>{escape(p['region'])}</li>
        <li><b>Sevkiyat bölgesi</b>{escape(p['zone'])}</li>
        <li><b>Ankara'ya uzaklık</b>{'Merkez' if is_center else '≈ ' + str(p['km']) + ' km'}</li>
        <li><b>Teslim süresi</b>{escape(t['eta'])}</li>
      </ul>
    </div>
  </div>
</section>

<section class="section wrap">
  <div class="section-head"><span class="eyebrow">{escape(name)} için ürün grupları</span><h2>{escape(name)} şantiyelerine gönderdiğimiz ürünler</h2></div>
  {category_cards()}
</section>

<section class="section alt">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">Sevkiyat</span>
      <h2>{escape(ship_title)}</h2>
      <ul class="methods">{methods}</ul>
    </div>
    <div class="card">
      <h3>{escape(name)} hızlı teklif formu</h3>
      <form data-quick-form>
        <input type="hidden" name="il" value="{escape(name)}">
        <label>Firma adı<input name="firma" required autocomplete="organization"></label>
        <label>İlçe / Şantiye<input name="ilce" placeholder="ör. merkez, OSB, şantiye adı"></label>
        <label>İhtiyacınız<textarea name="not" rows="3" required placeholder="ör. 4 varil Shell HM 46 hidrolik yağ, 10 adet yakıt filtresi"></textarea></label>
        <button class="btn btn-wa btn-block" type="submit">{WA_SVG} WhatsApp ile Gönder</button>
      </form>
    </div>
  </div>
</section>

<section class="section wrap narrow">
  <div class="section-head"><span class="eyebrow">Sık sorulan sorular</span><h2>Madeni yağ hakkında merak edilenler</h2></div>
  {faq}
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">Hedef sektörler</span><h2>{escape(name)} için kimlere tedarik sağlıyoruz?</h2></div>
    {sectors_html()}
  </div>
</section>

<section class="section wrap">
  <h2>{escape(p['zone'])} ve yakın mesafedeki iller</h2>
  <div class="chips">{''.join(province_chip(o) for o in near)}</div>
  <p><a href="/iller/">Tüm illeri gör →</a></p>
</section>
{cta(name + ' şantiyeniz için teklif alın', 'Ürün, marka, miktar ve ilçe bilgisini gönderin; ürün + nakliye dahil toplam teklif iletelim.', wa_text)}
"""
    title = f"{name} Toptan Madeni Yağ, Hidrolik Yağ, İş Makinesi Parçası | {t['badge']}"
    desc = (f"{name} ({p['zone']}) inşaat, yol ve hafriyat firmalarına toptan hidrolik yağ, dişli yağı, iş makinesi yedek parça ve filtre. "
            f"Ankara Ostim'den {t['eta'].lower()} teslimat. WhatsApp'tan teklif alın.")
    write(f"iller/{p['slug']}/index.html", layout(
        f"iller/{p['slug']}/index.html", title, desc, body,
        schema=[crumb_schema, faq_schema, service], active="iller", chat_city=name))


def build_cart():
    crumbs, crumb_schema = breadcrumbs([("Ana Sayfa", "/"), ("Teklif Sepeti", None)])
    options = "".join(f'<option>{escape(p["name"])}</option>' for p in sorted(PROVINCES, key=lambda x: x["plate"]))
    body = f"""{crumbs}
<section class="page-head wrap"><h1>Teklif Sepeti</h1>
<p class="lead">Sepetinizdeki ürünleri firma ve il bilgisiyle birlikte WhatsApp'tan gönderin. Ürün ve nakliye dahil güncel fiyat teklifini size iletelim.</p></section>
<section class="section wrap two-col">
  <div class="card">
    <h2>Ürünler</h2>
    <div data-cart-list><p class="muted">Sepetiniz boş. <a href="/urunler/">Ürünlere göz atın →</a></p></div>
  </div>
  <div class="card">
    <h2>Teslimat bilgileri</h2>
    <form data-cart-form>
      <label>Firma adı<input name="firma" required autocomplete="organization"></label>
      <label>Yetkili adı<input name="yetkili" autocomplete="name"></label>
      <label>Teslimat ili<select name="il" required data-cart-province><option value="">— İl seçiniz —</option>{options}</select></label>
      <label>İlçe / Şantiye adresi<input name="ilce"></label>
      <label>Not<textarea name="not" rows="3" placeholder="Ek ürün, marka tercihi, makine modeli…"></textarea></label>
      <button class="btn btn-wa btn-block" type="submit">{WA_SVG} Teklifi WhatsApp'tan Gönder</button>
      <button class="btn btn-ghost btn-block" type="button" data-cart-clear>Sepeti Temizle</button>
    </form>
  </div>
</section>
"""
    write("teklif/index.html", layout(
        "teklif/index.html", "Teklif Sepeti | Madeni Yağ Dünyası",
        "Toptan madeni yağ ve iş makinesi yedek parça teklif sepeti. WhatsApp ile hızlı fiyat teklifi alın.",
        body, schema=crumb_schema))


def build_contact():
    crumbs, crumb_schema = breadcrumbs([("Ana Sayfa", "/"), ("İletişim", None)])
    options = "".join(f'<option>{escape(p["name"])}</option>' for p in sorted(PROVINCES, key=lambda x: x["plate"]))
    body = f"""{crumbs}
<section class="page-head wrap"><h1>İletişim</h1>
<p class="lead">Toptan sipariş, fiyat teklifi ve sevkiyat planı için bize ulaşın. En hızlı dönüş WhatsApp üzerinden sağlanır.</p></section>
<section class="section wrap two-col">
  <div class="card contact-list">
    <h2>{SITE['company']}</h2>
    <p>📍 <b>Adres</b><br>{SITE['address']}</p>
    <p>📞 <b>Telefon</b><br><a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></p>
    <p>💬 <b>WhatsApp</b><br><a href="{wa_link('Merhaba, bilgi almak istiyorum.')}" target="_blank" rel="noopener">{SITE['phone']}</a></p>
    <p>🕗 <b>Çalışma saatleri</b><br>{SITE['hours']}</p>
    <a class="btn" href="{SITE['maps']}" target="_blank" rel="noopener">📍 Yol Tarifi Al</a>
  </div>
  <div class="card">
    <h2>Mesaj gönderin</h2>
    <form data-quick-form>
      <label>Firma adı<input name="firma" required autocomplete="organization"></label>
      <label>İl<select name="il" required><option value="">— İl seçiniz —</option>{options}</select></label>
      <label>İlçe / Şantiye<input name="ilce"></label>
      <label>Mesajınız<textarea name="not" rows="4" required></textarea></label>
      <button class="btn btn-wa btn-block" type="submit">{WA_SVG} WhatsApp ile Gönder</button>
    </form>
  </div>
</section>
"""
    write("iletisim/index.html", layout(
        "iletisim/index.html", "İletişim | Madeni Yağ Dünyası – Ostim / Ankara",
        f"Madeni Yağ Dünyası iletişim: {SITE['address']}. Telefon ve WhatsApp: {SITE['phone']}.",
        body, schema=crumb_schema, active="iletisim"))


def build_404():
    body = """<section class="page-head wrap narrow center"><h1>Sayfa bulunamadı</h1>
<p class="lead">Aradığınız sayfa taşınmış veya kaldırılmış olabilir.</p>
<p><a class="btn" href="/">Ana sayfaya dön</a> <a class="btn btn-ghost" href="/iller/">İlinizi seçin</a></p></section>"""
    html = layout("404.html", "Sayfa Bulunamadı | Madeni Yağ Dünyası", "Sayfa bulunamadı.", body)
    PAGES.remove("/404.html")
    write("404.html", html.replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"'))


def build_meta():
    urls = []
    for path in PAGES:
        prio = "1.0" if path == "/" else ("0.8" if path.startswith("/iller/") else "0.7")
        urls.append(f"  <url><loc>{SITE['domain']}{path}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority></url>")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "\n".join(urls) + "\n</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE['domain']}/sitemap.xml\n")
    write("_headers", "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n\n"
          "/style.css\n  Cache-Control: public, max-age=86400\n/app.js\n  Cache-Control: public, max-age=86400\n")
    for f in ("style.css", "app.js", "favicon.svg", "logo.svg", "logo.png", "favicon.ico", "favicon-192.png", "apple-touch-icon.png"):
        src = os.path.join(ROOT, f)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(OUT, f))


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    build_home()
    build_products()
    build_provinces()
    build_cart()
    build_contact()
    build_404()
    build_meta()
    print(f"Tamam: {len(PAGES)} sayfa -> {OUT}")


if __name__ == "__main__":
    main()
