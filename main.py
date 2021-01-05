import COVID19Py
import telebot
from covid19_cases import corona19
from telebot import types
from threading import Thread
covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot("1418850232:AAFc44xOkFdbYJyKgA2_CtDM3VGRvFq6uos")


@bot.message_handler(commands=['start'])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_about = types.InlineKeyboardButton(text = 'Обо мне ',callback_data= 'about')
    markup_inline.add(item_about)
    bot.send_message(message.chat.id, 'Привет!\n'
                                      'Введи страну где ты живешь\n'
                                      'Чтобы узнать больше нажми кнопку!',reply_markup = markup_inline)



@bot.callback_query_handler(func = lambda call:True)
def hello(call):
    if call.data == "about":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_world = types.KeyboardButton('world')
        markup_reply.add(item_world)
        bot.send_message(call.message.chat.id,'<b>Я кабот!</b>\n'
                                              'Могу рассказать тебе про статистику коронавируса🦠\n'
                                              '<u>Для этого просто напиши страну, про которую хочешь узнать</u>🇷🇺\n'
                                              'Или нажми на кнопку ⬇️', reply_markup = markup_reply, parse_mode = 'html')




@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'world':
        location = covid19.getLatest()

        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"
        bot.send_message(message.chat.id,final_message,parse_mode = 'html')

    if get_message_bot == "Сша":
        confirmed_count = corona19.confirmed_people("US")
        deaths_count = corona19.deaths_people("US")
        recoverd_count = corona19.recoverd_people("US")
        final_message = (f"<b>Данные по США</b>\n"
                         f"<u>Заболевших: </u>{confirmed_count}\n"
                         f"<u>Погибли: </u>{deaths_count}\n"
                         f"<u>Выздоровили: </u>{recoverd_count}")
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    if get_message_bot == "Россия":
        confirmed_count = corona19.confirmed_people("Russia")
        deaths_count = corona19.deaths_people("Russia")
        recoverd_count = corona19.recoverd_people("Russia")
        final_message = (f"<b>Данные по России</b>\n"
                         f"<u>Заболевших: </u>{confirmed_count}\n"
                         f"<u>Погибли: </u>{deaths_count}\n"
                         f"<u>Выздоровили: </u>{recoverd_count}")
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    if get_message_bot == "Италия":
        confirmed_count = corona19.confirmed_people("Italy")
        deaths_count = corona19.deaths_people("Italy")
        recoverd_count = corona19.recoverd_people("Italy")
        final_message = (f"<b>Данные по Италии</b>\n"
                         f"<u>Заболевших: </u>{confirmed_count}\n"
                         f"<u>Погибли: </u>{deaths_count}\n"
                         f"<u>Выздоровили: </u>{recoverd_count}")
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    if get_message_bot == "Украина ":
        confirmed_count = corona19.confirmed_people("Ukraine")
        deaths_count = corona19.deaths_people("Ukraine")
        recoverd_count = corona19.recoverd_people("Ukraine")
        final_message = (f"<b>Данные по Украине</b>\n"
                            f"<u>Заболевших: </u>{confirmed_count}\n"
                            f"<u>Погибли: </u>{deaths_count}\n"
                            f"<u>Выздоровили: </u>{recoverd_count}")
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    if get_message_bot == "Франция":
        confirmed_count = corona19.confirmed_people("France")
        deaths_count = corona19.deaths_people("France")
        recoverd_count = corona19.recoverd_people("France")
        final_message = (f"<b>Данные по Франции</b>\n"
                         f"<u>Заболевших: </u>{confirmed_count}\n"
                         f"<u>Погибли: </u>{deaths_count}\n"
                         f"<u>Выздоровили: </u>{recoverd_count}")
        bot.send_message(message.chat.id, final_message, parse_mode='html')

    if get_message_bot == "Германия":
        confirmed_count = corona19.confirmed_people("Germany")
        deaths_count = corona19.deaths_people("Germany")
        recoverd_count = corona19.recoverd_people("Germany")
        final_message = (f"<b>Данные по Германии</b>\n"
                         f"<u>Заболевших: </u>{confirmed_count}\n"
                         f"<u>Погибли: </u>{deaths_count}\n"
                         f"<u>Выздоровили: </u>{recoverd_count}")
        bot.send_message(message.chat.id, final_message, parse_mode='html')









bot.polling(none_stop=True,interval=0)
