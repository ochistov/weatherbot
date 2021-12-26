import requests
import telebot
import time


def weathernow():
    s_city = "Moscow,RU"
    city_id = 524901
    appid = '8336e2a69cce794ec6b7d2d028c63b49'
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

        data = res.json()
        return f"Сейчас в Москве {data['main']['temp']}, ощущается как {data['main']['feels_like']} \nМаксимальная температура: {data['main']['temp_max']}\nМинимальная температура: {data['main']['temp_min']} "
    except Exception as e:
        pass


bot = telebot.TeleBot('5092808962:AAG0hB5979ojSnXfraChzB2L7pJkV5aW1E4')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         "Привет, чтобы узнать погоду, напиши всё, что угодно")
    else:
        bot.send_message(message.from_user.id, weathernow())


# while True:
#     bot.send_message(chat_id="-1001710200731", text=weathernow())
#     time.sleep(1)

bot.polling(none_stop=True, interval=0)
