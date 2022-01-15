import telebot


bot = telebot.TeleBot('5093016536:AAE7Bi26hVrUTLdTSaaM5q9H_SFX3tx-Tlo')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Приветствую, {message.from_user.first_name}!\n'
                                           f'Меня зовут Лем, и я был создан, чтобы наводить порядок в чатах.')


bot.infinity_polling()
