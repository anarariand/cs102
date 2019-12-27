import telebot


access_token = "653582719:AAHFghkyK793qPntTnVaVWWYPMsSTlBtAVw"
telegram.apihelper.proxy = {'https': 'https://200.69.77.13:4145'}

# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)


# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message: str) -> None:
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling()
