import feedparser
import os, sys, pathlib

yol=pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(yol))
from analiz.konu_siniflandirici import haberi_siniflandirma
from depolama.veritabani import veritabani_baglantisi, haber_var_mi, haber_kaydet
from analiz.ceviri import ingilizceye_cevir
from analiz.kok_bulma import kok_bul
from analiz.duygu_analizi import duygu_analizi
from sinyaller.tavsiye_uretici import tavsiye_uret
from analiz.korelasyon import nan_temizle, istatistik_hesapla, veri_yukle
from sinyaller.bildirim_gonder import bildirim_gonder

df_korelasyon= veri_yukle()
df_korelasyon= nan_temizle(df_korelasyon)
korelasyon_sonucu= istatistik_hesapla(df_korelasyon)

url ="http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/uk_politics/rss.xml"
url2 = "https://www.aa.com.tr/tr/rss/default?cat=dunya"

urller=[url,url2]
conn = veritabani_baglantisi()

def haberleri_isle():
    for url in urller:
        akis = feedparser.parse(url)
        for haber in akis.entries:
            baslik = haber.title
            link = haber.link
            guid = haber.id
            kaynak = url  # veya haber.source gibi bir değer
            if not haber_var_mi(conn, guid):
                cevir= ingilizceye_cevir(baslik)
                kategori=haberi_siniflandirma(cevir)
                analiz= duygu_analizi(cevir)
                tavsiye= tavsiye_uret(kategori, analiz, korelasyon_sonucu)

                if tavsiye['etiket'] not in ['İlgisiz haber, tavsiye yok', 'Belirsiz']:
                    ilgili_kategoriler=[]
                    for anahtar, deger in kategori.items():       
                        if deger:
                            ilgili_kategoriler.append(anahtar)
                            
                    mesaj= f" '{baslik}' adlı bir haber yayınlandı. Bu haber {', '.join(ilgili_kategoriler)} ile ilgili olabilir. {tavsiye['etiket']} ihtimali var. "
                    bildirim_gonder(mesaj)

                haber_kaydet(conn, baslik, link, guid, kaynak, kategori, analiz, tavsiye)

                print(f"Haber kaydedildi: {baslik} - Kategori: {kategori} - Analiz: {analiz} - Tavsiye: {tavsiye}")

            else:
                print(f"Haber zaten mevcut: {baslik}")

if __name__ == "__main__":
    haberleri_isle()