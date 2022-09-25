import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random, os, asyncio
#import keep_alive

"""
1.5 重大更新需加入intents 詳細請閱讀官方文件
https://discordpy.readthedocs.io/en/latest/intents.html#intents-primer
"""
# 啟用所有 intents
intents = discord.Intents.all()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix=jdata['Prefix'])


@bot.event
async def on_ready():
    print(">> Bot is online <<")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="死亡筆記本"))
# # Setting `Playing ` status
# await bot.change_presence(activity=discord.Game(name="a game"))
#
# # Setting `Streaming ` status
# await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))
#
# # Setting `Listening ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
#
# # Setting `Watching ` status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

# #discord.Status.<狀態>，可以是,online,offline,idle,dnd,invisible
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    #keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])
