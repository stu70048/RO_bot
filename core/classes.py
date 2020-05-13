import discord
from discord.ext import commands
import json, datetime

class Cog_Extension(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

class Gloable_Func():
	def update_jdata(self, key, data, type='default', mode='update'):
		'''
		更新 Jdata 功能\n
		type: default / list\n
		mode: update / delete
		'''
		with open('setting.json', 'r', encoding='utf8') as jfile:
			jdata = json.load(jfile)
			if mode == 'update':
				if type == 'default':
					jdata[key] = data
				elif type == 'list':
					jdata[key].append(data)
			elif mode == 'delete':
				if type == 'list':
					jdata[key].remove(data)
				
		with open('setting.json', 'w', encoding='utf8') as jfile:
			json.dump(jdata, jfile, indent=4, ensure_ascii=False)
	
class Logger:
	def log(self, ctx, data, type='error'):
		'''事件紀錄器'''
		time = datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M]')
		user = ctx.author.name
		channel = ctx.channel.name
		command = ctx.command
		if type == 'error':
			print(f'🔥<Error Log>: {time}/[{user}][{channel}][{command}]: {data}')