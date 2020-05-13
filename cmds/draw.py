import random
from core.classes import Cog_Extension
from discord.ext import commands
class draw(Cog_Extension):
    # --------------------抽模組begin------------------------
    def DrawModel(self,arg):
        Boundary = [900, 1800, 2700, 3600, 4500, 5400, 6300, 7200,
                    7500, 7800, 8100, 8400, 8700, 9000,
                    9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900,
                    9911, 9922,
                    9934, 9946, 9958, 9970, 9982,
                    9985, 9988, 9991, 9994, 9997, 10000]
        dic = {0: "DEF", 1: "MDEF", 2: "VIT", 3: "LUK", 4: "STR", 5: "AGI", 6: "INT", 7: "DEX",
               8: "HealHP", 9: "HealSP", 10: "魔力", 11: "致命", 12: "攻擊速度", 13: "名弓",
               14: "CRI", 15: "ASPD", 16: "Cast", 17: "ATK", 18: "MATK", 19: "Archer", 20: "Heal", 21: "MSP", 22: "MHP",
               23: "Delay", 24: "Fix",
               25: "Above", 26: "Life", 27: "Soul", 28: "M_Heal", 29: "M_SouL",
               30: "L_VIT", 31: "L_INT", 32: "L_DEX", 33: "L_STR", 34: "L_AGI", 35: "L_LUK"
               }

        count = arg
        modelText = ""
        length = len(Boundary)
        list = [0 for _ in range(length)]
        while count:
            n = random.randint(1, 10000)
            for _ in range(len(Boundary)):
                if n <= Boundary[_]:
                    list[_] += 1
                    modelText += "{}\t".format(dic[_])
                    break
            count -= 1
        sortText = "\n"
        count = 0
        for _ in range(length):
            if list[_] != 0:
                sortText += "{1:}個{0}\t".format(dic[_], list[_])
                count += 1
                if count % 6 == 0 and count != 0 and arg > 10:
                    sortText += "\n"
        return modelText, sortText


    def draw_func(self,arg):
        arg = int(arg)
        if arg > 400:
            text = "請輸入小於400以下的數字"
            return text
        else:
            modelText, sortText = self.DrawModel(arg)
            if arg > 10:
                text = sortText
            else:
                text = "{}{}".format(modelText, sortText)
        return text


    # --------------------抽模組end------------------------
    # --------------------抽卡begin------------------------
    def tendraw(self):
        count = 10
        Boundary = [7200, 9900, 9982, 10000]
        probList = [0.72, 0.27, 0.0082, 0.0018]
        probBoundary = [0.01403965, 0.00197433, 0.00074037, 0.00009360]
        dic = {0: "<:normal:695141551063433235>", 1: "<:rare:695141550983741452>", 2: "<:unique:695141551055306773>",
               3: "<:legend:695141551034073089>"}
        text = ""
        length = len(Boundary)
        list = [0 for _ in range(length)]
        n_count = 0
        while count:
            n = random.randint(1, 10000)
            for _ in range(len(Boundary)):
                if n <= Boundary[_]:
                    list[_] += 1
                    text += "{}".format(dic[_])
                    n_count += 1
                    # if n_count % 5 == 0 and n_count != 0:
                    #     text += "\n"
                    break
            count -= 1
        prob = 1
        count = 0
        for _ in range(length):
            if list[_] != 0:
                prob *= probList[_] ** list[_]  # --------------計算機率
                count += 1
        prob = round(prob, 8)
        if prob >= probBoundary[0]:
            text2 = "你很非歐"
        elif prob >= probBoundary[1] and prob < probBoundary[0]:
            text2 = "運氣不太好"
        elif prob >= probBoundary[2] and prob < probBoundary[1]:
            text2 = "運氣還可以"
        elif prob >= probBoundary[3] and prob < probBoundary[2]:
            text2 = "運氣還不錯"
        else:
            text2 = "歐氣滿滿"
        return text, text2




    @commands.command()
    async def 抽模組(self, ctx, arg):
        text = self.draw_func(arg)
        await ctx.send(text)

    @commands.command()
    async def 曬卡(self, ctx):
        text, text2 = self.tendraw()
        await ctx.send(text)
        await ctx.send(text2)


def setup(bot):
    bot.add_cog(draw(bot))
