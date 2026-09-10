from deep_translator import GoogleTranslator
import time

def ingilizceye_cevir(metin):
    try:
        cevrilen_metin = GoogleTranslator(source='auto', target='en').translate(metin)
        time.sleep(1)
        return cevrilen_metin
    except Exception as e:
        print(f"Çeviri sırasında bir hata oluştu: {e}")
        return metin  # Hata durumunda orijinal metni döndür

metin=("Türkiye'nin jeopolitik riskleri, altın fiyatları üzerinde önemli bir etkiye sahiptir. ")
print(ingilizceye_cevir(metin))