import pandas as pd

df=pd.read_csv('veri\\ham\\Gold-Silver-GeopoliticalRisk_HistoricalData.csv')
print(df.head())
print(f"Sütunlar: {(df.columns)}")
altin_fiyat=df['GOLD_CHANGE_%']
gpr=df['GPRD']
print(f"Altın fiyatları: {altin_fiyat.head()}")
print(f"Jeopolitik risk endeksi: {gpr.head()}")

korelasyon=altin_fiyat.corr(gpr)
print(f"Korelasyon: {korelasyon}")

pct_ile_gprd=gpr.pct_change()
diff_ile_gprd=gpr.diff()

korelasyon_diff=altin_fiyat.corr(diff_ile_gprd)
print(f"Korelasyon (diff ile): {korelasyon_diff}")

korelasyon_pct=altin_fiyat.corr(pct_ile_gprd)
print(f"Korelasyon (pct ile): {korelasyon_pct}")

print(len(df))
print(f"Altın fiyatları ortalaması: {df['GOLD_CHANGE_%'].mean()}")

olayli = df[df['EVENT'].notna()]
print(len(olayli))
print(f"Altın fiyatları ortalaması: {olayli['GOLD_CHANGE_%'].mean()}")

print(olayli[['EVENT', 'GOLD_CHANGE_%']])

print()