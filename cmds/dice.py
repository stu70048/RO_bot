import random
from discord.ext import commands
from core.classes import Cog_Extension


def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros


def dice_ShowHand():
    list = []
    for i in range(5):
        list.append(random.randint(1, 6))
    callist = zerolistmaker(6)
    for _ in list:
        callist[_ - 1] += 1
    if max(callist) == 5:
        text = "豹子"
    elif callist == [1, 1, 1, 1, 1, 0] or callist == [0, 1, 1, 1, 1, 1]:
        text = "順子"
    elif max(callist) == 4:
        text = "4帶1"
    elif max(callist) == 3 and callist.count(2) == 1:
        text = "3帶2"
    elif max(callist) == 3:
        text = "3個"
    elif callist.count(2) == 2:
        text = "2對"
    elif callist.count(2) == 1:
        text = "1對"
    else:
        text = "散骰"
    return list, text


# 1-100的骰子與骰子梭哈
class dice(Cog_Extension):
    @commands.command()
    async def dice(self, ctx):
        text = random.randint(1, 100)
        await ctx.send('{.message.author.name}擲出\t{}'.format(ctx, text))

    @commands.command()
    async def DICE(self, ctx):
        text = random.randint(1, 100)
        await ctx.send('{.message.author.name}擲出\t{}'.format(ctx, text))

    @commands.command()
    async def 骰子(self, ctx):
        text = random.randint(1, 100)
        await ctx.send('{.message.author.name}擲出\t{}'.format(ctx, text))

    @commands.command()
    async def dice5(self, ctx):
        list, text = dice_ShowHand()
        await ctx.send('{.message.author.name}梭哈出\t{}，{}'.format(ctx, list, text))
    @commands.command()
    async def DICE5(self, ctx):
        list, text = dice_ShowHand()
        await ctx.send('{.message.author.name}梭哈出\t{}，{}'.format(ctx, list, text))
    @commands.command()
    async def 骰子梭哈(self, ctx):
        list, text = dice_ShowHand()
        await ctx.send('{.message.author.name}梭哈出\t{}，{}'.format(ctx, list, text))
    @commands.command()
    async def dice5info(self, ctx):
        text = "點數大小排序：1>6>5>4>3>2"
        text += "\n骰型大小排序：豹子>順子>4個>3帶2>3個>2對>1個>散骰"
        await ctx.send('{}'.format(text))
    @commands.command()
    async def 骰子梭哈玩法(self, ctx):
        text = "點數大小排序：1>6>5>4>3>2"
        text += "\n骰型大小排序：豹子>順子>4個>3帶2>3個>2對>1個>散骰"
        await ctx.send('{}'.format(text))

async def setup(bot):
    await bot.add_cog(dice(bot))
    
