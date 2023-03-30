import telebot

bot = telebot.TeleBot('5581903981:AAECHJkCEjfrZUoRJj7SGG9RJno_dJz1FmM')  # ініціалізація бота з токеном
ADMIN_CHAT_ID = '333482243'
last_user = None  # зберігає ідентифікатор останнього користувача

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Вітаю! Я бот для анонімних повідомлень. Надішліть мені своє повідомлення.")

@bot.message_handler(content_types=['text'])
def echo(message):
    global last_user  # оголошуємо змінну, щоб вона була глобальною і можна було змінювати її значення

    user_message = message.text
    if user_message:
        if last_user is None:
            bot.send_message(message.chat.id, "Ваше анонімне повідомлення надіслано!")
        else:
            bot.send_message(message.chat.id, "Вашу відповідь надіслано анонімно!")

        # Надсилання повідомлення адміністратору про нове повідомлення або відповідь
        if last_user is None:
            admin_message = f"Нове анонімне повідомлення: {user_message}"
        else:
            admin_message = f"Відповідь на анонімне повідомлення від користувача з ідентифікатором {last_user}: {user_message}"
        bot.send_message(ADMIN_CHAT_ID, admin_message)

        # Зберігаємо ідентифікатор останнього користувача
        last_user = message.chat.id

    else:
        bot.send_message(message.chat.id, "Надішліть мені текстове повідомлення, будь ласка.")

bot.polling(none_stop=True)
