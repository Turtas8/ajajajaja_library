import telebot
from telebot import types

bot = telebot.TeleBot("5629208779:AAGwBpAN5L0jjAxpLNAUEaDJZSOJIch96Dk")

pay = '401643678:TEST:18e9d969-e341-43f5-a6cd-059335e0af71'


@bot.message_handler(commands=['start'])
def send_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton('Перейти на сайт')
    item2 = types.KeyboardButton('Поддержка')
    item3 = types.KeyboardButton('Комплимент')
    item4 = types.KeyboardButton('Премиум')
    markup.add(item1, item2, item3, item4)

    privet = 'Вас приветствует AJAJAJAJA_Company\nВыберите команду: '
    bot.send_message(message.chat.id, privet, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Перейти на сайт':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('📖📖📖📖📖📖📖📖📖📖', 'http://34.73.108.209'))
            bot.send_message(message.chat.id, 'Окунитесь в мир книг вместе с Ajajajaja_Library:', reply_markup=markup)

        elif message.text == 'Поддержка':
            bot.send_message(message.chat.id, 'Можете обратиться к нашему партнёру @Personwithoutnameforlife')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Оставить контакт', request_contact=True)
            back = types.KeyboardButton('Назад')
            markup.add(item1, back)
            bot.send_message(message.chat.id, 'Или можете оставить контакт, мы с вами свяжемся', reply_markup=markup)

        elif message.text == 'Комплимент':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Красавчики ♥️')
            back = types.KeyboardButton('Назад')
            markup.add(item1, back)
            bot.send_message(message.chat.id, 'Ты словно книга для книжного червя <3', reply_markup=markup)

        elif message.text == 'Премиум':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item = types.KeyboardButton('Почкой??')
            back = types.KeyboardButton('Назад')
            markup.add(item, back)
            kard = ''
            bot.send_message(message.chat.id, f"Или картой ", reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Перейти на сайт')
            item2 = types.KeyboardButton('Поддержка')
            item3 = types.KeyboardButton('Комплимент')
            item4 = types.KeyboardButton('Премиум')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Чуть-чуть назад', reply_markup=markup)


bot.polling(none_stop=True)