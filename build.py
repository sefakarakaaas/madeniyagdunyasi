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

from data import (CATEGORIES, PROVINCES, PROVINCES_BY_KM, REGION_NOTES,
                  SECTORS, SITE)

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "dist")
TODAY = date.today().isoformat()
PAGES = []  # sitemap için

ICONS = {
    "hydraulic": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 4c6 9 12 16 12 24a12 12 0 0 1-24 0c0-8 6-15 12-24z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M18 30a6 6 0 0 0 6 6" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>',
    "gear": '<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="7" fill="none" stroke="currentColor" stroke-width="3"/><path d="M24 4v7M24 37v7M4 24h7M37 24h7M9.9 9.9l5 5M33.1 33.1l5 5M9.9 38.1l5-5M33.1 14.9l5-5" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="24" cy="24" r="15" fill="none" stroke="currentColor" stroke-width="3"/></svg>',
    "bucket": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M6 14h30l6 10-8 14H12L6 24z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M14 38v5M22 38v5M30 38v5" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M20 14l4-9h12" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>',
    "filter": '<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="12" y="6" width="24" height="36" rx="5" fill="none" stroke="currentColor" stroke-width="3"/><path d="M12 14h24M12 34h24M18 14v20M24 14v20M30 14v20" stroke="currentColor" stroke-width="3"/></svg>',
    "truck": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M3 12h26v22H3zM29 20h9l7 8v6H29z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><circle cx="12" cy="36" r="4" fill="var(--bg,#fff)" stroke="currentColor" stroke-width="3"/><circle cx="37" cy="36" r="4" fill="var(--bg,#fff)" stroke="currentColor" stroke-width="3"/></svg>',
}

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


def layout(path, title, description, body, schema=None, active=""):
    url = SITE["domain"] + url_of(path)
    PAGES.append(url_of(path))
    schemas = [{
        "@context": "https://schema.org",
        "@type": "Store",
        "name": SITE["name"],
        "legalName": SITE["company"],
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
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">
{schema_html}
</head>
<body>
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
    <a class="logo" href="/" aria-label="{SITE['name']} ana sayfa">
      <span class="logo-mark">MY</span>
      <span class="logo-text"><b>Madeni Yağ</b> Dünyası<small>Toptan · İş Makinesi · Şantiye</small></span>
    </a>
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
      <div class="logo logo-footer"><span class="logo-mark">MY</span><span class="logo-text"><b>Madeni Yağ</b> Dünyası</span></div>
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
  <div class="wrap footer-bottom">© {date.today().year} {SITE['name']} · {SITE['company']}. Tüm hakları saklıdır. Fiyatlar için güncel teklif alınız.</div>
</footer>
<a class="wa-float" href="{wa_link('Merhaba, toptan sipariş için teklif almak istiyorum.')}" target="_blank" rel="noopener" aria-label="WhatsApp ile yazın">{WA_SVG}<span>Teklif Al</span></a>
<div class="toast" data-toast role="status" aria-live="polite"></div>
<script src="/app.js" defer></script>
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
    return f"""<article class="product">
  <span class="tag">{escape(cat['short'])}</span>
  <h3>{escape(item['name'])}</h3>
  <p class="spec">{escape(item['spec'])}</p>
  <p>{escape(item['use'])}</p>
  <div class="product-form" data-product="{data}">
    <label>Ambalaj<select data-pack>{packs}</select></label>
    <label>Adet<input type="number" min="1" value="1" inputmode="numeric" data-qty></label>
    <button class="btn btn-sm" type="button" data-add>+ Sepete Ekle</button>
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
            f'<small>{"Merkez" if p["km"] == 0 else "~" + str(p["km"]) + " km"} · {p["tier"]["eta"]}</small></a>')


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
        ("Sadece Ankara'ya mı satış yapıyorsunuz?", "Hayır. Ankara Ostim deposundan Türkiye'nin 81 iline sevkiyat yapıyoruz. Ankara'ya yakın illere ertesi iş günü, diğer illere 1–4 iş günü içinde teslimat hedefliyoruz."),
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
  <div><b>1000 L</b><span>IBC'ye kadar ambalaj</span></div>
</section>

<section class="section wrap">
  <div class="section-head"><span class="eyebrow">Ürün grupları</span><h2>Makine parkınızın ihtiyacı tek yerden</h2></div>
  {category_cards()}
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
        body, schema=crumb_schema, active="urunler"))

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
            body, schema=[crumb_schema, item_list], active="urunler"))


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
    groups = [
        ("Merkez depo", [p for p in PROVINCES_BY_KM if p["km"] == 0]),
        ("Öncelikli bölge · ertesi iş günü (≈300 km'ye kadar)", [p for p in PROVINCES_BY_KM if 0 < p["km"] <= 300]),
        ("Hızlı sevkiyat · 1–2 iş günü (≈300–600 km)", [p for p in PROVINCES_BY_KM if 300 < p["km"] <= 600]),
        ("Türkiye geneli · 2–4 iş günü (600 km üzeri)", [p for p in PROVINCES_BY_KM if p["km"] > 600]),
    ]
    crumbs, crumb_schema = breadcrumbs([("Ana Sayfa", "/"), ("Sevkiyat İlleri", None)])
    body = f"""{crumbs}
<section class="page-head wrap">
  <h1>81 İle Toptan Madeni Yağ ve Yedek Parça Sevkiyatı</h1>
  <p class="lead">Tüm siparişler Ankara Ostim deposundan çıkar. İlinizi seçerek sevkiyat yöntemini, tahmini teslim süresini ve o ile özel teklif formunu görebilirsiniz. İller Ankara'ya yakınlığa göre sıralanmıştır.</p>
  <input class="search" type="search" placeholder="İl ara… (ör. Konya)" data-filter aria-label="İl ara">
</section>
"""
    for title, items in groups:
        body += f'<section class="section wrap" data-group><h2>{escape(title)}</h2><div class="chips">{"".join(province_chip(p) for p in items)}</div></section>'
    body += cta("İlinizi listede göremediniz mi?", "Tüm Türkiye'ye gönderim yapıyoruz; ilçe ve şantiye adresi için bize yazın.", "Merhaba, şantiyemize sevkiyat için bilgi almak istiyorum. İl/ilçe: ")
    write("iller/index.html", layout(
        "iller/index.html",
        "Sevkiyat Yapılan İller | 81 İle Toptan Madeni Yağ | Madeni Yağ Dünyası",
        "Ankara Ostim'den 81 ile toptan hidrolik yağ, dişli yağı, iş makinesi yedek parça ve filtre sevkiyatı. İlinize özel teslim süresi ve sevkiyat yöntemi.",
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
            ("Şehirlerarası ambar", f"{p['name']} ambar hattıyla ekonomik ve hızlı toplu gönderim."),
            ("Anlaşmalı kargo", "Küçük ve orta hacimli siparişlerde 1–2 iş günü içinde teslim."),
            ("Parsiyel / komple nakliye", "Yüksek hacimli siparişlerde doğrudan şantiye adresine sevkiyat."),
        ]
    return [
        ("Anlaşmalı kargo", "Filtre, parça ve teneke ürünlerde kapıya teslim."),
        ("Şehirlerarası ambar", f"Varil siparişlerinde {p['name']} ambarına teslim; en ekonomik seçenek."),
        ("Parsiyel / komple nakliye", "Birden fazla varil veya IBC içeren siparişlerde doğrudan araç."),
    ]


def build_province(p):
    name = p["name"]
    t = p["tier"]
    is_center = p["km"] == 0
    loc = "Ankara merkez depomuzdan" if is_center else f"Ankara'dan yaklaşık {p['km']} km"
    note = REGION_NOTES[p["region"]]
    methods = "".join(f'<li><b>{escape(a)}</b><span>{escape(b)}</span></li>' for a, b in shipping_methods(p))
    near = nearest(p)
    faq, faq_schema = faq_html([
        (f"{name} iline sipariş ne kadar sürede ulaşır?",
         f"{name} için tahmini teslim süresi {t['eta'].lower()}dür. Süre; sipariş saatine, ilçeye ve seçilen sevkiyat yöntemine göre değişebilir, kesin süre teklif ile birlikte bildirilir."),
        (f"{name} şantiyeme varil veya IBC gönderebilir misiniz?",
         f"Evet. Varil ve IBC siparişleri {name} içindeki şantiye, depo veya ambar adresine parsiyel ya da komple nakliye ile gönderilir."),
        (f"{name} için nakliye ücreti nasıl hesaplanıyor?",
         "Nakliye ücreti ürün hacmi, ağırlığı ve seçilen yönteme (kargo, ambar, nakliye) göre hesaplanır ve teklifte ürün fiyatıyla birlikte ayrıca belirtilir."),
        (f"{name} ilçelerine de teslimat yapıyor musunuz?",
         f"Evet. {name} merkez ve ilçelerine teslimat yapıyoruz. Uzak ilçe ve şantiye noktaları için ambar teslim veya nakliye seçeneği sunulur."),
        ("Ödeme ve fatura nasıl oluyor?",
         "Tüm satışlar faturalıdır. Ödeme koşulları sipariş hacmine göre teklif aşamasında netleştirilir."),
    ])
    crumbs, crumb_schema = breadcrumbs([("Ana Sayfa", "/"), ("Sevkiyat İlleri", "/iller/"), (name, None)])
    ship_title = ("Ankara içinde nasıl teslim ediyoruz?" if is_center
                  else f"Ankara'dan {dative(name)} nasıl gönderiyoruz?")
    wa_text = f"Merhaba, {name} ilindeki şantiyemiz için toptan teklif almak istiyoruz."
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
      <span class="eyebrow">{p['plate']:02d} · {escape(name)} · {escape(p['region'])} Bölgesi</span>
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
        <div><dt>Sevkiyat sınıfı</dt><dd>{escape(t['label'])}</dd></div>
      </dl>
      <p class="muted">Mesafe ve süreler yaklaşık değerlerdir; kesin bilgi teklifle birlikte verilir.</p>
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
        <label>İhtiyacınız<textarea name="not" rows="3" required placeholder="ör. 4 varil HM 46 hidrolik yağ, 10 adet yakıt filtresi"></textarea></label>
        <button class="btn btn-wa btn-block" type="submit">{WA_SVG} WhatsApp ile Gönder</button>
      </form>
    </div>
  </div>
</section>

<section class="section wrap">
  <div class="section-head"><span class="eyebrow">Hedef sektörler</span><h2>{escape(name)} için kimlere tedarik sağlıyoruz?</h2></div>
  {sectors_html()}
</section>

<section class="section wrap narrow">
  <div class="section-head"><h2>{escape(name)} sevkiyatı hakkında sorular</h2></div>
  {faq}
</section>

<section class="section wrap">
  <h2>Yakın ve benzer mesafedeki iller</h2>
  <div class="chips">{''.join(province_chip(o) for o in near)}</div>
  <p><a href="/iller/">Tüm illeri gör →</a></p>
</section>
{cta(name + ' şantiyeniz için teklif alın', 'Ürün, miktar ve ilçe bilgisini gönderin; ürün + nakliye dahil toplam teklif iletelim.', wa_text)}
"""
    title = (f"{name} Toptan Madeni Yağ, Hidrolik Yağ, İş Makinesi Parçası | {t['badge']}")
    desc = (f"{name} inşaat, yol ve hafriyat firmalarına toptan hidrolik yağ, dişli yağı, iş makinesi yedek parça ve filtre. "
            f"Ankara Ostim'den {name} iline {t['eta'].lower()} teslimat. WhatsApp'tan teklif alın.")
    write(f"iller/{p['slug']}/index.html", layout(
        f"iller/{p['slug']}/index.html", title, desc, body,
        schema=[crumb_schema, faq_schema, service], active="iller"))


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
    for f in ("style.css", "app.js", "favicon.svg"):
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
