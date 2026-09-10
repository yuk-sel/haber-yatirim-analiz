import os, requests, pathlib
from dotenv import load_dotenv

yol=pathlib.Path(__file__).resolve().parent.parent.parent.parent
env_yolu= yol / ".env"
load_dotenv(dotenv_path=env_yolu)
os.getenv('TELEGRAM_BOT_TOKEN')
os.getenv('TELEGRAM_CHAT_ID')

def bildirim_gonder(mesaj):
    url=f"https://api.telegram.org/bot8861642644:AAFS5xJzz6Vsk-Y9lIwoHfbQ52h5z6lMeFk/sendMessage"
    cevap=requests.get(url, params={'chat_id': 8902329366, 'text': mesaj})
    print(cevap.status_code)
    print(cevap.text)

bildirim_gonder("testinkoo")

