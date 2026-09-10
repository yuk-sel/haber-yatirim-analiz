import pathlib, sys

yol=pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(yol))

from analiz.korelasyon import istatistik_hesapla
from analiz.duygu_analizi import duygu_analizi
from analiz.konu_siniflandirici import haberi_siniflandirma

def duygu_yonunu_hesapla(duygu_sonucu):
    sonuc_sozlugu= duygu_sonucu[0]
    etiket= sonuc_sozlugu['label']
    skor= sonuc_sozlugu['score']
    if etiket== 'negative':
        return -skor
    elif etiket== 'positive':
        return skor
    else:
        return 0


print(duygu_yonunu_hesapla(duygu_sonucu=[{'label': 'negative', 'score': 0.8413788676261902}]))


def tarihsel_egilimi_normalize_et(ort_degisim):
    normalize = ort_degisim/5
    sinirlar= max(-1, (min(1, normalize)))
    return sinirlar



print(tarihsel_egilimi_normalize_et(ort_degisim=-10))   

def tavsiye_uret(kategori, duygu_sonucu, korelasyon_sonucu):

    if any(kategori.values()):
        duygu_yonu= duygu_yonunu_hesapla(duygu_sonucu)
        tarihsel_egilim= tarihsel_egilimi_normalize_et(korelasyon_sonucu['GOLD_CHANGE_mean'])
        skor= 0.5 * duygu_yonu + 0.5 * tarihsel_egilim
        if skor < -0.3:
            etiket="Dikkatli olunmalı, düşüş eğilimi var"
        elif skor > 0.3:
            etiket= "Olumlu, yükseliş eğilimi var"
        else: 
            etiket= 'Belirsiz'
        return {'skor': skor, 'etiket': etiket}
    else:
        return {'skor': 0, 'etiket': 'İlgisiz haber, tavsiye yok'}

print(tavsiye_uret(
    kategori={'savas': False, 'yaptirim': False, 'maden': False},
    duygu_sonucu=[{'label': 'negative', 'score': 0.84}],
    korelasyon_sonucu={'GOLD_CHANGE_mean': -0.59, 'GOLD_CHANGE_pozitif_oran': 0.27, 'GOLD_CHANGE_ornek_Sayisi': 11}
)
)