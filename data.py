# -*- coding: utf-8 -*-
"""Site verileri: firma bilgileri, ürün grupları ve 81 il."""

SITE = {
    "domain": "https://madeniyagdunyasi.com.tr",
    "name": "Madeni Yağ Dünyası",
    "company": "Karakaş Ticaret",
    "phone": "0501 542 14 22",
    "phone_tel": "+905015421422",
    "whatsapp": "905015421422",
    "address": "1229 Sokak No:7 Ostim OSB, Yenimahalle / Ankara",
    "maps": "https://www.google.com/maps/search/?api=1&query=1229+Sokak+No:7+Ostim+Yenimahalle+Ankara",
    "hours": "Pazartesi–Cumartesi 08:30–19:00",
}

CATEGORIES = [
    {
        "slug": "hidrolik-yaglar",
        "name": "Hidrolik Yağlar",
        "short": "Hidrolik Grubu",
        "icon": "hydraulic",
        "desc": "Ekskavatör, loder, beko loder, greyder ve vinç hidrolik sistemleri için yüksek basınç ve aşınma korumalı hidrolik yağları.",
        "intro": "İş makinelerinde arızaların büyük bölümü hidrolik sistemden gelir. Doğru viskozitede, temiz ve kaliteli hidrolik yağ; pompa, valf ve silindir ömrünü doğrudan uzatır. Şantiye ve iklim koşullarınıza göre doğru ürünü birlikte seçiyoruz.",
        "items": [
            {"name": "Hidrolik Yağ HM 32", "spec": "ISO VG 32 · Aşınma önleyici (AW)", "use": "Soğuk iklim, kış dönemi, hassas hidrolik devreler", "pack": ["16 L Teneke", "20 L Bidon", "180 Kg Varil"]},
            {"name": "Hidrolik Yağ HM 46", "spec": "ISO VG 46 · Aşınma önleyici (AW)", "use": "Ekskavatör ve loderlerde en yaygın kullanılan sınıf", "pack": ["16 L Teneke", "20 L Bidon", "180 Kg Varil", "1000 L IBC"]},
            {"name": "Hidrolik Yağ HM 68", "spec": "ISO VG 68 · Aşınma önleyici (AW)", "use": "Sıcak iklim, yaz dönemi, ağır yük altında çalışan makineler", "pack": ["16 L Teneke", "20 L Bidon", "180 Kg Varil", "1000 L IBC"]},
            {"name": "Hidrolik Yağ HM 100", "spec": "ISO VG 100", "use": "Pres, kırıcı ve yüksek sıcaklıkta çalışan sistemler", "pack": ["20 L Bidon", "180 Kg Varil"]},
            {"name": "Hidrolik Yağ HV 46 / HV 68", "spec": "Yüksek viskozite indeksli (HVI)", "use": "Gece-gündüz sıcaklık farkı yüksek şantiyeler, dış mekân", "pack": ["20 L Bidon", "180 Kg Varil"]},
            {"name": "SAE 10W Hidrolik / Şanzıman Yağı", "spec": "SAE 10W · İş makinesi tipi", "use": "Hidrolik ve powershift şanzımanı ortak kullanan makineler", "pack": ["20 L Bidon", "180 Kg Varil"]},
        ],
    },
    {
        "slug": "disli-yaglari",
        "name": "Dişli ve Şanzıman Yağları",
        "short": "Dişli Yağı Grubu",
        "icon": "gear",
        "desc": "Diferansiyel, şanzıman, redüktör ve son tahrik grupları için EP katkılı dişli yağları, TO-4 yağlar ve gresler.",
        "intro": "Ağır yük altında çalışan dişli grupları yüksek basınca dayanıklı (EP) yağlar ister. Kamyon diferansiyelinden asfalt plentinin redüktörüne kadar tüm dişli uygulamaları için ürünlerimiz stokta.",
        "items": [
            {"name": "Dişli Yağı SAE 80W-90", "spec": "API GL-5 · EP katkılı", "use": "Kamyon, damperli araç ve iş makinesi diferansiyelleri", "pack": ["16 L Teneke", "20 L Bidon", "180 Kg Varil"]},
            {"name": "Dişli Yağı SAE 85W-140", "spec": "API GL-5 · Ağır hizmet", "use": "Ağır yüklü akslar, son tahrik ve planet dişliler", "pack": ["16 L Teneke", "20 L Bidon", "180 Kg Varil"]},
            {"name": "Endüstriyel Dişli Yağı EP 150 / 220 / 320", "spec": "ISO VG 150–320 · CLP", "use": "Redüktörler, konveyörler, kırma-eleme tesisleri, asfalt plentleri", "pack": ["20 L Bidon", "180 Kg Varil"]},
            {"name": "Endüstriyel Dişli Yağı EP 460 / 680", "spec": "ISO VG 460–680", "use": "Yavaş dönen, ağır yüklü açık/kapalı dişliler", "pack": ["20 L Bidon", "180 Kg Varil"]},
            {"name": "TO-4 Şanzıman Yağı SAE 30 / SAE 50", "spec": "TO-4 spesifikasyonu", "use": "Dozer, greyder ve loder powershift şanzıman ve nihai tahrik", "pack": ["20 L Bidon", "180 Kg Varil"]},
            {"name": "Lityum EP2 Gres", "spec": "NLGI 2 · Yüksek basınç", "use": "Pim-burç, mafsal ve yatak noktaları", "pack": ["15 Kg Kova", "180 Kg Varil"]},
        ],
    },
    {
        "slug": "is-makinesi-yedek-parca",
        "name": "İş Makinesi Yedek Parçaları",
        "short": "Yedek Parça Grubu",
        "icon": "bucket",
        "desc": "Kova dişi, adaptör, bıçak, pim-burç, hidrolik hortum ve keçe takımları. CAT, Komatsu, JCB, Hitachi, Volvo, Hidromek ve Case uyumlu.",
        "intro": "Makinenin durduğu her saat şantiyeye maliyettir. Sık değişen aşınma ve bakım parçalarını yağ siparişinizle aynı sevkiyatta göndererek ayrı ayrı nakliye masrafından kurtarıyoruz. Parça numarası veya makine modeli ile sorgulayabilirsiniz.",
        "items": [
            {"name": "Kova Dişi ve Adaptör", "spec": "Ekskavatör / beko loder / loder", "use": "Kazı ve yükleme kovaları için aşınma parçaları", "pack": ["Adet", "Takım"]},
            {"name": "Bıçak ve Köşe Bıçak", "spec": "Greyder, dozer ve loder", "use": "Yol yapımı, tesviye ve sıyırma işleri", "pack": ["Adet", "Takım"]},
            {"name": "Pim ve Burç", "spec": "Kova, bom ve arm bağlantıları", "use": "Boşluk yapan mafsal noktalarının yenilenmesi", "pack": ["Adet", "Takım"]},
            {"name": "Hidrolik Hortum ve Rakor", "spec": "2 ve 4 tel örgülü · ölçüye göre", "use": "Patlayan hortumların hızlı değişimi", "pack": ["Adet", "Metre"]},
            {"name": "Silindir Keçe ve Conta Takımları", "spec": "Bom, arm, kova, direksiyon silindirleri", "use": "Yağ kaçıran silindirlerin revizyonu", "pack": ["Takım"]},
            {"name": "Yürüyüş Aksamı Parçaları", "spec": "Palet, makara, zincir, avare", "use": "Paletli ekskavatör ve dozerler", "pack": ["Adet", "Takım"]},
        ],
    },
    {
        "slug": "is-makinesi-filtreleri",
        "name": "İş Makinesi Filtreleri",
        "short": "Filtre Grubu",
        "icon": "filter",
        "desc": "Yağ, yakıt, separatör, hava, hidrolik, şanzıman ve kabin filtreleri. Bakım setleri halinde toptan tedarik.",
        "intro": "Periyodik bakımı aksatmamak için filtreleri makine bazında set halinde hazırlıyoruz. Araç ve makine filosu olan firmalar için toplu bakım seti ve düzenli sevkiyat planı oluşturabiliyoruz.",
        "items": [
            {"name": "Motor Yağ Filtresi", "spec": "Muadil ve orijinal seçenekler", "use": "Her periyodik bakımda değişim", "pack": ["Adet", "Koli"]},
            {"name": "Yakıt ve Separatör Filtresi", "spec": "Su ayırıcılı", "use": "Kalitesiz yakıt riskine karşı enjektör koruması", "pack": ["Adet", "Koli"]},
            {"name": "Hava Filtresi (İç / Dış)", "spec": "Tozlu ortam dayanımlı", "use": "Hafriyat, maden ve kırma-eleme sahaları", "pack": ["Adet", "Takım"]},
            {"name": "Hidrolik Dönüş ve Emiş Filtresi", "spec": "Mikron değerine göre", "use": "Hidrolik yağ değişiminde zorunlu değişim", "pack": ["Adet", "Koli"]},
            {"name": "Şanzıman Filtresi", "spec": "Powershift ve otomatik şanzıman", "use": "Loder, greyder, dozer", "pack": ["Adet"]},
            {"name": "Periyodik Bakım Seti", "spec": "Makine modeline özel", "use": "250 / 500 / 1000 saat bakımları", "pack": ["Set"]},
        ],
    },
]

SECTORS = [
    ("İnşaat Firmaları", "Konut, sanayi ve altyapı projelerinde çalışan makine parkları için düzenli yağ ve filtre tedariki."),
    ("Yol Yapım Firmaları", "Greyder, silindir, finişer ve asfalt plentleri için dişli yağı, hidrolik yağ ve bıçak grubu."),
    ("Şantiyeler", "Şantiye deposuna varil ve IBC bazında teslimat, sahada bakım için set halinde filtre."),
    ("Hafriyat Firmaları", "Ekskavatör ve damperli kamyon filoları için kova dişi, hidrolik hortum ve diferansiyel yağı."),
    ("Kamu İhaleli Taşeronlar", "Belediye, KGM, DSİ ve TOKİ projelerinde çalışan taşeronlar için faturalı, düzenli tedarik."),
    ("Maden ve Taş Ocakları", "Kırma-eleme tesisleri için endüstriyel dişli yağları ve yüksek tozlu ortam filtreleri."),
]

# (plaka, il, bölge, Ankara'dan yaklaşık karayolu km)
PROVINCES_RAW = [
    (1, "Adana", "Akdeniz", 490), (2, "Adıyaman", "Güneydoğu Anadolu", 740),
    (3, "Afyonkarahisar", "Ege", 255), (4, "Ağrı", "Doğu Anadolu", 1060),
    (5, "Amasya", "Karadeniz", 335), (6, "Ankara", "İç Anadolu", 0),
    (7, "Antalya", "Akdeniz", 480), (8, "Artvin", "Karadeniz", 950),
    (9, "Aydın", "Ege", 570), (10, "Balıkesir", "Marmara", 530),
    (11, "Bilecik", "Marmara", 310), (12, "Bingöl", "Doğu Anadolu", 870),
    (13, "Bitlis", "Doğu Anadolu", 1060), (14, "Bolu", "Karadeniz", 190),
    (15, "Burdur", "Akdeniz", 420), (16, "Bursa", "Marmara", 385),
    (17, "Çanakkale", "Marmara", 650), (18, "Çankırı", "İç Anadolu", 130),
    (19, "Çorum", "Karadeniz", 245), (20, "Denizli", "Ege", 480),
    (21, "Diyarbakır", "Güneydoğu Anadolu", 910), (22, "Edirne", "Marmara", 680),
    (23, "Elazığ", "Doğu Anadolu", 750), (24, "Erzincan", "Doğu Anadolu", 680),
    (25, "Erzurum", "Doğu Anadolu", 870), (26, "Eskişehir", "İç Anadolu", 235),
    (27, "Gaziantep", "Güneydoğu Anadolu", 680), (28, "Giresun", "Karadeniz", 620),
    (29, "Gümüşhane", "Karadeniz", 750), (30, "Hakkari", "Doğu Anadolu", 1330),
    (31, "Hatay", "Akdeniz", 680), (32, "Isparta", "Akdeniz", 400),
    (33, "Mersin", "Akdeniz", 490), (34, "İstanbul", "Marmara", 450),
    (35, "İzmir", "Ege", 580), (36, "Kars", "Doğu Anadolu", 1070),
    (37, "Kastamonu", "Karadeniz", 240), (38, "Kayseri", "İç Anadolu", 315),
    (39, "Kırklareli", "Marmara", 650), (40, "Kırşehir", "İç Anadolu", 185),
    (41, "Kocaeli", "Marmara", 340), (42, "Konya", "İç Anadolu", 260),
    (43, "Kütahya", "Ege", 310), (44, "Malatya", "Doğu Anadolu", 660),
    (45, "Manisa", "Ege", 550), (46, "Kahramanmaraş", "Akdeniz", 620),
    (47, "Mardin", "Güneydoğu Anadolu", 1000), (48, "Muğla", "Ege", 620),
    (49, "Muş", "Doğu Anadolu", 980), (50, "Nevşehir", "İç Anadolu", 275),
    (51, "Niğde", "İç Anadolu", 345), (52, "Ordu", "Karadeniz", 540),
    (53, "Rize", "Karadeniz", 830), (54, "Sakarya", "Marmara", 290),
    (55, "Samsun", "Karadeniz", 410), (56, "Siirt", "Güneydoğu Anadolu", 1070),
    (57, "Sinop", "Karadeniz", 430), (58, "Sivas", "İç Anadolu", 440),
    (59, "Tekirdağ", "Marmara", 580), (60, "Tokat", "Karadeniz", 380),
    (61, "Trabzon", "Karadeniz", 760), (62, "Tunceli", "Doğu Anadolu", 850),
    (63, "Şanlıurfa", "Güneydoğu Anadolu", 820), (64, "Uşak", "Ege", 370),
    (65, "Van", "Doğu Anadolu", 1220), (66, "Yozgat", "İç Anadolu", 215),
    (67, "Zonguldak", "Karadeniz", 270), (68, "Aksaray", "İç Anadolu", 225),
    (69, "Bayburt", "Karadeniz", 820), (70, "Karaman", "İç Anadolu", 370),
    (71, "Kırıkkale", "İç Anadolu", 80), (72, "Batman", "Güneydoğu Anadolu", 990),
    (73, "Şırnak", "Güneydoğu Anadolu", 1170), (74, "Bartın", "Karadeniz", 290),
    (75, "Ardahan", "Doğu Anadolu", 1050), (76, "Iğdır", "Doğu Anadolu", 1180),
    (77, "Yalova", "Marmara", 390), (78, "Karabük", "Karadeniz", 215),
    (79, "Kilis", "Güneydoğu Anadolu", 740), (80, "Osmaniye", "Akdeniz", 580),
    (81, "Düzce", "Karadeniz", 230),
]

REGION_NOTES = {
    "İç Anadolu": "bölgedeki yol genişletme, OSB altyapı, baraj ve toplu konut projeleri ile taş ocakları",
    "Karadeniz": "bölgedeki tünel, viyadük, HES ve sahil yolu projeleri ile heyelan-ıslah çalışmaları",
    "Marmara": "bölgedeki otoyol, kentsel dönüşüm, liman ve sanayi yatırımları",
    "Ege": "bölgedeki maden sahaları, mermer ocakları, sulama ve otoyol projeleri",
    "Akdeniz": "bölgedeki deprem sonrası yeniden yapılanma, liman, sulama ve turizm altyapı projeleri",
    "Doğu Anadolu": "bölgedeki baraj, yol, tünel ve kamu konut projeleri",
    "Güneydoğu Anadolu": "bölgedeki sulama kanalları, deprem konutları, yol ve enerji yatırımları",
}

TR_MAP = str.maketrans("çğıöşüÇĞİÖŞÜâîû", "cgiosuCGIOSUaiu")


def slugify(s):
    return s.translate(TR_MAP).lower().replace(" ", "-")


def tier(km):
    if km == 0:
        return {"key": "merkez", "label": "Merkez Depo", "eta": "Aynı gün", "badge": "Aynı Gün Teslim"}
    if km <= 300:
        return {"key": "yakin", "label": "Öncelikli Bölge", "eta": "Ertesi iş günü", "badge": "Ertesi Gün Sevkiyat"}
    if km <= 600:
        return {"key": "orta", "label": "Hızlı Sevkiyat Bölgesi", "eta": "1–2 iş günü", "badge": "1–2 Günde Teslim"}
    return {"key": "uzak", "label": "Türkiye Geneli Sevkiyat", "eta": "2–4 iş günü", "badge": "2–4 Günde Teslim"}


PROVINCES = []
for plate, name, region, km in PROVINCES_RAW:
    PROVINCES.append({
        "plate": plate, "name": name, "region": region, "km": km,
        "slug": slugify(name), "tier": tier(km),
    })
PROVINCES_BY_KM = sorted(PROVINCES, key=lambda p: p["km"])
