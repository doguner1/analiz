# 🎯 Güner AV - SERP & Rakip İstihbarat Botu

Bu depo, **Güner AV (`gunerav.site`)** için Malatya yerelindeki ve Türkiye genelindeki avcılık, balıkçılık ve outdoor sektöründeki rakipleri analiz etmek, SERP (arama motoru sonuçları) sıralamalarını haritalandırmak ve arama motorlarında rakiplerin önüne geçecek stratejileri belirlemek üzere geliştirilmiş istihbarat yazılımlarını içerir.

---

## 📁 Proje İçeriği

* **`scanner.py`**: 27 farklı anahtar kelimeyi (hem Malatya yerel hem de genel avcılık terimleri) otomatik olarak tarayan, ilk sayfalara çıkan rakipleri tespit eden, başlık (`<title>`), meta açıklamalar, `H1-H3` hiyerarşisi, kelime yoğunluğu ve schema verilerini inceleyen ana motor.
* **`backlink_recon.py`**: Hedef rakip domainlerin (örn. `ozsanavbayi.com`, `bozmazbalikavmalzemeleri.com`) internette nereden link, referans ve dizin kaydı aldığını bulan dedektif bot.
* **`run.sh`**: Tek komutla sanal ortamı kurup taramayı baştan sona çalıştıran script.
* **`RAKIP_ANALIZ_VE_STRATEJI_RAPORU.md`**: Yapılan tarama sonucunda ortaya çıkan detaylı yönetici özeti, rakip incelemeleri ve Güner AV için 5 aşamalı karşı hamle stratejisi.
* **`serp_results.json`**: 27 sorgunun ham SERP ve rakip analiz verilerini içeren JSON arşivi.

---

## 🚀 Hızlı Başlangıç

```bash
# Depoyu klonlayın
git clone https://github.com/doguner1/analiz.git
cd analiz

# Taramayı başlatın (Sanal ortamı otomatik kurar)
chmod +x run.sh
./run.sh

# Belirli bir rakibin backlink ayak izini inceleyin
./venv/bin/python backlink_recon.py ozsanavbayi.com
```

---

## 📊 Özet Bulgular (Neden Rakipler Önde?)

1. **Domain Yaşı Farkı:** Rakipler (Özsan Silah, Kolay Av vb.) 8-10 yıllık eski domainlerdir. Güner AV ise 3 haftalık yepyeni bir sitedir (Google Sandbox evresi).
2. **Programatik Sayfalar (Doorway Pages):** Konya merkezli `ozsanavbayi.com` sitesi, `av-tufegi-pompali-tufek-tek-cift-kirma-superpoze-av-tufegi-malatya.html` gibi illere özel açtığı sayfalarla sıralama almaktadır.
3. **Yerel Dizin Kayıtları (NAP Tutarlılığı):** Rakipler Bulurum, Haritane, Malatyarehberim gibi yerel firma rehberlerinde kayıtlıdır. Güner AV henüz bu dizinlerin tamamına eklenmemiştir.
4. **Google AI / Gemini Farkı:** Klasik eski algoritmalar yaşa baksa da, **Google AI Overview (Gemini) şimdiden Güner AV'yi Malatya'da 1. sıraya** yerleştirmiştir.
