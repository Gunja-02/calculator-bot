import telebot

Token = "7902920407:AAHTKeFaYZ6WsHmHr4CkfZqD7SZwSM4PH0A"

bot = telebot.TeleBot(Token)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Welcome to my Calculator")
    
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, """Available Commands:
    /start - Welcome Message
    /help - List of commands
    Send me any math expression, and I'll calculate it for you!
    """)

@bot.message_handler(commands=['about'])
def about_command(message):
    bot.reply_to(message, """Bot Info:
    /Name: Calculator Bot
    /Version: 1.0
    /Author: Gunjan Chaudhari
    Description: A bot that evaluates mathematical expressions.
    """)

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        result = eval(message.text)
        bot.reply_to(message, f"Result: {result}")
    except:
        bot.reply_to(message, "Sorry, I couldn't calculate that. Please send a valid expression.")

print("Bot is running...")
bot.polling()

