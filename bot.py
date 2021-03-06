# pyTelegramBotAPI imports
import telebot

# Local imports
import config
import markups
bot = telebot.TeleBot(config.TOKEN)




@bot.message_handler(commands = ['start'])
def start(message):
	bot.send_message(message.chat.id, text = "Xush kelibsiz!")
	text = "Jadval juda xira ekan, tiniqrog'i bo'lsa tashlab yuboring iltimos!"
	bot.send_message(message.chat.id, text = text)
@bot.message_handler(commands = ['help'])
def help(message):
	bot.send_message(message.chat.id, text = "Kanikulda mazza qilib dam oling!")

@bot.message_handler(func = lambda message: message.text in markups.days)
def show_table(message):
	day_index = markups.days.index(message.text)
	day = markups.weekdays[day_index]

	text = "<b>{0}</b>\n{1}".format(message.text, day.get_lessons())

	bot.send_message(message.chat.id, text = text, parse_mode = 'HTML')

@bot.message_handler(func = lambda message: True)
def any_text(message):
	bot.send_message(message.chat.id, text = "Sorry, I do not understand you, please use below the menu \xE2\xAC\x87")
