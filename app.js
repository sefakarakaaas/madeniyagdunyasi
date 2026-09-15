/* Madeni Yağ Dünyası — teklif sepeti, marka/stok butonları ve WhatsApp sohbet kutusu */
(function () {
  "use strict";
  var WA = "905015421422";
  var KEY = "myd_cart_v2";
  var PKEY = "myd_province";
  var AUTO_OPEN_MS = 10000;

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
  function itemLabel(i) { return (i.brand ? i.brand + " " : "") + i.name; }

  function toast(msg) {
    var t = $("[data-toast]"); if (!t) return;
    t.textContent = msg; t.classList.add("show");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("show"); t.textContent = ""; }, 2200);
  }
  function openWA(text) {
    window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent(text), "_blank", "noopener");
  }
  function cartLines() {
    return cart.map(function (i, n) { return (n + 1) + ") " + itemLabel(i) + " — " + i.qty + " x " + i.pack; });
  }
  function save() { store(KEY, cart); renderCount(); renderCart(); }
  function renderCount() {
    $$("[data-cart-count]").forEach(function (el) { el.textContent = cart.length; });
  }

  // Mobil menü
  var mb = $("[data-menu]"), nav = $("[data-nav]");
  if (mb && nav) mb.addEventListener("click", function () {
    var o = nav.classList.toggle("open"); mb.setAttribute("aria-expanded", o);
  });

  // İl sayfasındaysak ili hatırla
  var sp = $("[data-set-province]");
  if (sp) store(PKEY, sp.getAttribute("data-set-province"));

  // Sepete ekle (marka bazında)
  $$("[data-add]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var box = btn.closest("[data-product]");
      var p = JSON.parse(box.getAttribute("data-product"));
      var brand = btn.getAttribute("data-brand") || "";
      var pack = $("[data-pack]", box).value;
      var qty = Math.max(1, parseInt($("[data-qty]", box).value, 10) || 1);
      var found = cart.filter(function (i) { return i.name === p.name && i.pack === pack && i.brand === brand; })[0];
      if (found) found.qty += qty; else cart.push({ name: p.name, brand: brand, cat: p.cat, pack: pack, qty: qty });
      save();
      toast("✔ " + (brand ? brand + " " : "") + p.name + " sepete eklendi");
    });
  });

  // Stok butonu: seçili ambalaj bilgisini mesaja ekle
  $$("[data-stock]").forEach(function (a) {
    a.addEventListener("click", function () {
      var box = a.closest("[data-product]");
      var pack = box && $("[data-pack]", box);
      if (!pack) return;
      var url = new URL(a.href);
      if (!a.getAttribute("data-base")) a.setAttribute("data-base", url.searchParams.get("text") || "");
      var text = a.getAttribute("data-base").replace(" ürününün stok durumu", " (" + pack.value + ") ürününün stok durumu");
      url.searchParams.set("text", text);
      a.href = url.toString();
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
      return '<div class="cart-row"><div><b>' + esc(itemLabel(i)) + '</b><small>' + esc(i.cat) + " · " + esc(i.pack) +
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
    lines = lines.concat(cartLines());
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
      if (cart.length) txt += "\n\nSepetimdeki ürünler:\n" + cartLines().join("\n");
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

  /* ---------------- WhatsApp sohbet kutusu ---------------- */
  var chat = $("[data-chat]");
  if (chat) {
    var panel = $("[data-chat-panel]", chat),
      fab = $("[data-chat-toggle]", chat),
      teaser = $("[data-chat-teaser]", chat),
      badge = $("[data-chat-badge]", chat),
      input = $("[data-chat-input]", chat),
      optsBox = $("[data-chat-options]", chat),
      form = $("[data-chat-form]", chat),
      root = document.documentElement,
      wide = window.matchMedia("(min-width: 1100px)"),
      topic = document.body.getAttribute("data-chat-topic"),
      city = document.body.getAttribute("data-chat-city"),
      touched = false;

    var now = new Date();
    $("[data-chat-time]", chat).textContent =
      ("0" + now.getHours()).slice(-2) + ":" + ("0" + now.getMinutes()).slice(-2);

    var options;
    if (city) {
      options = [
        city + " iline sevkiyat hakkında bilgi almak istiyorum.",
        city + " için toptan fiyat teklifi almak istiyorum.",
        "Ürünlerin stok durumu hakkında bilgi almak istiyorum."
      ];
    } else if (topic) {
      options = [
        topic.charAt(0).toLocaleUpperCase("tr") + topic.slice(1) + " hakkında bilgi almak istiyorum.",
        topic.charAt(0).toLocaleUpperCase("tr") + topic.slice(1) + " için fiyat teklifi almak istiyorum.",
        "Bu ürünün stok durumu hakkında bilgi almak istiyorum."
      ];
    } else {
      options = [
        "Ürünler hakkında bilgi almak istiyorum.",
        "Toptan fiyat teklifi almak istiyorum.",
        "Şantiyeme sevkiyat hakkında bilgi almak istiyorum."
      ];
    }
    if (cart.length) options.push("Sepetimdeki ürünler için teklif istiyorum.");
    optsBox.innerHTML = options.map(function (o) {
      return '<button type="button" class="wchat-opt">' + esc(o) + "</button>";
    }).join("");
    optsBox.addEventListener("click", function (e) {
      var b = e.target.closest(".wchat-opt"); if (!b) return;
      $$(".wchat-opt", optsBox).forEach(function (x) { x.classList.toggle("on", x === b); });
      input.value = b.textContent;
      autoSize(); input.focus();
    });

    function autoSize() { input.style.height = "auto"; input.style.height = Math.min(input.scrollHeight, 120) + "px"; }
    input.addEventListener("input", autoSize);
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); form.requestSubmit ? form.requestSubmit() : form.dispatchEvent(new Event("submit")); }
    });

    function dock() { root.classList.toggle("chat-docked", !panel.hidden && wide.matches); }
    function open() {
      touched = true;
      panel.hidden = false; teaser.hidden = true; badge.hidden = true;
      fab.setAttribute("aria-expanded", "true"); fab.classList.add("is-open");
      dock();
    }
    function close() {
      touched = true;
      panel.hidden = true;
      fab.setAttribute("aria-expanded", "false"); fab.classList.remove("is-open");
      dock();
    }
    fab.addEventListener("click", function () { panel.hidden ? open() : close(); });
    $("[data-chat-close]", chat).addEventListener("click", close);
    teaser.addEventListener("click", function (e) {
      if (e.target.closest("[data-chat-teaser-close]")) { teaser.hidden = true; touched = true; return; }
      open();
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) close(); });
    if (wide.addEventListener) wide.addEventListener("change", dock);

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = input.value.trim();
      if (!msg) { input.focus(); toast("Lütfen bir konu seçin veya mesaj yazın"); return; }
      if (/Sepetimdeki ürünler/.test(msg) && cart.length) msg += "\n\n" + cartLines().join("\n");
      msg += "\n\n(Sayfa: " + location.href + ")";
      openWA(msg);
    });

    // Sayfada 10 saniyeden uzun kalınca: geniş ekranda panel yana yerleşir (yazıların üstüne binmez),
    // dar ekranda yalnızca küçük bir karşılama balonu gösterilir.
    setTimeout(function () {
      if (touched || !panel.hidden) return;
      var msg = city ? city + " iline sevkiyat hakkında bilgi almak ister misiniz?"
        : topic ? "Ürünlerimiz hakkında bilgi almak ister misiniz?"
        : "Merhaba 👋 Size nasıl yardımcı olabiliriz?";
      $("[data-chat-teaser-text]", chat).textContent = msg;
      if (wide.matches) { open(); touched = false; }
      else {
        teaser.hidden = false; badge.hidden = false;
        setTimeout(function () { teaser.hidden = true; }, 6000);
      }
    }, AUTO_OPEN_MS);
  }

  renderCount(); renderCart();
})();
