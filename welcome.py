import telebot


# Replace ‘YOUR_API_TOKEN’ with the API token you received from the BotFather
API_TOKEN = "7352121940:AAFZDHb_JXJzglBK2k8V53_ZmQXBux4EfWM"

badwords = open("badwords.txt", "r", encoding="utf-8")
badword_list = badwords.read().split("\n")
badwords.close()

bot = telebot.TeleBot(API_TOKEN)

# Define a command handler
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Welcome to this channel! Type /info to get more information.")

@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(message, "I am a Guard Bot that find the spam words and warn to the clients!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text in badword_list:
        bot.reply_to(message, "Warning: Stop! This is spam!")

# Start the bot
bot.polling()