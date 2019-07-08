import telebot;
import pyowm
city = ''
owm = pyowm.OWM('')
bot = telebot.TeleBot('');
@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Введите город, в котором хотите узнать погоду")
@bot.message_handler(content_types=['text'])
def getCity(message):
    global city
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()

        temperature = w.get_temperature('celsius')['temp']
        bot.send_message(message.from_user.id, "Температура - " + str(temperature) + " по Цельсию")
        bot.send_message(message.from_user.id, "Также, в указанном городе " + w.get_detailed_status())
    except Exception:
        bot.send_message(message.from_user.id, "Такого города нет!")
bot.polling(none_stop=True, interval=0)