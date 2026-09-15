# madeniyagdunyasi.com.tr

İnşaat, yol, hafriyat firmaları ve şantiyeler için toptan madeni yağ, hidrolik yağ, dişli yağı,
iş makinesi yedek parça ve filtre satış/iletişim platformu. Ankara Ostim çıkışlı, 81 ile özel sayfa.

## Yapı
| Dosya | Açıklama |
|---|---|
| `data.py` | Firma bilgileri, ürün grupları, 81 il (plaka, bölge, Ankara'ya mesafe) |
| `build.py` | Statik site üreticisi (sadece Python standart kütüphanesi) → `dist/` |
| `style.css`, `app.js`, `favicon.svg` | Tasarım, teklif sepeti ve WhatsApp formları |

## Yerelde çalıştırma
```bash
python3 build.py
cd dist && python3 -m http.server 8000
```

## Cloudflare Pages ayarları
- Framework preset: **None**
- Build command: `python3 build.py`
- Build output directory: `dist`

## Güncelleme
Telefon, adres, ürün veya il bilgisini `data.py` içinden değiştirip GitHub'a gönderin;
Cloudflare Pages siteyi otomatik yeniden oluşturur.
