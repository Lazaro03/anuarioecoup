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
from requests import Session
from bs4 import BeautifulSoup as s
import openai
api_id = 9910861
api_hash = "86e927460a8998ba6d84e9c13acfda95"
bot_token = "5999344767:AAErW_Ejrlhv4X-GocxLdXxdRX__JNenVyc"
bot = Client("bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
openai.api_key = bot_token

@bot.on_message(filters.command('url') & filters.private & filters.incoming)
async def add(bot, message):
    send = message.reply
    username = message.from_user.username
    await send("Iniciando")
    session = requests.Session()
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'}
    url = f"https://santiago.uo.edu.cu/index.php/stgo/login/signIn"
  #  resp = session.get(url, headers=header)
  #  soup = s(resp.text,'html.parser')
  #  ltoken = soup.find("input", attrs={"name": "logintoken"})['value']
  #  await send(ltoken)
    data = {
           # "anchor": "",
           # "logintoken": ltoken,
            "username": "tvz02",
            "password": "stvz02**"
        #    "rememberusername": 1,
        }
    resp2 = session.post(url, headers=header, data=data)
    print(resp2.text)
    if 'Cerrar sesión' in resp2.text:
        await send('Login Okkm')
        soup2 = s(resp2.text,'html.parser')
        await send('Login ok')
        url1 = f"https://santiago.uo.edu.cu/index.php/stgo/user/profile"
        resp3 = session.post(url1, headers=header)
        print(resp3.text)
        await send("Estás en el perfil")
    else:
        await send("login error")

bot.start()
bot.send_message(5416296262,'**BoT Iniciado**')
bot.loop.run_forever()
