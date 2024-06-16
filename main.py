import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import pyautogui
import time
from steam_web_api import Steam
import pydirectinput
import subprocess
import pyautogui
import numpy as np
import cv2
import pytesseract
from threading import Thread
import helpers


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
adminprefix = "admin_bot: "
pyautogui.FAILSAFE = False



KEY = os.getenv("STEAM_API_KEY")
steam = Steam(KEY)
# Ping up
@bot.event
async def on_ready():
    channel = bot.get_channel(1247894755380297791)
    await channel.send("Admin Bot is Online!")


#Commands
@bot.command(name='adminmessage',help="Sends a message as an admin")
@commands.has_role('Bot Admin')
async def adminmessage(ctx, *, message: str):
    try:
        pyautogui.typewrite('j')
        pyautogui.typewrite(f'{ctx.author.name}@Discord: {message}')
        time.sleep(0.05)
        pyautogui.press('enter')

        await ctx.send("Message sent!")
        time.sleep(0.05)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command(name='softrestart', help="Restarts the match")
@commands.has_role('Bot Admin')
async def adminmessage(ctx):
    pyautogui.press('esc')
    for i in range(4):
        pyautogui.press('tab')
        time.sleep(0.05)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    await ctx.send("Server has been soft rebooted")

@bot.command(name='weather',help="Changes the weather. Can be changed to sunny, partcloudy, cloudy, highfog, sunnywet, sunnysnow, rain, thunder, snow")
@commands.has_role('Bot Admin')
async def weather(ctx, *, weather:str):
    pyautogui.press('esc')
    for i in range(4):
        pyautogui.press('tab')
        time.sleep(0.05)
    pyautogui.press('enter')
    for i in range(35):
        pyautogui.press('tab')
        time.sleep(0.03)
    # paths
    if(weather=="sunny"):
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press('esc')
            time.sleep(0.05)

    elif(weather=="partcloudy"):
        for i in range(2):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press('esc')
            time.sleep(0.05)

    elif(weather=="cloudy"):
        for i in range(3):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press('esc')
            time.sleep(0.05)

    elif(weather=="highfog"):
        for i in range(4):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press('esc')
            time.sleep(0.05)

    elif(weather=="sunnywet"):
        for i in range(5):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press('esc')
            time.sleep(0.05)

    elif(weather=="sunnysnow"):
        for i in range(6):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press('esc')
            time.sleep(0.05)

    elif(weather=="rain"):
        for i in range(7):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press('esc')
            time.sleep(0.05)

    elif(weather=="thunder"):
        for i in range(8):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press('esc')
            time.sleep(0.05)

    elif(weather=="snow"):
        for i in range(9):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        time.sleep(0.5)
        for i in range(2):
            pyautogui.press('esc')
            time.sleep(0.05)
    else:
        await ctx.send("Invalid weather.")
    await ctx.send("Weather changed")
    



# ban command
@bot.command(name='banid', help="Bans a user by their steam64 ID")
@commands.has_role('Bot Admin')
async def banid(ctx, id: str, length:str, reason:str="Default Reason."):
    guild = ctx.guild
    user = steam.users.get_user_details(id)
    username = user['player']['personaname']
    pyautogui.press('esc')
    for i in range(3):
        pyautogui.press('tab')
        time.sleep(0.05)    
    pyautogui.press('enter')
    for i in range(2):
        pyautogui.press('tab')
        time.sleep(0.05)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('enter') 
    pyautogui.typewrite(str(id))
    pyautogui.press('enter')
    for i in range(5):
        pyautogui.press('tab')
        time.sleep(0.03)
    pyautogui.press('enter')
    pyautogui.typewrite(f"You have been banned by a Discord admin for reason: {reason}. You may appeal this ban in the Discord.")
    pyautogui.press('enter')
    if(length=='10'):
        for i in range(7):
            pyautogui.press('tab')
            time.sleep(0.05)
        pyautogui.press('enter')
        pyautogui.press('esc')
        pyautogui.press('esc')
        await ctx.send(f"{id} AKA {username} banned for 10 minutes, reason {reason}")
    elif(length=='inf'):
        for i in range(6):
            pyautogui.press('tab')
            time.sleep(0.05)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('esc')
        pyautogui.press('esc')
        await ctx.send(f"{id} AKA {username} banned for infinity, reason {reason}")
    else:
        await ctx.send("At this time, banning someone for a time other than 10 or inf is not supported.")

# hard reboot command
def killbr():
    subprocess.call("TASKKILL /F /IM BrickRigs-Win64-Shipping.exe")

def startbr():
    os.startfile("steam://rungameid/552100")

@bot.command(name='hardrestart', help="Kills the server and then starts it again")
@commands.has_role('Bot Admin')
async def hardrestart(ctx):
    guild = ctx.guild
    await ctx.send("Restarting server...")
    killbr()
    time.sleep(5)
    startbr()
    time.sleep(25)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('enter')
    await ctx.send("Server has been hard rebooted")

@bot.command(name='settime', help="Sets the time in 24 hr whole number format")
@commands.has_role('Bot Admin')
async def settime(ctx, timesetting:str):
    guild = ctx.guild
    pyautogui.press('esc')
    time.sleep(0.1)
    for i in range(4):
        pyautogui.press('tab')
        time.sleep(0.05)
    pyautogui.press('enter')
    for i in range(28):
        pyautogui.press('tab')
        time.sleep(0.03)
    pyautogui.press('enter')
    pyautogui.typewrite(timesetting)
    pyautogui.press('enter')
    pyautogui.press('esc')
    time.sleep(0.03)
    pyautogui.press('esc')
    await ctx.send(f"Time changed to {timesetting}.")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)
