import pandas as pd
import pathlib
yol=pathlib.Path(__file__).resolve().parent.parent.parent.parent

def veri_yukle():
    dosya= yol/"veri" / "ham" /"Gold-Silver-GeopoliticalRisk_HistoricalData.csv"
    return pd.read_csv(dosya)

df= veri_yukle()


print(df.head())
print(f"df info: {df.info()}")
print(f"df boyutu: {df.shape}")

def nan_temizle(df):
    df = df.dropna(subset=['EVENT'])
    return df

df= nan_temizle(df)


def istatistik_hesapla(df):
    istatistik={}
    istatistik['GOLD_CHANGE_max'] = df['GOLD_CHANGE_%'].max()
    istatistik['GOLD_CHANGE_min'] = df['GOLD_CHANGE_%'].min()
    istatistik['GOLD_CHANGE_mean'] = df['GOLD_CHANGE_%'].mean()
    istatistik['GOLD_CHANGE_median'] = df['GOLD_CHANGE_%'].median()
    istatistik['GOLD_CHANGE_std'] = df['GOLD_CHANGE_%'].std()
    istatistik['GOLD_CHANGE_pozitif_Sayisi'] = (df['GOLD_CHANGE_%'] > 0).sum()
    istatistik['GOLD_CHANGE_negatif_Sayisi'] = (df['GOLD_CHANGE_%'] < 0).sum()
    istatistik['GOLD_CHANGE_ornek_Sayisi'] = len(df)
    istatistik['GOLD_CHANGE_pozitif_oran'] = istatistik['GOLD_CHANGE_pozitif_Sayisi'] / len(df['GOLD_CHANGE_%'])
    istatistik['sifir']= (df['GOLD_CHANGE_%'] == 0).sum()
    return istatistik

print(istatistik_hesapla(df))


'''bak= list(df["GOLD_CHANGE_%"])

for i in range(len(bak)):
    if bak[i]==0:
        print(df.iloc[i])'''
