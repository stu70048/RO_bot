import random
from discord.ext import commands
from core.classes import Cog_Extension
import gspread
import json


def chgUpperlimit(Upperlimit):
    client = gspread.service_account("service_account.json")
    spreadSheet = client.open("ChenKuang").sheet1
    spreadSheet.batch_update([{
        'range': 'A7:B7',
        'values': [["﻿Upperlimit", Upperlimit], ],
    }])


def chgpwdr():
    client = gspread.service_account("service_account.json")
    spreadSheet = client.open("ChenKuang").sheet1
    Upperlimit = int(spreadSheet.get('B7').first())
    pwdvalue = random.randint(1, Upperlimit)
    spreadSheet.batch_update([{
        'range': 'A6:B6',
        'values': [["pwdvalue", pwdvalue],
                   ],
    }])


def chgpwdp(pwdvalue):
    client = gspread.service_account("service_account.json")
    spreadSheet = client.open("ChenKuang").sheet1
    spreadSheet.batch_update([{
        'range': 'A6:B6',
        'values': [["pwdvalue", pwdvalue],
                   ],
    }])


def reset():
    client = gspread.service_account("service_account.json")
    spreadSheet = client.open("ChenKuang").sheet1
    spreadSheet.batch_update([{
        'range': 'A8:B9',
        'values': [["valuesMAX", -1],
                   ["valueMIN", -1], ],
    }])


# def checknumber(arg):
#     client = gspread.service_account("service_account.json")
#     spreadSheet = client.open("ChenKuang").sheet1
#     spreadSheet.batch_update([{
#         'range': 'A7:B8',
#         'values': [["valuesMAX", valuesMAX],
#                    ["valueMIN", valueMIN], ],
#     }])
#     return
def guesspwdfunc(value):
    value = int(value)
    client = gspread.service_account("service_account.json")
    spreadSheet = client.open("ChenKuang").sheet1
    pwdvalue = int(spreadSheet.get('B6').first())
    Upperlimit = int(spreadSheet.get('B7').first())
    valueMAX = int(spreadSheet.get('B8').first())
    valueMIN = int(spreadSheet.get('B9').first())
    if valueMAX == -1 and valueMIN == -1:
        if value == pwdvalue:
            text = f"第一次就賓果，答案是{pwdvalue}!"
            spreadSheet.batch_update([{
                'range': 'A8:B9',
                'values': [["valueMAX", -1],
                           ["valueMIN", -1], ],
            }])
        elif pwdvalue < value < Upperlimit:
            valueMAX = value
            valueMIN = 1
            spreadSheet.batch_update([{
                'range': 'A8:B9',
                'values': [["valueMAX", valueMAX],
                           ["valueMIN", valueMIN], ],
            }])
            text = f"現在密碼介於為{valueMIN}~{valueMAX}"
        elif value < pwdvalue and value > 0:
            valueMAX = Upperlimit
            valueMIN = value
            spreadSheet.batch_update([{
                'range': 'A8:B9',
                'values': [["valueMAX", valueMAX],
                           ["valueMIN", valueMIN], ],
            }])
            text = f"現在密碼介於為{valueMIN}~{valueMAX}"
        else:
            text = f"輸入數字超出範圍，請再輸入一次"
        return text
    elif valueMAX <= Upperlimit and valueMIN >= 1:
        if value == pwdvalue:
            text = f"賓果，答案是{pwdvalue}!"
            spreadSheet.batch_update([{
                'range': 'A8:B9',
                'values': [["valuesMAX", -1],
                           ["valueMIN", -1], ],
            }])

        elif pwdvalue < value < valueMAX:
            valueMAX = value
            spreadSheet.batch_update([{
                'range': 'A8:B9',
                'values': [["valueMAX", valueMAX],
                           ["valueMIN", valueMIN], ],
            }])
            text = f"現在密碼介於為{valueMIN}~{valueMAX}"
        elif pwdvalue > value > valueMIN:
            valueMIN = value
            spreadSheet.batch_update([{
                'range': 'A8:B9',
                'values': [["valueMAX", valueMAX],
                           ["valueMIN", valueMIN], ],
            }])
            text = f"現在密碼介於為{valueMIN}~{valueMAX}"
        else:
            text = f"輸入數字超出範圍，請再輸入一次"
        return text


# 終極密碼
class guesspwd(Cog_Extension):
    @commands.command()
    async def d(self, ctx, arg):
        text = guesspwdfunc(arg)
        await ctx.send('{.message.author.name}輸入的數字為{}，{}'.format(ctx, arg, text))

    @commands.command()
    async def dr(self, ctx):
        chgpwdr()
        await ctx.send('已產生一個新的終極密碼')

    @commands.command()
    async def dp(self, ctx, arg):
        chgpwdp(arg)
        await ctx.send('已將終極密碼改為{}'.format(arg))

    @commands.command()
    async def dup(self, ctx, arg):
        chgUpperlimit(arg)
        await ctx.send('已將終極密碼上限改為{}'.format(arg))

    @commands.command()
    async def dreset(self, ctx):
        reset()
        await ctx.send('已重製數據')

    # --------------------------大寫
    @commands.command()
    async def D(self, ctx, arg):
        text = guesspwdfunc(arg)
        await ctx.send('{.message.author.name}輸入的數字為{}，{}'.format(ctx, arg, text))

    @commands.command()
    async def DR(self, ctx):
        chgpwdr()
        await ctx.send('已產生一個新的終極密碼')

    @commands.command()
    async def DP(self, ctx, arg):
        chgpwdp(arg)
        await ctx.send('已將終極密碼改為{}'.format(arg))

    @commands.command()
    async def DUP(self, ctx, arg):
        chgUpperlimit(arg)
        await ctx.send('已將終極密碼上限改為{}'.format(arg))

    @commands.command()
    async def DRESET(self, ctx):
        reset()
        await ctx.send('已重製數據')


def setup(bot):
    bot.add_cog(guesspwd(bot))
