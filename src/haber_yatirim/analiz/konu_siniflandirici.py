import re
import os, sys, pathlib

yol=pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(yol))
from analiz.kok_bulma import kok_bul

def temizle_metin(metin):
    # Metni küçük harfe çevir
    metin = metin.lower()
    
    # Noktalama işaretlerini kaldır
    metin = re.sub(r'[^\w\s]', '', metin)
    
    # Gereksiz boşlukları kaldır
    metin = re.sub(r'\s+', ' ', metin).strip()
    
    return metin

#verisetim ingilzce olduğu  için sınıflandırmada ingilizce kelimler kullandım.
#re ile kelimleri ararken kelimenin tam olarak eşleşmesini sağlamak için \b (word boundary) kullandım Bu sayede "war" kelimesi "warfare" gibi kelimelerle karışmayacak.

def haberi_siniflandirma(metin):
    metin = temizle_metin(metin)
    metin_kokleri= kok_bul(metin)

    savas_kelimeleri=["war", "invasion", "conflict", "battle", "military", "troops", "attack", "defense", "casualties", "occupation", "missile", "weapon", "weapons", "militant", "militants", "airstrike", "sabotage", "raid", "raids", "bomb", "bombing", "bombardment", "insurgency", "insurgent", "rebel", "rebels", "terrorist", "terrorism", "combat", "siege", "offensive", "mobilization", "deployment", "artillery", "drone", "warfare", "hostilities", "skirmish", "ambush", "assault", "incursion", "shelling", "explosion", "wounded", "killed", "soldier", "soldiers", "army", "navy", "warplane", "tank", "warship", "ballistic", "coup", "uprising", "rebellion", "unrest", "clashes", "escalation", "evacuation", "refugee", "refugees", "massacre", "warzone", "ceasefire", "armistice", "aggression", "retaliation", "counterattack", "annexation", "blockade", "mercenary", "mercenaries", "paramilitary"]
    cok_kelime_savas=["war declared", "military conflict", "armed forces", "military operation", "air strike", "missile strike", "military strike", "armed conflict", "military intervention", "military offensive", "armed attack", "military engagement", "armed struggle", "military campaign", "armed resistance", "military escalation", "armed insurrection", "military offensive", "armed conflict", "war crimes", "ground offensive", "border clash", "military operation", "no-fly zone", "declared war", "peace talks", "troop withdrawal", "military base"]
    yaptirim_kelimeleri=["sanctions", "embargo", "restrictions", "penalties", "embargo", "blacklist", "boycott", "tariff", "tariffs", "freeze", "frozen", "blockade", "divestment", "seizure", "confiscation"]
    cok_kelime_yaptirim=["asset freeze", "frozen assets", "export ban", "import ban", "export restrictions", "import restrictions", "travel ban", "arms embargo", "oil embargo", "economic blockade", "financial blockade", "secondary sanctions", "sanctions package", "sanctions regime", "trade war", "punitive tariffs", "sanctions imposed", "economic sanctions", "trade restrictions", "financial penalties", "trade ban", "economic measures", "financial sanctions", "international sanctions", "trade embargo", "economic restrictions"]
    maden_kelimeleri=["mine", "miner", "miners", "bullion", "smelting", "refinery", "deposit", "reserves", "excavation", "drilling", "lithium", "uranium", "zinc", "nickel", "aluminum", "cobalt", "bauxite", "platinum", "palladium", "tungsten", "titanium", "mining", "ore", "extraction", "quarry", "minerals", "coal", "gold", "silver", "copper", "iron"]
    cok_kelime_maden=["rare earth elements", "precious metals", "gold reserves", "mining operation", "open-pit mine"]
    savas_kelime_kok=[]
    yaptirim_kelime_kok=[]
    maden_kelime_kok=[]

    for savas_kelime in savas_kelimeleri:
        savas_kelime=kok_bul(savas_kelime)[0]
        savas_kelime_kok.append(savas_kelime)

    for yaptirim_kelime in yaptirim_kelimeleri:
        yaptirim_kelime=kok_bul(yaptirim_kelime)[0]
        yaptirim_kelime_kok.append(yaptirim_kelime)

    for maden_kelime in maden_kelimeleri:
        maden_kelime=kok_bul(maden_kelime)[0]
        maden_kelime_kok.append(maden_kelime)


    mevcut_tahmin={"savas":False,"yaptirim": False,"maden":False}

    for savas_kelime in savas_kelime_kok:
        if savas_kelime in metin_kokleri:
            mevcut_tahmin["savas"]=True

    for yaptirim_kelime in yaptirim_kelime_kok:
        if yaptirim_kelime in metin_kokleri:
            mevcut_tahmin["yaptirim"]=True

    for maden_kelime in maden_kelime_kok:
        if maden_kelime in metin_kokleri:
            mevcut_tahmin["maden"]=True

    for savas_kelime in cok_kelime_savas:
        if re.search(r'\b' + re.escape(savas_kelime) + r'\b', metin):
            mevcut_tahmin["savas"]=True

    for yaptirim_kelime in cok_kelime_yaptirim:
        if re.search(r'\b' + re.escape(yaptirim_kelime) + r'\b', metin):
            mevcut_tahmin["yaptirim"]=True

    for maden_kelime in cok_kelime_maden:
        if re.search(r'\b' + re.escape(maden_kelime) + r'\b', metin):
            mevcut_tahmin["maden"]=True

    return mevcut_tahmin

'''#test ettiiiimm
cumle= "New iPhone attacks battled today"
print(kok_bul(cumle))
print(haberi_siniflandirma(cumle))
'''