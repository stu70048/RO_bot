from discord.ext import commands
from datetime import timezone, timedelta
import datetime
import asyncio
import datetime
import json
from core.classes import Cog_Extension


class threeboss(Cog_Extension):
    def ten2b(self, arg):
        value = str(bin(int(arg))).split("b")[-1]
        length = len(value)
        if length % 4:
            value = value.zfill(length + 4 - length % 4)
        if length < 5:
            value = value.zfill(8)
        count = len(value) // 4 - 1
        text_list = list(value)
        while count:
            text_list.insert(int(count * (-4)), " ")
            count -= 1
        value = "".join(text_list)
        if len(value) < 10:
            value = self.b2s(value)
        return value

    def b2s(self, arg):
        count = 0
        text = ""
        for _ in arg:
            if _ == "0" or _ == "1":
                count += 1
                if _ == "1":
                    text += str(count)
        return text

    def todayValue(self):
        tzutc_4 = timezone(timedelta(hours=8))
        local_time = datetime.datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tzutc_4)
        todayValue = (local_time.day + local_time.month) * 5
        return self.ten2b(todayValue)

    # -------- old code
    # @commands.command()
    # async def b(self, ctx, arg):
    #     text = self.ten2b(arg)
    #     await ctx.send(text)
    #
    # @commands.command()
    # async def B(self, ctx, arg):
    #     text = self.ten2b(arg)
    #     await ctx.send(text)
    @commands.command()
    async def q(self, ctx):
        text = self.todayValue()
        await ctx.send(text)

    @commands.command()
    async def Q(self, ctx):
        text = self.todayValue()
        await ctx.send(text)

    @commands.command()
    async def b(self, ctx):
        text = self.todayValue()
        await ctx.send(text)

    @commands.command()
    async def B(self, ctx):
        text = self.todayValue()
        await ctx.send(text)


class threeboss_Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_task = self.bot.loop.create_task(self.daily_task())

    async def daily_task(self):
        await self.bot.wait_until_ready()
        self.channel = self.bot.get_channel(691950402937028629)
        while not self.bot.is_closed():
            now_time = datetime.datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(
                timezone(timedelta(hours=8))).strftime('%H%M')
            with open('setting.json', 'r', encoding='utf8') as jfile:
                jdata = json.load(jfile)
            if now_time == jdata['time']:
                await self.channel.send(threeboss.todayValue())
                # self.counter = 1
                await asyncio.sleep(60)
            else:
                await asyncio.sleep(1)
                pass


def setup(bot):
    bot.add_cog(threeboss(bot))
    bot.add_cog(threeboss_Task(bot))