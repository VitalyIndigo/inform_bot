from telebot import TeleBot, types
import config
import random

bot = TeleBot(config.TOKEN)

def create_random_message_keyboard ():
    kb = types.InlineKeyboardMarkup()
    random_org_site_button = types.InlineKeyboardButton (text = 'RANDOM', url = 'https://www.random.org/') # кнопка №1
    yandex_maps_site_button = types.InlineKeyboardButton (text = 'YANDEX maps', url = 'https://yandex.ru/maps/50/perm/?ll=56.229441%2C58.010454&z=12') # кнопка №2
    sportbox_site_button = types.InlineKeyboardButton (text = 'SPORTBOX', url = 'https://news.sportbox.ru/') # кнопка №3
    kb.add (random_org_site_button)
    kb.add (yandex_maps_site_button)
    kb.add (sportbox_site_button) # отображение кнопок в ряд
    # kb.row (random_org_site_button, yandex_maps_site_button, sportbox_site_button)# отображение кнопок в строчку
    return kb

@bot.message_handler(commands = ['random'])
def handle_command_random (message: types.Message):
    kb = create_random_message_keyboard ()
    bot.send_message (message.chat.id, text = 'Выберите сайт', reply_markup = kb)


def hendle_user_name (message: types.Message):
    if message.content_type != 'text':
        bot.send_message (chat_id = message.chat.id, text = 'Неправильная форма, пожалуйста, напишите Ваше имя, например, Виталий Петров')
        return 
    bot.register_next_step_handler (message = message, callback = hendle_user_name)
    name = message.text
    bot.send_message (chat_id = message.chat.id, text = 'Все ОК, продолжаем')


def hendle_user_age (message: types.Message):
    pass # такая же обработка, как в hendle_user_name


@bot.message_handler(commands = ['survay'])
def handle_survay (message: types.Message):
    bot.send_message (chat_id = message.chat.id, text = 'Добро пожаловать, пожалуйста, напишите Ваше имя, например, Виталий Петров')
    bot.register_next_step_handler (message = message, callback = hendle_user_name)


@bot.message_handler(commands = ['start'])
def handle_commands_start (message: types.Message):
    bot.send_message (message.chat.id, text = '<b>Добро пожаловать в информационный бот</b>', parse_mode='html')

@bot.message_handler(commands = ['reference'])
def handle_commands_reference (message: types.Message):
    bot.send_message (message.chat.id, text = 'Описание бота')

@bot.message_handler(commands = ['wisdom'])
def handle_commands_reference (message: types.Message):
    bot.send_message (message.chat.id, text = 'Мудрость дня')

@bot.message_handler(content_types = ['sticker'])
def handle_sticker (message: types.Message):
    bot.send_message (chat_id = message.chat.id, text = 'Прикольный стикер', reply_to_message_id = message.id)

@bot.message_handler(content_types = ['photo'])
def handle_photo (message: types.Message):
    bot.send_message (chat_id = message.chat.id, text = 'Какое классное фото!', reply_to_message_id = message.id)

@bot.message_handler()
def weather_bot (message: types.Message):
    text = message.text
    if 'привет' in text.lower() or 'добрый' in text.lower() or 'здрав' in text.lower():
        text = 'Здравствуйте! Я готов к работе'
    elif 'прогноз погоды' in text.lower():
        text = 'Актуальный прогноз погоды на сайте gismeteo.ru'
    elif 'новости' in text.lower():
        text = 'Самые свежие новости на сайте news.mail.ru'
    elif 'курс валют' in text.lower():
        text = 'Официальный курс валют на сайте ru.myfin.by'
    elif 'еще' in text.lower():
        text = 'Остались еще вопросы? Поможет yandex.ru'
    elif 'спасибо' in text.lower() or 'благодар' in text.lower():
        text = 'Пожалуйста! Обращайтесь!'
    else:
        text = 'Неверная команда, попробуйте еще раз'

    bot.send_message (message.chat.id, text)

if __name__ == '__main__':
    bot.infinity_polling (skip_pending=True)

