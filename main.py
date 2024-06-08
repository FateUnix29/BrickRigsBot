import discord, pyautogui, time, subprocess, pytesseract, pydirectinput, os
from discord import app_commands
from dotenv import load_dotenv
from steam_web_api import Steam
from threading import Thread


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(bot)
adminprefix = "admin_bot: "
pyautogui.FAILSAFE = False

home_guild = discord.Object(1247723267029074002) # Guild object with ID 1247723267029074002
leave_unauth_guilds = True
admin_role = discord.utils.get(home_guild.roles, name="Bot Admin")

KEY = os.getenv("STEAM_API_KEY")
steam = Steam(KEY)
# Ping up
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------------------------------------------------------------")
    print("Syncing commands...")
    if len(bot.guilds) == 1: await tree.sync(guild=home_guild) # Sync slash commands with our server
    elif len(bot.guilds) >= 2: await tree.sync() # Sync slash commands with all servers
    channel = bot.get_channel(1247894755380297791)
    await channel.send("Admin Bot is Online!")

@bot.event
async def on_guild_join(guild):
    global leave_unauth_guilds
    # We aren't supposed to be in any other guild.
    print("Bot joined unauthorized guild! Leaving for security reasons.")
    print(f"Guild name: '{guild.name}' with an ID of {guild.id}.")
    print("Disable 'leave_unauth_guilds' in codes if you wish to join any other guild.")
    if leave_unauth_guilds: await bot.get_guild(guild.id).leave() # bye bye
    else:
        print("Aborting leave. Variable is set to False. Syncing...")
        tree.sync()

#Commands
@bot.command(name='adminmessage', description="Sends a message as an admin")
async def adminmessage(ctx, *, message: str):
    global admin_role
    if admin_role in ctx.author.roles:
        try:
            pyautogui.typewrite('j')
            pyautogui.typewrite(f'{message}')
            time.sleep(0.05)
            pyautogui.press('enter')

            await ctx.channel.send("Message sent!")
            time.sleep(0.05)
        except Exception as e:
            await ctx.channel.send(f"An error occurred: {e}")
    else:
        print(f"{ctx.author.display_name} did not have the permission level to use the admin message command.")
        await ctx.channel.send("You do not have permission to use this command.")


@bot.command(name='softrestart', description="Restarts the match")
async def adminmessage(ctx):
    global admin_role
    if admin_role in ctx.author.roles:
        pyautogui.press('esc')
        for _ in range(4):
            pyautogui.press('tab')
            time.sleep(0.05)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('enter')
        await ctx.channel.send("Server has been soft rebooted")
    else:
        print(f"{ctx.author.display_name} did not have the permission level to soft restart the server.")
        await ctx.channel.send("You do not have permission to use this command.")

@bot.command(name='weather', description="Changes the weather. Can be changed to sunny, partcloudy, cloudy, highfog, sunnywet, sunnysnow, rain, thunder, snow")
async def weather(ctx, *, weather:str):
    global admin_role
    if admin_role in ctx.author.roles:
        weather_not_set = False
        pyautogui.press('esc')
        for _ in range(4):
            pyautogui.press('tab')
            time.sleep(0.05)
        pyautogui.press('enter')
        for _ in range(35):
            pyautogui.press('tab')
            time.sleep(0.03)
        # paths
        match weather:
            case "sunny":
                pyautogui.press('tab')
                pyautogui.press('enter')
                time.sleep(0.5)
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.05)

            case "partcloudy":
                for _ in range(2):
                    pyautogui.press('tab')
                    time.sleep(0.03)
                pyautogui.press('enter')
                time.sleep(0.5)
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.05)

            case "cloudy":
                for _ in range(3):
                    pyautogui.press('tab')
                    time.sleep(0.03)
                pyautogui.press('enter')
                time.sleep(0.5)
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.05)

            case "highfog":
                for _ in range(4):
                    pyautogui.press('tab')
                    time.sleep(0.03)
                pyautogui.press('enter')
                time.sleep(0.5)
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.05)

            case "sunnywet":
                for _ in range(5):
                    pyautogui.press('tab')
                    time.sleep(0.03)
                pyautogui.press('enter')
                time.sleep(0.5)
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.05)

            case "sunnysnow":
                for _ in range(6):
                    pyautogui.press('tab')
                    time.sleep(0.03)
                pyautogui.press('enter')
                time.sleep(0.5)
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.05)

            case "rain":
                for _ in range(7):
                    pyautogui.press('tab')
                    time.sleep(0.03)
                pyautogui.press('enter')
                time.sleep(0.5)
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.05)

            case "thunder":
                for _ in range(8):
                    pyautogui.press('tab')
                    time.sleep(0.03)
                pyautogui.press('enter')
                time.sleep(0.5)
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.05)

            case "snow":
                for _ in range(9):
                    pyautogui.press('tab')
                    time.sleep(0.03)
                pyautogui.press('enter')
                time.sleep(0.5)
                for _ in range(2):
                    pyautogui.press('esc')
                    time.sleep(0.05)
            case _:
                await ctx.channel.send("Invalid weather.")
                weather_not_set = True

        if not weather_not_set: await ctx.channel.send("Weather changed.")
    else:
        print(f"{ctx.author.display_name} did not have the permission level to change the weather.")
        await ctx.channel.send("You do not have permission to use this command.")
        



# ban command
@bot.command(name='banid', description="Bans a user by their steam64 ID")
async def banid(ctx, id: str, length:str, reason:str="Default Reason."):
    global admin_role
    if admin_role in ctx.author.roles:
        guild = ctx.guild
        user = steam.users.get_user_details(id)
        username = user['player']['personaname']
        pyautogui.press('esc')
        for _ in range(3):
            pyautogui.press('tab')
            time.sleep(0.05)    
        pyautogui.press('enter')
        for _ in range(2):
            pyautogui.press('tab')
            time.sleep(0.05)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter') 
        pyautogui.typewrite(str(id))
        pyautogui.press('enter')
        for _ in range(5):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        pyautogui.typewrite(f"You have been banned by a Discord admin for reason: {reason}. You may appeal this ban in the Discord.")
        pyautogui.press('enter')
        if length=='10':
            for _ in range(7):
                pyautogui.press('tab')
                time.sleep(0.05)
            pyautogui.press('enter')
            pyautogui.press('esc')
            pyautogui.press('esc')
            await ctx.channel.send(f"{id} AKA {username} banned for 10 minutes, reason {reason}")
        elif length=='inf':
            for _ in range(6):
                pyautogui.press('tab')
                time.sleep(0.05)
            pyautogui.press('enter')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.press('esc')
            pyautogui.press('esc')
            await ctx.channel.send(f"{id} AKA {username} banned for infinity, reason {reason}")
        else:
            await ctx.channel.send("At this time, banning someone for a time other than 10 or inf is not supported.")
    else:
        print(f"{ctx.author.display_name} did not have the permission level to ban a user.")
        await ctx.channel.send("You do not have permission to use this command.")

# hard reboot command
def killbr():
    subprocess.call("TASKKILL /F /IM BrickRigs-Win64-Shipping.exe")

def startbr():
    os.startfile("steam://rungameid/552100")

@bot.command(name='hardrestart', description="Kills the server and then starts it again")
async def hardrestart(ctx):
    global admin_role
    if admin_role in ctx.author.roles:
        guild = ctx.guild
        await ctx.channel.send("Restarting server...")
        killbr()
        time.sleep(5)
        startbr()
        time.sleep(25)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')
        await ctx.channel.send("Server has been hard rebooted")
    else:
        print(f"{ctx.author.display_name} did not have the permission level to hard restart the server.")
        await ctx.channel.send("You do not have permission to use this command.")

@bot.command(name='settime', description="Sets the time in 24 hr whole number format")
async def settime(ctx, timesetting:str):
    global admin_role
    if admin_role in ctx.author.roles:
        guild = ctx.guild
        pyautogui.press('esc')
        time.sleep(0.05)
        for _ in range(4):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        for _ in range(28):
            pyautogui.press('tab')
            time.sleep(0.03)
        pyautogui.press('enter')
        pyautogui.typewrite(timesetting)
        pyautogui.press('enter')
        pyautogui.press('esc')
        time.sleep(0.03)
        pyautogui.press('esc')
        await ctx.channel.send(f"Time changed to {timesetting}.")
    else:
        print(f"{ctx.author.display_name} did not have the permission level to set the time.")
        await ctx.channel.send("You do not have permission to use this command.")

@bot.command(name='die', description="Kills host")
async def die(ctx):
    global admin_role
    if admin_role in ctx.author.roles:
        guild = ctx.guild
        pyautogui.press('end')
    else:
        print(f"{ctx.author.display_name} did not have the permission level to kill the host.")
        await ctx.channel.send("You do not have permission to use this command.")

bot.run(TOKEN)