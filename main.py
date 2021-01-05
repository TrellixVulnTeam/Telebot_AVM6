import telebot
from telebot import types
from covid19_cases import corona19
import COVID19Py


covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot("1418850232:AAFc44xOkFdbYJyKgA2_CtDM3VGRvFq6uos")


@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_about = types.InlineKeyboardButton(text = 'обо мне',callback_data= 'about')
    markup_inline.add(item_about)
    bot.send_message(message.chat.id, 'Привет!',reply_markup = markup_inline)



@bot.callback_query_handler(func = lambda call:True)
def hello(call):
    if call.data == "about":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_world = types.KeyboardButton('world')
        markup_reply.add(item_world)
        bot.send_message(call.message.chat.id,'Я кабот!', reply_markup = markup_reply)

@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'world':
        location = covid19.getLatest()

        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"
        bot.send_message(message.chat.id,final_message,parse_mode = 'html')

    if get_message_bot == "сша":
        confirmed_count = corona19.confirmed_people("US")
        deaths_count = corona19.deaths_people("US")
        recoverd_count = corona19.recoverd_people("US")
        final_message = (confirmed_count,deaths_count,recoverd_count)
        bot.send_message(message.chat.id, final_message, parse_mode='html')





bot.polling(none_stop=True,interval=0)
