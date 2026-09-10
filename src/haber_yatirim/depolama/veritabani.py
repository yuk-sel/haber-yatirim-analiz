import sqlite3

def veritabani_baglantisi():
    conn=sqlite3.connect("veri/takip.db")
    return conn
def tablo_olustur(conn):
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS gorulmus_haberler (id INTEGER PRIMARY KEY AUTOINCREMENT, baslik TEXT, link TEXT, guid TEXT, kaynak TEXT, gorulme_zamani TIMESTAMP DEFAULT CURRENT_TIMESTAMP, savas INTEGER, yaptirim INTEGER, maden INTEGER, duygu_etiketi TEXT, duygu_skoru REAL, tavsiye_skoru REAL, tavsiye_etiketi TEXT)''')
    conn.commit()

def haber_var_mi(conn, guid):
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM gorulmus_haberler WHERE guid=?", (guid,))
    return cursor.fetchone() is not None

def haber_kaydet(conn, baslik, link, guid, kaynak, kategori, analiz, tavsiye):
    cursor=conn.cursor()
    yaptirim= kategori['yaptirim']
    savas= kategori['savas']
    maden= kategori['maden']
    duygu_etiketi= analiz[0]['label']
    duygu_skoru= analiz[0]['score']
    tavsiye_etiketi=tavsiye['etiket']
    tavsiye_skoru=tavsiye['skor']
    cursor.execute("INSERT OR IGNORE INTO gorulmus_haberler (baslik, link, guid, kaynak, yaptirim, savas, maden, duygu_etiketi, duygu_skoru, tavsiye_etiketi, tavsiye_skoru) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (baslik, link, guid, kaynak, yaptirim, savas, maden, duygu_etiketi, duygu_skoru, tavsiye_etiketi, tavsiye_skoru))
    conn.commit()

tablo_olustur(veritabani_baglantisi())
