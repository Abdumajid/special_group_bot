
import telebot
import os
from flask import Flask, request

from bot import bot

server = Flask(__name__)



@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://herokuProject_url/bot")
    return "!", 200

