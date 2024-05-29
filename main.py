import telebot

API_TOKEN = '7193508658:AAETbSNrFnGyGthm2Cn7hYpZL-PhxUuGL14'
GROUP_ID = '1386974764'

bot = telebot.TeleBot(API_TOKEN)

@bot.channel_post_handler(func=lambda message: True)
def echo_all(message):
    print('Chanel {} message received: {}'.format(message.chat.title, message.text))
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, 'Error')

bot.polling()
