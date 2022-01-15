import telebot


bot = telebot.TeleBot('5093016536:AAE7Bi26hVrUTLdTSaaM5q9H_SFX3tx-Tlo')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    if message.chat.type == 'private':

        if message.text == '/start':
            bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}!\n'
                                                   f'Меня зовут Лем, и я был создан, чтобы делать чаты более интересными. '
                                                   f'Чтобы узнать, что я умею, ты можешь воспользоваться командой "/help".'
                                                   f' Либо просто добавь меня в свой чат, а там я уже расскажу всем о своих'
                                                   f'способностях!')

        elif message.text == '/help':
            bot.send_message(message.from_user.id, 'Позже здесь будет список команд, которые я умею выполнять. А пока что'
                                                   ' я не умею ничего...')

    elif message.chat.type == 'group':

        if message.text == '/start':
            bot.send_message(message.chat.id, 'Кринж, чел, ты в муте... И все остальные, кто сидит в этой беседе, '
                                              'тоже в пожизненном муте.')

        elif message.text == '/help':
            bot.send_message(message.chat.i, 'Позже здесь будет список команд, которые я умею выполнять. А пока что'
                                             ' я не умею ничего...')


bot.infinity_polling()
