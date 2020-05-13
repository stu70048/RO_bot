import random
from discord.ext import commands
from core.classes import Cog_Extension


# 1-100的骰子
class dice(Cog_Extension):
    @commands.command()
    async def dice(self, ctx):
        text = random.randint(1, 100)
        await ctx.send(text)

    @commands.command()
    async def DICE(self, ctx):
        text = random.randint(1, 100)
        await ctx.send(text)

    @commands.command()
    async def 骰子(self, ctx):
        text = random.randint(1, 100)
        await ctx.send(text)


def setup(bot):
    bot.add_cog(dice(bot))
