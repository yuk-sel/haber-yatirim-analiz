import os, requests, pathlib
from dotenv import load_dotenv

yol=pathlib.Path(__file__).resolve().parent.parent.parent.parent
env_yolu= yol / ".env"
load_dotenv(dotenv_path=env_yolu)
bot_token=os.getenv('TELEGRAM_BOT_TOKEN')
chat_id= os.getenv('TELEGRAM_CHAT_ID')

def bildirim_gonder(mesaj):
    url=f"https://api.telegram.org/bot{bot_token}/sendMessage"
    cevap=requests.get(url, params={'chat_id': chat_id, 'text': mesaj})
    print(cevap.status_code)
    print(cevap.text)

bildirim_gonder("testinkoo")

