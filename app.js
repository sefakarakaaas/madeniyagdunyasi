/* Madeni Yağ Dünyası — teklif sepeti ve WhatsApp formları */
(function () {
  "use strict";
  var WA = "905015421422";
  var KEY = "myd_cart_v1";
  var PKEY = "myd_province";

  function store(k, v) {
    try {
      if (v === undefined) return JSON.parse(localStorage.getItem(k));
      localStorage.setItem(k, JSON.stringify(v));
    } catch (e) { return null; }
  }
  var cart = store(KEY) || [];
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return "&#" + c.charCodeAt(0) + ";"; }); }

  function toast(msg) {
    var t = $("[data-toast]"); if (!t) return;
    t.textContent = msg; t.classList.add("show");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("show"); }, 2200);
  }
  function openWA(text) {
    window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent(text), "_blank", "noopener");
  }
  function save() { store(KEY, cart); renderCount(); renderCart(); }
  function renderCount() {
    var n = cart.reduce(function (a, i) { return a + 1; }, 0);
    $$("[data-cart-count]").forEach(function (el) { el.textContent = n; });
  }

  // Mobil menü
  var mb = $("[data-menu]"), nav = $("[data-nav]");
  if (mb && nav) mb.addEventListener("click", function () {
    var o = nav.classList.toggle("open"); mb.setAttribute("aria-expanded", o);
  });

  // İl sayfasındaysak ili hatırla
  var sp = $("[data-set-province]");
  if (sp) store(PKEY, sp.getAttribute("data-set-province"));

  // Sepete ekle
  $$("[data-add]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var box = btn.closest("[data-product]");
      var p = JSON.parse(box.getAttribute("data-product"));
      var pack = $("[data-pack]", box).value;
      var qty = Math.max(1, parseInt($("[data-qty]", box).value, 10) || 1);
      var found = cart.filter(function (i) { return i.name === p.name && i.pack === pack; })[0];
      if (found) found.qty += qty; else cart.push({ name: p.name, cat: p.cat, pack: pack, qty: qty });
      save();
      toast("✔ " + p.name + " sepete eklendi");
    });
  });

  // Sepet sayfası
  function renderCart() {
    var list = $("[data-cart-list]"); if (!list) return;
    if (!cart.length) {
      list.innerHTML = '<p class="muted">Sepetiniz boş. <a href="/urunler/">Ürünlere göz atın →</a></p>';
      return;
    }
    list.innerHTML = cart.map(function (i, idx) {
      return '<div class="cart-row"><div><b>' + esc(i.name) + '</b><small>' + esc(i.cat) + " · " + esc(i.pack) +
        '</small></div><input type="number" min="1" value="' + i.qty + '" data-idx="' + idx + '" aria-label="Adet">' +
        '<button type="button" data-del="' + idx + '" aria-label="Kaldır">✕</button></div>';
    }).join("");
  }
  var list = $("[data-cart-list]");
  if (list) {
    list.addEventListener("change", function (e) {
      var i = e.target.getAttribute("data-idx");
      if (i !== null) { cart[i].qty = Math.max(1, parseInt(e.target.value, 10) || 1); save(); }
    });
    list.addEventListener("click", function (e) {
      var i = e.target.getAttribute("data-del");
      if (i !== null) { cart.splice(+i, 1); save(); }
    });
    var ps = $("[data-cart-province]"), last = store(PKEY);
    if (ps && last) ps.value = last;
  }
  var clr = $("[data-cart-clear]");
  if (clr) clr.addEventListener("click", function () { cart = []; save(); });

  var cf = $("[data-cart-form]");
  if (cf) cf.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!cart.length) { toast("Önce sepete ürün ekleyin"); return; }
    var f = new FormData(cf);
    var lines = ["*Toptan Teklif Talebi*", "", "Firma: " + f.get("firma")];
    if (f.get("yetkili")) lines.push("Yetkili: " + f.get("yetkili"));
    lines.push("Teslimat: " + f.get("il") + (f.get("ilce") ? " / " + f.get("ilce") : ""), "", "*Ürünler:*");
    cart.forEach(function (i, n) { lines.push((n + 1) + ") " + i.name + " — " + i.qty + " x " + i.pack); });
    if (f.get("not")) lines.push("", "Not: " + f.get("not"));
    lines.push("", "Ürün + nakliye dahil fiyat teklifi rica ederim.");
    openWA(lines.join("\n"));
  });

  // Hızlı formlar (il sayfası, iletişim)
  $$("[data-quick-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var txt = "*Teklif / Bilgi Talebi*\n\nFirma: " + f.get("firma") +
        "\nİl: " + f.get("il") + (f.get("ilce") ? " / " + f.get("ilce") : "") +
        "\n\n" + f.get("not");
      if (cart.length) txt += "\n\nSepetimdeki ürünler:\n" + cart.map(function (i) { return "- " + i.name + " — " + i.qty + " x " + i.pack; }).join("\n");
      openWA(txt);
    });
  });

  // Ana sayfa il seçici
  var finder = $("[data-finder]");
  if (finder) {
    var sel = $("[data-province-select]", finder), res = $("[data-finder-result]", finder);
    sel.addEventListener("change", function () {
      if (!sel.value) { res.hidden = true; return; }
      res.hidden = false;
      res.innerHTML = "Sevkiyat bilgisi için <b>" + esc(sel.options[sel.selectedIndex].text.split("· ")[1]) + "</b> sayfasına gidin.";
    });
    finder.addEventListener("submit", function (e) {
      e.preventDefault();
      if (sel.value) location.href = "/iller/" + sel.value + "/";
    });
  }

  // İl arama filtresi
  var flt = $("[data-filter]");
  if (flt) flt.addEventListener("input", function () {
    var q = flt.value.toLocaleLowerCase("tr");
    $$("[data-group]").forEach(function (g) {
      var any = false;
      $$(".chip", g).forEach(function (c) {
        var ok = c.textContent.toLocaleLowerCase("tr").indexOf(q) > -1;
        c.hidden = !ok; if (ok) any = true;
      });
      g.hidden = !any;
    });
  });

  renderCount(); renderCart();
})();
