import keyboard
import time
import discord
#import pyautogui

def press_button(button: str, duration: int = 0.05):
    """Use keyboard to press a button."""
    keyboard.press(button)
    time.sleep(duration)
    keyboard.release(button)

def press_button_combo(buttons: list[str], duration: int = 0.05, seperation: int = 0.05):
    for button in buttons:
        press_button(button, duration)
        time.sleep(seperation)

def write_text(text: str, starting_char: str = "", ending_char: str = "", button_press_duration: int = 0.05):
    if starting_char != "": press_button(starting_char, button_press_duration)
    keyboard.write(text)
    if ending_char != "": press_button(ending_char, button_press_duration)


def cycle_menu(times: int = 1):
    """Cycles through menu items (by pressing tab)."""
    for _ in range(times):
        press_button("tab")
        time.sleep(0.05)

def roles_check(user: discord.User, guild: discord.Guild, roles: list[str], mode: int = 1) -> int:
    # Courtesy of Rubicon 3.x by Copper (GitHub: FateUnix29, Discord: @destiny_29)
    """Returns whether or not the specified user has the proper roles, or if the roles do not exist.
    
    Args:
        user (discord.User): The user to check.
        guild (discord.Guild): The guild with the roles specified.
        roles (list[str]): The names of the roles to check.
        mode (int): The mode. If 0, user must have all specified roles, if 1, user must have at least one specified role. If 2, user must not have any specified roles."""
    user_roles = [role.id for role in user.roles]
    for role in roles:
        guild_role = discord.utils.get(guild.roles, name=role)
        if not guild_role: return 2 # Role does not exist
        if guild_role.id not in user_roles:
            if mode == 0:
                return 0 # User does not meet one or more roles
        if guild_role.id in user_roles:
            if mode == 2:
                return 0 # User has blacklisted role
            return 1
    # User does not meet at least one role for mode 1. All other modes would have returned already.
    return 0