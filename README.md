# Haber-Yatırım-Analiz

Yabancı ve yerli haber kaynaklarını (savaş, yaptırım, maden gibi jeopolitik olaylar) gerçek zamanlı takip edip, doğal dil işleme ve tarihsel jeopolitik risk (GPR) korelasyonu kullanarak altın/BIST için yatırım eğilimi sinyali üreten ve önemli haberlerde Telegram üzerinden bildirim gönderen kişisel bir analiz sistemi.

> **Not:** Bu proje deneysel ve kişisel bir çalışmadır. Ürettiği sinyaller **finansal tavsiye değildir**. Herhangi bir yatırım kararı vermeden önce kendi araştırmanızı yapın ve gerekirse bir finansal danışmana başvurun.

## Nasıl Çalışıyor?

Sistem, RSS kaynaklarından çektiği her haberi aşağıdaki adımlardan geçirir:

```
RSS'ten haber çekme (BBC, AA)
        ↓
Türkçe → İngilizce çeviri
        ↓
Konu sınıflandırma (savaş / yaptırım / maden)
        ↓
Duygu analizi (FinBERT)
        ↓
Tarihsel korelasyon referansı (jeopolitik olay günlerinde altın eğilimi)
        ↓
Tavsiye skoru ve etiketi üretme
        ↓
SQLite veritabanına kayıt
        ↓
Anlamlı sinyallerde Telegram bildirimi
```

Haberin ilgili olup olmadığı (savaş/yaptırım/maden ile bağlantılı mı) ve haberin duygu yönü (olumlu/olumsuz/nötr), geçmişte benzer jeopolitik olay günlerinde altının ortalama nasıl hareket ettiğine dair tarihsel istatistiklerle birleştirilerek `-1` ile `1` arasında bir skor ve buna karşılık gelen okunabilir bir etiket ("Dikkatli olunmalı, düşüş eğilimi var" gibi) üretilir.

Sadece kategoriyle ilgili ve yeterince belirgin (nötr olmayan) sinyaller için Telegram üzerinden bildirim gönderilir; her yeni haber için bildirim gönderilmez.

## Kullanılan Teknolojiler

- **feedparser** — RSS akışlarını okuma
- **deep-translator** — Türkçe → İngilizce çeviri (Google Translate)
- **nltk** — kelime kökü bulma (stemming) ve tokenizasyon
- **transformers (ProsusAI/FinBERT)** — finansa özel duygu analizi
- **pandas** — tarihsel jeopolitik risk verisi (GPR) üzerinde istatistik hesaplama
- **yfinance** — altın ve BIST fiyat verisi
- **sqlite3** — görülen haberlerin ve analiz sonuçlarının kalıcı depolanması
- **python-dotenv** — ortam değişkenleri / gizli bilgilerin yönetimi
- **requests** — Telegram Bot API ile bildirim gönderimi

## Klasör Yapısı

```
src/haber_yatirim/
├── haber_toplama/     # RSS'ten haber çekme ve pipeline'ı orkestre etme
├── analiz/             # Çeviri, konu sınıflandırma, duygu analizi, tarihsel korelasyon
├── sinyaller/           # Tavsiye üretimi ve Telegram bildirim gönderimi
├── depolama/            # SQLite veritabanı bağlantısı ve kayıt işlemleri
├── zamanlayici/         # Pipeline'ı periyodik çalıştıran zamanlayıcı
└── piyasa_verisi/       # Altın ve BIST fiyat verisi çekme (yfinance)

veri/
└── ham/                 # Ham veri setleri (ör. tarihsel GPR/altın verisi)
```

## Kurulum

1. Depoyu klonlayın ve proje klasörüne girin.
2. Bağımlılıkları kurun:
   ```
   pip install -r requirements.txt
   ```
3. Proje kök dizininde bir `.env` dosyası oluşturun (`.env.example` dosyasına bakabilirsiniz) ve aşağıdaki değişkenleri kendi değerlerinizle doldurun:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   ```
   `.env` dosyası `.gitignore` içinde olduğu için repoya gönderilmez; kendi gizli bilgilerinizi asla commit etmeyin.

## Çalıştırma

Pipeline'ı tek seferlik çalıştırmak için:
```
python -m haber_yatirim.haber_toplama.haber_cekici
```

Pipeline'ı 30 dakikada bir otomatik tekrar eden şekilde çalıştırmak için:
```
python -m haber_yatirim.zamanlayici.gorevler
```

## Yol Haritası

- [x] RSS haber toplama (BBC, AA)
- [x] Türkçe → İngilizce çeviri
- [x] Kural tabanlı konu sınıflandırma (savaş / yaptırım / maden)
- [x] FinBERT ile duygu analizi
- [x] Hazır (Kaggle) GPR veri seti ile tarihsel korelasyon referansı
- [x] Tavsiye skoru/etiketi üretimi
- [x] SQLite'a analiz sonuçlarının kaydı
- [x] Periyodik otomatik çalışma (zamanlayıcı)
- [x] Telegram bildirimleri
- [ ] **Devam ediyor:** Tarihsel referansı hazır veri setinden, projenin kendi biriktirdiği gerçek haber + fiyat verisine taşımak
- [ ] Web paneli / API üzerinden sinyallerin görüntülenmesi
- [ ] Konu sınıflandırmada kural tabanlı yaklaşımdan ML modeline geçiş

## Lisans

Kişisel/deneysel bir projedir; şu an için herhangi bir lisans belirtilmemiştir.