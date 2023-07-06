import telebot
from randstaff import RandStuff
import time

TOKEN = "6349040347:AAG_CFsr-_wwL4SLPE1iq9w4ue9ygCHrBOI"
bot = telebot.TeleBot(token=TOKEN)
chanell = '@tipo_anekdoty'
randstaff = RandStuff()


while True:
    text = randstaff.generate_random_joke()
    send = bot.send_message(chat_id=chanell, text=text)
    print(f'Сообщение отправлено: {send.text}')
    time.sleep(1800)