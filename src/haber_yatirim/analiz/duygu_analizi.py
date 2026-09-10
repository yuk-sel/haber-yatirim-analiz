from transformers import pipeline

pipe = pipeline("sentiment-analysis", model="ProsusAI/finbert")


def duygu_analizi(metin):
    try:
        analiz_sonucu= pipe(metin)
        return analiz_sonucu
    except Exception as e:
        print(f"Duygu analizi sırasında bir hata oluştu: {e}")
        return None  

cumle="Russia's attacks caused damage in Ukraine"
print(duygu_analizi(cumle))