import os
import time

import discord
from dotenv import load_dotenv
from selenium import webdriver
# get vars stored in .env
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

load_dotenv("key.env")

# instantiate discord client
client = discord.Client(intents=discord.Intents.default())

# check if bot is online
@client.event
async def on_ready():
    print(f'{client.user} is now online')

@client.event
async def on_message(message):
    if message.content == '!start':
        while 1:
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            driver = webdriver.Chrome('chromedriver.exe', options=option)
            driver.get('https://d2runewizard.com/terror-zone-tracker')
            terror = driver.find_element(by=By.CLASS_NAME, value='terror-zone-tracker_currentZone__stQfc').text
            await message.channel.send(terror)
            dt = datetime.now() + timedelta(hours=1)
            dt = dt.replace(minute=5)
            while datetime.now() < dt:
                time.sleep(1)


# get bot token from .env and run
client.run(os.getenv('TOKEN'))
