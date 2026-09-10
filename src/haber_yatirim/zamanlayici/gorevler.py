import time, pathlib, sys

yol=pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(yol))

from haber_toplama.haber_cekici import haberleri_isle

while True:
    try:
        haberleri_isle()
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    time.sleep(30*60)