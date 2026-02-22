import telebot

TOKEN = "8418742735:AAFTjzs4atT2SBNQRF8L90IJHURqkq_IhDo"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "استلمت رسالتك: " + message.text)

print("Bot is running...")
bot.infinity_polling()
