import telebot
from telebot import types
from time import sleep

bot = telebot.TeleBot('')

@bot.message_handler(commands=['watching'])
def watching_on_right_now(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAELQJZncDgW6rMwnR-zTyhcI0YNYVPsRwACrhQAAo4n0EqxFZIn-u6dajYE")
    bot.send_message(message.chat.id, "Первая серия, как создать сервер в Minecraft (плагины).\nРекомендую его посмотреть! 👍🏻\nСсылка: rutube.ru/video/74b80b7848c5cb44679b066d892101ce")

@bot.message_handler(commands=['support'])
def questions_for_me(message):
    audio = open(r'C:/Users/dmitr/Desktop/TeleBot-1/Навигация по тому, как и куда обратиться за помощью.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    bot.send_message(message.chat.id, "Номер телефона: (8)+79539036130\nНаписать во VKонтакте: vk.com/piroschock.frilance.work\nE-Mail Почта: dizelano.53.usinger.917@internet.ru")

@bot.message_handler(commands=['start'])
def welcome_to_my_chat(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAELP6Bnb_9SLqbjzlL0sDnW3pmgdKikjAACSQkAAnlc4gk-iCYrsVN-eTYE")
    bot.send_message(message.chat.id, 'Здравствуй, меня зовут Risovick-бот! 🥰\nЯ ассистент создателя данного Telegram бота, могу помочь вам вступить в приватный канал\nмоего курса по созданию серверов в Minecraft...')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("1. Да, я присоединюсь!")
    button2 = types.KeyboardButton("2. Нет, спасибо.")
    button3 = types.KeyboardButton("3. Мой аккаунт.")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Переслать вам ссылочку для вступления?", reply_markup=markup)
    # sleep(180)
    
    bot.send_photo(message.chat.id, photo="https://i.ytimg.com/vi/WoJwJPFA9us/maxresdefault.jpg")
    markup = types.InlineKeyboardMarkup()
    torrent1 = types.InlineKeyboardButton("Другие мои социальные ресурсы!", url="https://piroschock-official-8549.taplink.ws", callback_data='1')
    torrent2 = types.InlineKeyboardButton("Информация о боте.", url="https://telegra.ph/Informaciya-o-Telegram-bote-12-28", callback_data='2')
    torrent3 = types.InlineKeyboardButton("Переходник на Telegram канал.", url="https://t.me/rise_channel15", callback_data='3')
    torrent4 = types.InlineKeyboardButton("Поделиться с друзьями / коллегами.", url="https://t.me/+JJT-Do4n62AwZGMy", callback_data='4')
    markup.add(torrent1, torrent2, torrent3, torrent4)
    bot.send_message(message.chat.id, "Не забудьте подписаться на мои социальные сети:", reply_markup=markup)
    
@bot.message_handler(content_types="text")
def younger(message):
    if message.text == ("1. Да, я присоединюсь!"):
        bot.send_video(message.chat.id, "https://img1.picmix.com/output/stamp/thumb/6/7/9/0/2530976_4ce38.gif", None, 'Text')
        bot.send_message(message.chat.id, "Отлично, +1 участник! 😘\nСсылка: t.me/+bs-y9MgUgJA5N2U6")
    elif message.text == ("2. Нет, спасибо."):
        bot.send_video(message.chat.id, 'https://konstruktortestov.ru/files/1ef0/4530/8786/6973/81cc/a86b/e339/2fda/2335528862.gif', None, 'Text')
        bot.send_message(message.chat.id, "Эх... 😭\nЖаль конечно, но ладно.\nУдачного вам дня!")
    elif message.text == ("3. Мой аккаунт."):
        bot.send_video(message.chat.id, "https://i.imgur.com/WOCsQ8b.gif", None, 'Text')
        bot.send_message(message.chat.id, "Собираю все данные из вашего профиля Telegram!")
        sleep(3)
        bot.send_message(message.chat.id, "Пожалуйста, подождите от 5-10 секунд.")
        sleep(7)
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username
        bot.send_message(message.chat.id, f"Вот, что я смог найти из информации:\n *ID вашего аккаунта: {user_id}\n *Имя пользователя: {first_name}\n *Фамилия пользователя: {last_name}\n *Указанный ник(@): @{username}")

bot.infinity_polling()