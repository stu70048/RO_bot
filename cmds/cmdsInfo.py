from discord.ext import commands
from core.classes import Cog_Extension


class cmdsInfo(Cog_Extension):
    def info_func(self):
        text = "!eat 晨光今天食物"
        text += "\n!update or !upgrade + 物品 更新晨光食物(ex:!update\t鼠尾)"
        text += "\n!updatec 今天更新晨光食物次數"
        text += "\n!item 晨光食物列表"
        text += "\n!eatshit 晨光甲賽"
        text += "\n!w 三王密碼二進位"
        text += "\n!b or !q 三王密碼只看on開關"
        text += "\n!曬卡 模組十連抽"
        text += "\n!抽模組 抽模組模擬器，最多400抽(ex:!抽模組\t10)"
        text += "\n!finfo 迷宮森林指令訊息"
        text += "\n!diceinfo 骰子指令訊息"
        text += "\n!dinfo 終極密碼指令訊息"
        # text += "\n"
        return text

    def finfo_fun(self):
        text = "!f1 迷霧森林1樓起點(ex:!f1\t23)"
        text += "\n!f1p 迷霧森林1樓起點跟終點(ex:!f1p\t23\t26)\t26為2F"
        text += "\n!f11 迷霧森林起點23\n!f12 迷霧森林起點23"
        text += "\n!f3 迷霧森林3樓起點(ex:!f1\t23)"
        text += "\n!f3p 迷霧森林1樓起點跟終點(ex:!f1p\t23\t26)\t26為2F"
        return text

    def diceinfo_fun(self):
        text = "!dice(DICE/骰子) 1~100的骰子(ex:!骰子)"
        text += "\n!dice5(DICE5/骰子梭哈) 骰子梭哈(ex:!dice5)"
        text += "\n!dice5info(骰子梭哈玩法)"
        return text

    def dinfo_fun(self):
        text = "!d 猜終極密碼(ex:!d\t50)"
        text += "\n!dup 設定終極密碼數字上限(ex:!dup\t1000)"
        text += "\n!dr 機器人隨機產生一個終極密碼，介於1~設定上限"
        text += "\n!dp 直接設定終極密碼(ex:!dp 50)，請先設定上限在手動設定終極密碼"
        text += "\n!dreset 初始化設定，出錯時用"
        return text

    @commands.command()
    async def info(self, ctx):
        text = self.info_func()
        await ctx.send(text)

    @commands.command()
    async def INFO(self, ctx):
        text = self.info_func()
        await ctx.send(text)

    @commands.command()
    async def finfo(self, ctx):
        text = self.finfo_fun()
        await ctx.send(text)

    @commands.command()
    async def FINFO(self, ctx):
        text = self.finfo_fun()
        await ctx.send(text)

    @commands.command()
    async def dinfo(self, ctx):
        text = self.dinfo_fun()
        await ctx.send(text)

    @commands.command()
    async def DINFO(self, ctx):
        text = self.dinfo_fun()
        await ctx.send(text)

    @commands.command()
    async def diceinfo(self, ctx):
        text = self.diceinfo_fun()
        await ctx.send(text)

    @commands.command()
    async def DICEINFO(self, ctx):
        text = self.diceinfo_fun()
        await ctx.send(text)

def setup(bot):
    bot.add_cog(cmdsInfo(bot))
