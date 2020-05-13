import discord
from discord.ext import commands
from core.classes import Cog_Extension, Logger
import json, asyncio

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Errors():
	# 自訂 Error Handler


	# 預設 Error Handler
	async def default_error(self, ctx, error):
		# default_check = False
		if isinstance(error, commands.MissingRequiredArgument):
			# default_check = True
			await ctx.send(self, error)
			Logger.log(self, ctx, error)
		else:
			await ctx.send(f'未知錯誤: {error}')
			Logger.log(self, ctx, error)