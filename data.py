# -*- coding: utf-8 -*-
"""Site verileri: firma bilgileri, ürün grupları ve 81 il."""

SITE = {
    "domain": "https://madeniyagdunyasi.com.tr",
    "name": "Madeni Yağ Dünyası",
    "company": "Petromia Madeni Yağ A.Ş.",
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


# Sevkiyat bölgeleri (TÜİK İBBS 1. düzey bölgeleri)
ZONES = {
    "İstanbul": [34],
    "Batı Marmara": [59, 22, 39, 10, 17],
    "Ege": [35, 9, 20, 48, 45, 3, 43, 64],
    "Doğu Marmara": [16, 26, 11, 41, 54, 81, 14, 77],
    "Batı Anadolu": [6, 42, 70],
    "Akdeniz": [7, 32, 15, 1, 33, 31, 46, 80],
    "Orta Anadolu": [71, 68, 51, 50, 40, 38, 58, 66],
    "Batı Karadeniz": [67, 78, 74, 37, 18, 57, 55, 60, 19, 5],
    "Doğu Karadeniz": [61, 52, 28, 53, 8, 29],
    "Kuzeydoğu Anadolu": [25, 24, 69, 4, 36, 76, 75],
    "Ortadoğu Anadolu": [44, 23, 12, 62, 65, 49, 13, 30],
    "Güneydoğu Anadolu": [27, 2, 79, 63, 21, 47, 72, 73, 56],
}
ZONE_OF = {pl: z for z, pls in ZONES.items() for pl in pls}
assert len(ZONE_OF) == 81

# İl hakkında kısa bilgiler
INFO = {
    1: "Çukurova'nın merkezi Adana; Seyhan ve Ceyhan nehirlerinin beslediği verimli ovası, tekstil, gıda ve ağır sanayisiyle Türkiye'nin büyük üretim şehirlerinden biridir.",
    2: "Nemrut Dağı'na ev sahipliği yapan Adıyaman, Atatürk Barajı kıyısında yer alır; ekonomisinde tekstil, çimento ve petrol üretimi öne çıkar.",
    3: "Afyonkarahisar, Ege ile İç Anadolu'yu bağlayan önemli bir karayolu kavşağıdır; mermer ocakları, termal turizm ve gıda sanayisiyle bilinir.",
    4: "Türkiye'nin en yüksek dağı Ağrı Dağı'nın bulunduğu Ağrı, Gürbulak sınır kapısıyla İran'a açılır; ekonomide hayvancılık belirleyicidir.",
    5: "Yeşilırmak vadisinde kurulu tarihi Amasya, elma üretimi ile Suluova ve Merzifon çevresindeki sanayi yatırımlarıyla tanınır.",
    6: "Başkent Ankara, depomuzun bulunduğu şehirdir; Ostim, İvedik ve Sincan OSB'leriyle iş makinesi, savunma ve imalat sanayisinin merkezlerinden biridir.",
    7: "Türkiye'nin turizm başkenti Antalya'da otel, konut ve altyapı yatırımları ile seracılık ve taş ocakları nedeniyle iş makinesi kullanımı yoğundur.",
    8: "Dağlık ve ormanlık Artvin, Çoruh Nehri üzerindeki Deriner ve Yusufeli barajları gibi büyük enerji projeleri ve bakır madenciliğiyle bilinir.",
    9: "Büyük Menderes ovasındaki Aydın; incir, zeytin ve pamuk üretimi ile jeotermal enerji yatırımlarıyla öne çıkan bir Ege ilidir.",
    10: "Hem Marmara hem Ege kıyısı olan Balıkesir; bor ve mermer madenciliği, hayvancılık ve gıda sanayisiyle gelişmiş bir ildir.",
    11: "İstanbul–Ankara hattı üzerindeki Bilecik, Bozüyük'teki seramik ve mermer sanayisi ile Osmanlı'nın kuruluş yeri Söğüt'le bilinir.",
    12: "Doğu Anadolu'nun dağlık illerinden Bingöl, baraj ve HES projeleriyle, hayvancılık ve arıcılığıyla öne çıkar.",
    13: "Van Gölü kıyısındaki Bitlis, Nemrut Krater Gölü ve Ahlat Selçuklu Mezarlığı'na ev sahipliği yapar.",
    14: "İstanbul–Ankara otoyolu üzerindeki Bolu; Bolu Dağı Tüneli, tavukçuluk, orman ürünleri ve doğa turizmiyle bilinir.",
    15: "Göller Bölgesi'ndeki Burdur; mermer ocakları, hayvancılık ve süt ürünleri üretimiyle tanınır.",
    16: "Otomotiv ve tekstil sanayisinin merkezi Bursa, çok sayıda organize sanayi bölgesiyle Türkiye'nin en büyük üretim şehirlerinden biridir.",
    17: "Çanakkale 1915 Köprüsü'nün bulunduğu Çanakkale; enerji santralleri, madencilik ve tarih turizmiyle öne çıkar.",
    18: "Ankara'ya komşu Çankırı; tuz mağarası, organize sanayi bölgesi ve ahşap-gıda sanayisiyle bilinir, depomuza en yakın illerden biridir.",
    19: "Leblebisiyle ünlü Çorum'da tuğla-kiremit, çimento ve un sanayisi gelişmiştir; Hitit başkenti Hattuşa da bu ildedir.",
    20: "Tekstil ihracatında güçlü Denizli; mermer-traverten ocakları ve Pamukkale travertenleriyle tanınır.",
    21: "Dicle kıyısındaki Diyarbakır, Güneydoğu'nun en büyük şehirlerindendir; petrol üretimi ve inşaat sektörü hareketlidir.",
    22: "Avrupa'ya açılan Kapıkule sınır kapısının bulunduğu Edirne; ayçiçeği ve pirinç üretimiyle bilinen bir Trakya ilidir.",
    23: "Keban Barajı kıyısındaki Elazığ; krom madenciliği, mermer ve çimento sanayisiyle bilinir.",
    24: "Kemaliye ve Girlevik Şelalesi'yle tanınan Erzincan, madencilik faaliyetleri ve demiryolu hattı üzerindeki konumuyla öne çıkar.",
    25: "Doğu Anadolu'nun en büyük şehirlerinden Erzurum, Palandöken kayak merkezi ve sert kışlarıyla bilinir; soğuk iklimde düşük viskoziteli yağ ihtiyacı artar.",
    26: "Raylı sistemler, havacılık ve makine sanayisi gelişmiş Eskişehir; lületaşı ve Kırka bor madenleriyle tanınan bir üniversite şehridir.",
    27: "Güneydoğu'nun sanayi başkenti Gaziantep; tekstil, gıda ve plastik sektörlerinde çok sayıda OSB barındırır.",
    28: "Fındık üretiminin merkezlerinden Giresun'da Karadeniz Sahil Yolu ve dağlık iç kesimler nedeniyle yol-tünel çalışmaları yoğundur.",
    29: "Adını gümüş madenlerinden alan Gümüşhane, Zigana Tüneli ve dağlık yollarıyla bilinir.",
    30: "Türkiye'nin en dağlık illerinden Hakkari; Zap vadisi, baraj ve yol projeleriyle öne çıkar.",
    31: "Antakya'nın bulunduğu Hatay; İskenderun'daki demir-çelik ve liman tesisleriyle bilinir, 2023 depremleri sonrası yoğun yeniden yapılanma sürmektedir.",
    32: "Gül ve lavanta üretimiyle ünlü Isparta, Göller Bölgesi'nde yer alır ve Süleyman Demirel Havalimanı'na sahiptir.",
    33: "Türkiye'nin en büyük limanlarından Mersin Limanı'na ev sahipliği yapan Mersin; Akkuyu Nükleer Santrali ve lojistik yatırımlarıyla öne çıkar.",
    34: "Türkiye'nin en büyük şehri İstanbul'da metro, köprü, kentsel dönüşüm ve konut projeleri nedeniyle iş makinesi kullanımı çok yoğundur.",
    35: "Ege'nin en büyük liman ve sanayi şehri İzmir; Aliağa'daki petrokimya ve demir-çelik tesisleriyle bilinir.",
    36: "Ani Harabeleri ve Kars kaşarıyla ünlü Kars, hayvancılığın öne çıktığı sert iklimli bir doğu ilidir.",
    37: "Batı Karadeniz'in orman varlığı en zengin illerinden Kastamonu; ahşap sanayisi ve Küre bakır madenleriyle bilinir.",
    38: "Mobilya, metal ve beyaz eşya sanayisiyle güçlü Kayseri; Erciyes Dağı ve büyük organize sanayi bölgesiyle tanınan bir ticaret şehridir.",
    39: "Trakya'daki Kırklareli; cam ve çimento sanayisi ile İğneada longoz ormanlarıyla bilinir.",
    40: "Ahilik kültürünün merkezi Kırşehir, Kızılırmak havzasında tahıl üretimi ve hayvancılıkla öne çıkar.",
    41: "Türkiye'nin sanayi yoğunluğu en yüksek illerinden Kocaeli; otomotiv, petrokimya ve liman tesisleriyle bilinir.",
    42: "Yüzölçümü en büyük il olan Konya; tahıl üretimi, döküm-makine ve otomotiv yan sanayisiyle güçlü bir sanayi merkezidir.",
    43: "Çini, seramik ve termal kaynaklarıyla bilinen Kütahya'da Tunçbilek ve Seyitömer linyit sahaları ile termik santraller bulunur.",
    44: "Kayısı üretiminin dünyadaki merkezi Malatya'da, 2023 depremleri sonrası kapsamlı konut ve altyapı çalışmaları sürmektedir.",
    45: "Beyaz eşya ve elektronik sanayisi güçlü OSB'siyle Manisa, üzüm üretiminde de Türkiye'nin önde gelen illerindendir.",
    46: "Tekstil sanayisi ve dondurmasıyla ünlü Kahramanmaraş, 2023 depremlerinin merkez üssü olduğundan geniş çaplı yeniden inşa sürecindedir.",
    47: "Taş mimarisiyle ünlü Mardin; Nusaybin sınır kapısı ve çimento sanayisiyle bilinir.",
    48: "Bodrum, Marmaris ve Fethiye'nin bağlı olduğu Muğla; turizmin yanı sıra mermer ocakları ve termik santralleriyle bilinir.",
    49: "Muş Ovası'nda tahıl üretimi ve hayvancılıkla öne çıkan Muş, tarihi Malazgirt ilçesine ev sahipliği yapar.",
    50: "Kapadokya'nın kalbi Nevşehir; turizmin yanı sıra pomza (sünger taşı) madenciliğiyle de bilinir.",
    51: "Patates ve elma üretimiyle ünlü Niğde, Niğde–Ankara Otoyolu üzerindeki konumuyla lojistik açıdan avantajlıdır.",
    52: "Fındığın önemli merkezlerinden Ordu, denize dolgu yöntemiyle yapılan Ordu-Giresun Havalimanı'yla bilinir.",
    53: "Çay üretiminin merkezi Rize; denize dolgu Rize-Artvin Havalimanı ve dağlık yollarıyla tanınır.",
    54: "Otomotiv, raylı sistem ve savunma sanayisiyle gelişmiş Sakarya, İstanbul–Ankara sanayi koridorunda yer alır.",
    55: "Karadeniz'in en büyük şehri Samsun; liman, lojistik ve tıbbi cihaz sanayisiyle öne çıkar.",
    56: "Fıstığı ve battaniyesiyle bilinen Siirt'te bakır madenciliği ve baraj projeleri bulunur.",
    57: "Türkiye'nin en kuzey ucu İnceburun'un bulunduğu Sinop, balıkçılık ve turizmle öne çıkar.",
    58: "Yüzölçümüyle Türkiye'nin ikinci büyük ili Sivas; demiryolu araç sanayisi, çimento ve madencilikle bilinir.",
    59: "Çorlu–Çerkezköy sanayi bölgeleriyle Tekirdağ, Trakya'nın üretim merkezidir; liman ve lojistik yatırımları yoğundur.",
    60: "Yeşilırmak havzasındaki Tokat; sebze-meyve üretimi, bakır işlemeciliği ve Almus Barajı'yla bilinir.",
    61: "Doğu Karadeniz'in ticaret ve liman merkezi Trabzon; Sümela Manastırı ve Uzungöl'le tanınır.",
    62: "Munzur Vadisi Milli Parkı'yla bilinen Tunceli, Uzunçayır ve Keban baraj göllerine sahip dağlık bir ildir.",
    63: "Göbeklitepe'nin bulunduğu Şanlıurfa; GAP sulama kanalları ve Atatürk Barajı ile büyük sulama-altyapı yatırımlarına sahiptir.",
    64: "Deri ve battaniye sanayisiyle bilinen Uşak, Ege'nin iç kesiminde önemli bir tekstil merkezidir.",
    65: "Van Gölü kıyısındaki Van, Doğu Anadolu'nun büyük şehirlerindendir; Kapıköy sınır kapısı ve konut yatırımlarıyla öne çıkar.",
    66: "Ankara'ya yakın Yozgat; Yozgat Çamlığı Milli Parkı, tahıl üretimi ve hayvancılıkla bilinir, Ankara–Sivas hızlı tren hattı ilden geçer.",
    67: "Taşkömürü madenciliğinin merkezi Zonguldak; Ereğli demir-çelik tesisleri, Filyos Limanı ve termik santralleriyle bir ağır sanayi ilidir.",
    68: "Kamyon üretimi ve Ihlara Vadisi'yle bilinen Aksaray, önemli bir karayolu kavşağında yer alır.",
    69: "Türkiye'nin en az nüfuslu illerinden Bayburt, Çoruh Nehri kıyısında kurulmuştur ve Bayburt Kalesi'yle tanınır.",
    70: "Bisküvi ve un mamulleri sanayisiyle bilinen Karaman, Konya ovasına komşu bir ildir.",
    71: "MKE tesisleri ve Tüpraş rafinerisiyle bilinen Kırıkkale, depomuza en yakın sanayi ilidir.",
    72: "Türkiye petrol üretiminin önemli merkezi Batman; rafinerisi ve tarihi Hasankeyf'le bilinir.",
    73: "Cudi ve Gabar dağlarındaki petrol sahaları ile Habur sınır kapısına sahip Şırnak, enerji ve lojistikte öne çıkar.",
    74: "Tarihi Amasra ilçesiyle tanınan Bartın, Filyos Limanı'na yakın ormanlık bir Batı Karadeniz ilidir.",
    75: "Türkiye'nin en yüksek rakımlı illerinden Ardahan, Çıldır Gölü ve hayvancılığıyla bilinir.",
    76: "Ağrı Dağı'nın kuzeyindeki Iğdır, Dilucu sınır kapısıyla Nahçıvan'a açılır.",
    77: "Termal kaynakları, tersaneleri ve Osmangazi Köprüsü bağlantısıyla bilinen Yalova, Marmara'nın hızlı gelişen illerindendir.",
    78: "Kardemir demir-çelik fabrikasıyla Türkiye ağır sanayisinin öncü şehirlerinden olan Karabük, UNESCO Dünya Mirası Safranbolu'ya ev sahipliği yapar.",
    79: "Suriye sınırındaki Kilis; zeytin-zeytinyağı üretimi ve Öncüpınar sınır kapısıyla bilinir.",
    80: "Karatepe-Aslantaş ve yer fıstığıyla bilinen Osmaniye; demir-çelik sanayisi ve önemli kara-demiryolu kavşağındaki konumuyla öne çıkar.",
    81: "İstanbul–Ankara otoyolu üzerindeki Düzce; fındık, mobilya ve otomotiv yan sanayisiyle bilinir.",
}
assert len(INFO) == 81

# Madeni yağ markaları
BRANDS = ["Mobil", "Castrol", "Shell", "Opet", "Lukoil", "Alpet", "Borax"]
MACHINE_BRANDS = ["CAT", "Komatsu", "JCB", "Hitachi", "Volvo", "Hidromek"]

TR_MAP = str.maketrans("çğıöşüÇĞİÖŞÜâîû", "cgiosuCGIOSUaiu")


def slugify(s):
    return s.translate(TR_MAP).lower().replace(" ", "-")


def tier(km):
    """En uzak il 2–3 iş günü olacak şekilde teslim süresi sınıfları."""
    if km == 0:
        return {"key": "merkez", "eta": "Aynı gün", "badge": "Aynı Gün Teslim"}
    if km <= 300:
        return {"key": "yakin", "eta": "Ertesi iş günü", "badge": "Ertesi Gün Teslim"}
    if km <= 700:
        return {"key": "orta", "eta": "1–2 iş günü", "badge": "1–2 Günde Teslim"}
    return {"key": "uzak", "eta": "2–3 iş günü", "badge": "2–3 Günde Teslim"}


PROVINCES = []
for plate, name, region, km in PROVINCES_RAW:
    PROVINCES.append({
        "plate": plate, "name": name, "region": region, "km": km,
        "slug": slugify(name), "tier": tier(km),
        "zone": ZONE_OF[plate], "info": INFO[plate],
    })
PROVINCES_BY_KM = sorted(PROVINCES, key=lambda p: p["km"])

# Her ürün için 4–6 marka (yağ grupları) / uyumlu makine markaları (parça-filtre)
_BRAND_SETS = [
    ["Mobil", "Shell", "Castrol", "Opet", "Lukoil", "Alpet"],
    ["Shell", "Mobil", "Opet", "Alpet", "Borax"],
    ["Castrol", "Mobil", "Lukoil", "Borax"],
    ["Opet", "Shell", "Castrol", "Alpet", "Lukoil"],
    ["Mobil", "Castrol", "Shell", "Borax", "Opet", "Lukoil"],
    ["Lukoil", "Alpet", "Opet", "Borax"],
]
for _c in CATEGORIES:
    for _i, _item in enumerate(_c["items"]):
        if _c["slug"] in ("hidrolik-yaglar", "disli-yaglari"):
            _item["brands"] = _BRAND_SETS[(_i + (1 if _c["slug"] == "disli-yaglari" else 0)) % len(_BRAND_SETS)]
            _item["brand_label"] = "Markalar"
        else:
            _item["brands"] = MACHINE_BRANDS[:5] if _i % 2 else MACHINE_BRANDS[1:6]
            _item["brand_label"] = "Uyumlu makine markaları"

# Yağ hakkında sık sorulan sorular ({il} il adıyla değiştirilir)
OIL_FAQ = [
    ("Hidrolik yağ ne sıklıkla değiştirilmeli?",
     "Makine üreticisinin kılavuzundaki aralık esas alınır; iş makinelerinde bu süre genellikle 2.000–5.000 çalışma saati arasındadır. Hidrolik filtreler de yağla birlikte değiştirilmeli, tozlu şantiyelerde aralık kısaltılmalıdır."),
    ("HM 32, HM 46 ve HM 68 arasındaki fark nedir?",
     "Rakam, 40 °C'deki viskoziteyi (akışkanlık) gösterir. HM 32 soğuk havada, HM 46 dört mevsim genel kullanımda, HM 68 ise sıcak iklimde ve ağır yük altında tercih edilir. {il} şantiyeniz için mevsime uygun sınıfı birlikte belirleyebiliriz."),
    ("Kış aylarında hangi hidrolik yağı kullanmalıyım?",
     "Soğuk havalarda ilk çalıştırmada pompanın zorlanmaması için HM 32 veya viskozitesi sıcaklıkla daha az değişen HV sınıfı (HV 46 gibi) yağlar önerilir. Gece-gündüz sıcaklık farkı büyük bölgelerde HV yağlar avantaj sağlar."),
    ("Farklı marka yağlar birbirine karıştırılabilir mi?",
     "Önerilmez. Markaların katkı paketleri farklı olduğundan karışım köpürme ve tortu yapabilir. Zorunlu durumda yalnızca aynı sınıf ve viskozitede, az miktarda tamamlama yapılmalı ve ilk bakımda yağ tamamen değiştirilmelidir."),
    ("Dişli yağında API GL-4 ile GL-5 farkı nedir?",
     "GL-5 yağlar daha yüksek basınç (EP) katkısı içerir ve ağır yüklü hipoid diferansiyeller için uygundur. Bazı senkromeçli şanzımanlar GL-4 ister; doğru sınıf için araç veya makine kılavuzuna bakılmalıdır."),
    ("TO-4 yağ nedir, motor yağı yerine kullanılabilir mi?",
     "TO-4; dozer, greyder ve loderlerin powershift şanzıman, nihai tahrik ve ıslak fren sistemleri için geliştirilmiş bir spesifikasyondur. Sürtünme özellikleri farklı olduğundan motor yağı yerine veya motor yağı onun yerine kullanılmamalıdır."),
    ("Madeni yağ ile sentetik yağ arasındaki fark nedir?",
     "Madeni yağlar ham petrolün rafinasyonuyla, sentetik yağlar kimyasal olarak üretilir. Sentetikler daha geniş sıcaklık aralığında çalışır ve daha uzun ömürlüdür ancak maliyeti yüksektir. İş makinesi hidrolik ve dişli sistemlerinin çoğunda kaliteli madeni yağ yeterlidir."),
    ("Yağın bozulduğunu nasıl anlarım?",
     "Koyulaşma veya incelme, bulanık ya da sütlü görünüm (su karışması), köpürme, yanık koku ve sistemde sıcaklık artışı başlıca işaretlerdir. Büyük makine parklarında periyodik yağ analizi yaptırmak arızaları önceden yakalamayı sağlar."),
    ("Varil ve bidonları şantiyede nasıl depolamalıyım?",
     "Ambalajlar kapalı, serin ve kuru bir alanda, doğrudan güneş ve yağıştan korunarak saklanmalıdır. Variller açık alanda kalacaksa kapakları yağmur suyu toplamayacak şekilde yan yatırılmalı, açılan ambalaj kısa sürede tüketilmelidir."),
    ("Atık yağlar ne yapılmalı?",
     "Atık yağlar toprağa, kanalizasyona veya suya dökülemez. Atık Yağların Kontrolü Yönetmeliği kapsamında ayrı biriktirilip lisanslı toplama firmalarına teslim edilmelidir. {il} içindeki lisanslı toplayıcılar için bize danışabilirsiniz."),
]
