import asyncio
import time
import requests
from pyrogram import Client , filters
from pyrogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from json import loads,dumps
from pyrogram.types import ForceReply
from pyrogram.handlers import MessageHandler
from bs4 import BeautifulSoup
import json

api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = "5897771276:AAHjxn9_D-ar3lHXxfEJAqjdwAdTp01Lw30"
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)

@bot.on_message(filters.command('url') & filters.private & filters.incoming)
async def add(bot, message):
    send = message.reply
    username = message.from_user.username
    await send("Iniciando")
    session = requests.Session()
    login = f'https://eduvirtual.uho.edu.cu/login/index.php'
    resp = requests.post(url=login)
    soup = BeautifulSoup(resp.text, 'html.parser')
    logintoken = soup.find('input', attrs={'name':'logintoken'})['value']
    await send(logintoken)
    username = f'alejandropo@uho.edu.cu'
    password = '1234567m'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
    }
    payload = {'anchor':'', 'logintoken': logintoken, 'username': username, 'password': password}
    resp2 = requests.post(url=login, headers=headers, data=payload)
    print(resp2.text)   

@bot.on_message(filters.command('start') & filters.private & filters.incoming)
async def add(bot, message):
    send = message.reply
    username = message.from_user.username
    await send("Iniciando")
    url = f'https://studio.mogenius.com/user/login'

    data = {'username': 'lastvz02s@gmail.com', 'password': 'Stvz02**'}
    r = requests.post(url=url, data=data)
    print(r.text)
    await send("Terminado")

bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
