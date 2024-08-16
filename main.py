###################################################################################################################
##                                                                                                               ##
##                                             Brick Rigs Server Bot                                             ##
##     A Discord bot that allows you to control (specifically, regarding moderation) your Brick Rigs server.     ##
##                                                                                                               ##
##                                   Authored by JHudd073 (Discord: @jhudd435)                                   ##
##                        App commands: Copper (GitHub: FateUnix29, Discord: @destiny_29)                        ##
##                                                                                                               ##
##                     Find the bot on GitHub here: https://github.com/JHudd073/BrickRigsBot                     ##
##                                                                                                               ##
###################################################################################################################


###  Modules  ###
import os                                      # Operating System | Functionality such as file system management, environment variables, etc.
import discord                                 # Discord API      | Discord bot framework (In Python).
from discord import app_commands               # Discord API      | App/slash commands.
import pyautogui                               # GUI automation   | Allows for interaction with GUI in Python.                  
import time                                    # Time             | Timing.
import subprocess                              # Subprocess       | Running shell commands, other processes, etc.

### Src files ###
from utils_extras import print, FM             # Utilities        | Colored printing.
from functions import *                        # Functions        | Various functions.

###    Init   ###
os.system("color") # Terminal coloring support.

### Constants ###
DT_TOKEN_NAME = "DISCORD_TOKEN"                  # Name of Discord token environment variable
BOT_CHANNEL_ID = 1247894755380297791  # The ID of the channel you want the bot to send stuff like it's boot message to

###  Globals  ###
TOKEN = os.getenv(DT_TOKEN_NAME)

#bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
bot = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(bot)
adminprefix = "admin_bot: "
pyautogui.FAILSAFE = False

# Ping up
@bot.event
async def on_ready():
    print(f"{FM.success} Logged in as {bot.user} ({bot.user.id})")
    channel = bot.get_channel(1247894755380297791)
    # Create a fancy embed
    embed = discord.Embed(title="Online - BR-BOT 2024", description="Authored by JHudd073 (@jhudd435).\nThe Brick Rigs bot is now online.", color=0x00ff00)
    await channel.send("Bot is online!", embed=embed)
    print(f"{FM.trying} Attempting sync...")
    await tree.sync()
    print(f"{FM.success} Synced to all servers.")


#Commands

# Send a message as admin
@tree.command(name='adminmessage',description="Sends a message as an admin")
async def adminmessage(ctx, message: str):
    if roles_check(ctx.author, ctx.guild, ['Bot Admin']):
        press_button('j')
        write_text(f"{ctx.author.display_name}@Discord: {message}", ending_char="enter")
        await ctx.response.send_message("Message sent!")
    else:
        print(f"{FM.info} User {ctx.user.display_name} did not have permissions to run adminmessage.")
        await ctx.response.send_message("You do not have permission to run this command.")

# Reboot the match
@tree.command(name='softrestart', description="Restarts the match")
async def adminmessage(ctx):
    if roles_check(ctx.author, ctx.guild, ['Bot Admin']):
        press_button("esc")
        cycle_menu(4)
        press_button_combo(['enter', 'tab', 'enter'], seperation=0)
        time.sleep(0.5)
        press_button('enter')
        await ctx.response.send_message("Server has been soft rebooted.")
    else:
        print(f"{FM.info} User {ctx.user.display_name} did not have permissions to run softrestart.")
        await ctx.response.send_message("You do not have permission to run this command.")


# Weather command
@tree.command(name='weather', description="Changes the weather. Enter 'list' for available weather options.")
async def weather(ctx, weather: str):
    if roles_check(ctx.author, ctx.guild, ['Bot Admin']):
        press_button('esc')
        cycle_menu(4)
        press_button('enter')
        cycle_menu(35)
        
        # paths
        match weather:
            case "sunny":
                press_button_combo(['tab', 'enter'])
                time.sleep(0.1)
                press_button_combo(['esc', 'esc'])
                ctx.response.send_message(f"Successfully changed weather to '{weather}'.")

            case "partly_cloudy":
                cycle_menu(2)
                press_button('enter')
                time.sleep(0.1)
                press_button_combo(['esc', 'esc'])
                ctx.response.send_message(f"Successfully changed weather to '{weather}'.")

            case "cloudy":
                cycle_menu(3)
                press_button('enter')
                time.sleep(0.1)
                press_button_combo(['esc', 'esc'])
                ctx.response.send_message(f"Successfully changed weather to '{weather}'.")

            case "highfog":
                cycle_menu(4)
                press_button('enter')
                time.sleep(0.1)
                press_button_combo(['esc', 'esc'])
                ctx.response.send_message(f"Successfully changed weather to '{weather}'.")

            case "sunnywet":
                cycle_menu(5)
                press_button('enter')
                time.sleep(0.1)
                press_button_combo(['esc', 'esc'])
                ctx.response.send_message(f"Successfully changed weather to '{weather}'.")

            case "sunnysnow":
                cycle_menu(6)
                press_button('enter')
                time.sleep(0.1)
                press_button_combo(['esc', 'esc'])
                ctx.response.send_message(f"Successfully changed weather to '{weather}'.")

            case "rain":
                cycle_menu(7)
                press_button('enter')
                time.sleep(0.1)
                press_button_combo(['esc', 'esc'])
                ctx.response.send_message(f"Successfully changed weather to '{weather}'.")

            case "thunder":
                cycle_menu(8)
                press_button('enter')
                time.sleep(0.1)
                press_button_combo(['esc', 'esc'])
                ctx.response.send_message(f"Successfully changed weather to '{weather}'.")

            case "snow":
                cycle_menu(9)
                press_button('enter')
                time.sleep(0.1)
                press_button_combo(['esc', 'esc'])
                ctx.response.send_message(f"Successfully changed weather to '{weather}'.")
            
            case "list":
                ctx.response.send_message("""Available weather options:
                sunny
                partly_cloudy
                cloudy
                highfog
                sunnywet
                sunnysnow
                rain
                thunder
                snow""".replace("\t", ""))
            case _:
                await ctx.response.send_message("Invalid weather option. Try 'list' for available weather options.")
    else:
        print(f"{FM.info} User {ctx.user.display_name} did not have permissions to run weather.")
        await ctx.response.send_message("You do not have permission to run this command.")
    



# ban command
@tree.command(name='banid', description="Bans a user by their steam64 ID")
async def banid(ctx, id: str, length_min: int = 0, length_hr: int = 0, length_day: int = 0, length_sec: int = 0, inf: bool = False, reason: str = "No reason given"):
    if roles_check(ctx.author, ctx.guild, ['Bot Admin']):
        press_button('esc')
        cycle_menu(3)
        press_button('enter')
        cycle_menu(2)
        press_button_combo(['enter', 'tab', 'enter'])
        write_text(str(id), ending_char='enter')
        cycle_menu(5)
        write_text(str(reason), "enter", "enter")
        cycle_menu(2)
        write_text(str(length_day), "enter", "enter")
        press_button("tab")
        write_text(str(length_hr), "enter", "enter")
        press_button("tab")
        write_text(str(length_min), "enter", "enter")
        press_button("tab")
        write_text(str(length_sec), "enter", "enter")
        press_button("tab")
        if inf: press_button("enter")
        press_button_combo(["tab", "enter", "esc", "esc"])
        ban_time_str = ""
        if length_day != 0: ban_time_str += f"{length_day} days, "
        if length_hr != 0: ban_time_str += f"{length_hr} hours, "
        if length_min != 0: ban_time_str += f"{length_min} minutes, "
        if length_sec != 0: ban_time_str += f"{length_sec} seconds"
        ban_time_str.rstrip(", ")
        if inf:
            ban_time_str = "infinity"
        elif not inf and ban_time_str == "": ban_time_str = "????????"
        embed = discord.Embed(title="Banned", description=f"User `{str(id)}` has been banned for {ban_time_str} for `{reason}`.", color=0x2ecc71)
        ctx.response.send_message(embed=embed)
    else:
        print(f"{FM.info} User {ctx.user.display_name} did not have permissions to run banid.")
        await ctx.response.send_message("You do not have permission to run this command.")
        

# hard reboot command
def killbr():
    subprocess.call("TASKKILL /F /IM BrickRigs-Win64-Shipping.exe")

def startbr():
    os.startfile("steam://rungameid/552100")

@tree.command(name='hardrestart', description="Kills the server and then starts it again")
async def hardrestart(ctx):
    if roles_check(ctx.author, ctx.guild, ['Bot Admin']):
        await ctx.response.send_message("Restarting server...")
        killbr()
        time.sleep(5)
        startbr()
        time.sleep(25)
        press_button_combo(['enter', 'tab', 'enter'])
        await ctx.channel.send("Server has been hard rebooted")
    else:
        print(f"{FM.info} User {ctx.user.display_name} did not have permissions to run hardrestart.")
        await ctx.response.send_message("You do not have permission to run this command.")

# Set the time
@tree.command(name='settime', description="Sets the time in 24 hr whole number format")
async def settime(ctx, timesetting:str):
    if roles_check(ctx.author, ctx.guild, ['Bot Admin']):
        press_button('esc')
        time.sleep(0.1)
        cycle_menu(4)
        press_button('enter')
        cycle_menu(28)
        write_text(timesetting, "enter", "enter")
        press_button_combo(['esc', 'esc'])
        await ctx.response.send_message(f"Time changed to {timesetting}.")
    else:
        print(f"{FM.info} User {ctx.user.display_name} did not have permissions to run settime.")
        await ctx.response.send_message("You do not have permission to run this command.")

@tree.command(name="force_sync", description="Sync the commands of this bot to the servers it is in.")
async def forcesynccmd(ctx):
    if roles_check(ctx.author, ctx.guild, ['Bot Admin']):
        print(f"{FM.trying} Attempting sync...")
        ctx.response.send_message("Attempting sync...")
        tree.sync()
        print(f"{FM.success} Synced to all servers.")
        ctx.channel.send("Synced to all servers.")
    else:
        print(f"{FM.info} User {ctx.user.display_name} did not have permissions to run force_sync.")
        await ctx.response.send_message("You do not have permission to run this command.")

bot.run(TOKEN)
