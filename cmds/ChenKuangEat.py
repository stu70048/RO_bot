import asyncio
import datetime
import json
from discord.ext import commands
from datetime import timezone, timedelta

from core.classes import Cog_Extension

# item_num = {1: "傑勒比結晶", 2: "樹根", 3: "蝗蟲後腿", 4: "三葉幸運草", 5: "羽毛", 6: "鼠尾", 7: "毒牙", 8: "猴子尾巴", 9: "蝙蝠牙"}
item_num = {1: "傑勒比結晶", 2: "樹根", 3: "蝗蟲後腿", 4: "三葉幸運草", 5: "羽毛", 6: "鼠尾", 7: "毒牙", 8: "猴子尾巴", 9: "蝙蝠牙", 10: "熊掌"}
item_id = {y: x for x, y in item_num.items()}


def days(str1, str2):
    date1 = datetime.datetime.strptime(str1[0:10], "%Y-%m-%d")
    date2 = datetime.datetime.strptime(str2[0:10], "%Y-%m-%d")
    num = (date1 - date2).days
    return num


def time_now():
    tzutc_4 = timezone(timedelta(hours=4))
    local_time = datetime.datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tzutc_4).strftime("%Y-%m-%d")
    return local_time


def eat_func():
    with open('ChenKuang.json', 'r', encoding='utf8') as jfile:
        jdata = json.load(jfile)
    if jdata['update_time'] == time_now():
        today_item = item_num[jdata['ChenKuangEatItem']]
        tomorrow_item = item_num[(jdata['ChenKuangEatItem']) % len(item_num) + 1]
        text = "晨光今天吃\"{}\"\n明天吃{}".format(today_item, tomorrow_item)
    else:
        day = days(str(time_now()), jdata['update_time'])
        today_item = item_num[(jdata['ChenKuangEatItem'] + day - 1) % len(item_num) + 1]
        tomorrow_item = item_num[item_id[today_item] % len(item_num) + 1]

        jdata['week'] = datetime.datetime.now().weekday() + 1
        jdata['ChenKuangEatItem'] = item_id[today_item]
        jdata['update_time'] = time_now()
        with open('ChenKuang.json', 'w', encoding='utf8') as file:
            json.dump(jdata, file, ensure_ascii=False, indent=4, default=str)
        text = "晨光今天吃\"{}\"\n明天吃{}".format(today_item, tomorrow_item)
    if datetime.datetime.now().weekday() + 1 == 2:
        text += "\n今天可能維修，物品若有變動請用[!upgrade or !UPGRADE + 物品]進行更新"
    return text


def upgradeData(arg):
    if arg in item_id.keys():
        with open('ChenKuang.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['week'] = datetime.datetime.now().weekday() + 1
        jdata['ChenKuangEatItem'] = item_id[arg]
        jdata['update_time'] = time_now()
        with open('ChenKuang.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, ensure_ascii=False, indent=4, default=str)
        text = f"物品為{item_num[jdata['ChenKuangEatItem']]}，更新資料成功!"
    else:
        text = "輸入物品錯誤，請在更新一次"
    return text


class ChenKuang(Cog_Extension):
    @commands.command()
    async def eat(self, ctx):
        text = eat_func()
        await ctx.send(text)

    @commands.command()
    async def EAT(self, ctx):
        text = eat_func()
        await ctx.send(text)

    @commands.command()
    async def eatshit(self, ctx):
        text = "晨光哩甲賽喇"
        await ctx.send(text)

    @commands.command()
    async def EATSHIT(self, ctx):
        text = "晨光哩甲賽喇"
        await ctx.send(text)

    @commands.command()
    async def upgrade(self, ctx, arg):
        text = upgradeData(arg)
        await ctx.send(text)

    @commands.command()
    async def UPGRADE(self, ctx, arg):
        text = upgradeData(arg)
        await ctx.send(text)


class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.bot.loop.create_task(self.daily_task())

    async def daily_task(self):
        await self.bot.wait_until_ready()
        self.channel = self.bot.get_channel(691950402937028629)
        while not self.bot.is_closed():
            now_time = datetime.datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(
                timezone(timedelta(hours=4))).strftime('%H%M')
            with open('setting.json', 'r', encoding='utf8') as jfile:
                jdata = json.load(jfile)
            # if now_time == jdata['time'] and self.counter == 0:
            if now_time == jdata['time']:
                await self.channel.send(eat_func())
                # self.counter = 1
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(1)
                pass

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.metion}')

    @commands.command()
    async def set_time(self, ctx, time):
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)


def setup(bot):
    bot.add_cog(Task(bot))
    bot.add_cog(ChenKuang(bot))
