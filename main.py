from os import getenv
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

# Replace with the actual user ID you want to monitor
TARGET_USER_ID = 123456789012345678

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_message(message):


    target_user = bot.get_user(TARGET_USER_ID)
    if not target_user:
        return

    direct_ping_detected = False
    ping_detected = False

    # Check for direct mentions
    if target_user in message.mentions:
        direct_ping_detected = True

    # Check for reply pings
    if message.reference:
        try:
            replied_message = await message.channel.fetch_message(message.reference.message_id)
            if replied_message.author.id == TARGET_USER_ID and target_user in message.mentions:
                ping_detected = True
        except:
            pass

    # Do something when ping is detected
    if ping_detected:
        print(f"{message.author.mention} please leave reply pings off for maz!")

    if direct_ping_detected:
        print(f"{message.author.mention} please don't ping Maz!")
    await bot.process_commands(message)

BotToken = getenv("bot_token")
bot.run(BotToken)