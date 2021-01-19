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
        text += "\n!dice or !骰子 1~100的骰子"
        text += "\n!曬卡 模組十連抽"
        text += "\n!抽模組 抽模組模擬器，最多400抽(ex:!抽模組\t10)"
        text += "\n!finfo 迷宮森林指令訊息"
        # text += "\n"
        return text

    def finfo_fun(self):
        text = "!f1 迷霧森林1樓起點(ex:!f1\t23)"
        text += "\n!f1p 迷霧森林1樓起點跟終點(ex:!f1p\t23\t26)\t26為2F"
        text += "\n!f11 迷霧森林起點23\n!f12 迷霧森林起點23"
        text += "\n!f3 迷霧森林3樓起點(ex:!f1\t23)"
        text += "\n!f3p 迷霧森林1樓起點跟終點(ex:!f1p\t23\t26)\t26為2F"
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


def setup(bot):
    bot.add_cog(cmdsInfo(bot))
