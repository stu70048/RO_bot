from discord.ext import commands
import asyncio
from core.classes import Cog_Extension

####################################################################################################
########DATA for F1 toF2
F1toF2_graph = {1: {21: 1, 15: 1},
                2: {6: 1},
                3: {26: 1, 23: 1},
                4: {1: 1, 5: 1},
                5: {12: 1, 6: 1},
                6: {20: 1, 24: 1, 17: 1},
                7: {5: 1, 15: 1},
                8: {3: 1, 14: 1, 6: 1},
                9: {10: 1, 2: 1},
                10: {4: 1, 11: 1},
                11: {1: 1, 9: 1},
                12: {18: 1, 24: 1, 7: 1, 22: 1},
                13: {8: 1, 7: 1, 16: 1},
                14: {6: 1, 16: 1},
                15: {17: 1, 10: 1, 2: 1},
                16: {12: 1, 24: 1},
                17: {19: 1, 2: 1},
                18: {16: 1, 7: 1, 13: 1, 25: 1},
                19: {15: 1, 22: 1},
                20: {17: 1, 23: 1},
                21: {4: 1, 25: 1},
                22: {4: 1, 14: 1, 17: 1},
                23: {9: 1, 11: 1, 20: 1},
                24: {19: 1},
                25: {1: 1, 9: 1, 7: 1, 17: 1},
                26: {}
                }
F1toF2_direction = {1: {21: '上', 15: '左'},
                    2: {6: '上'},
                    3: {26: '左', 23: '下'},
                    4: {1: '左', 5: '右'},
                    5: {12: '下', 6: '右'},
                    6: {20: '上', 24: '下', 17: '左'},
                    7: {5: '上', 15: '下'},
                    8: {3: '上', 14: '左', 6: '右'},
                    9: {10: '下', 2: '右'},
                    10: {4: '左', 11: '右'},
                    11: {1: '上', 9: '下'},
                    12: {18: '上', 24: '下', 7: '左', 22: '右'},
                    13: {8: '上', 7: '左', 16: '右'},
                    14: {6: '上', 16: '左'},
                    15: {17: '下', 10: '左', 2: '右'},
                    16: {12: '左', 24: '上'},
                    17: {19: '下', 2: '右'},
                    18: {16: '上', 7: '下', 13: '左', 25: '右'},
                    19: {15: '上', 22: '下'},
                    20: {17: '下', 23: '右'},
                    21: {4: '上', 25: '下'},
                    22: {4: '下', 14: '左', 17: '右'},
                    23: {9: '上', 11: '左', 20: '右'},
                    24: {19: '右'},
                    25: {1: '上', 9: '下', 7: '左', 17: '右'},
                    26: {}
                    }
####################################################################################################
########DATA for F3 to F2
F3toF2_graph = {1: {20: 1, 9: 1},
                2: {8: 1, 9: 1, 16: 1},
                3: {16: 1, 19: 1},
                4: {13: 1, 19: 1},
                5: {22: 1, 10: 1},
                6: {22: 1, 20: 1, 18: 1},
                7: {14: 1, 13: 1},
                8: {23: 1, 11: 1, 25: 1},
                9: {17: 1, 1: 1},
                10: {12: 1, 5: 1},
                11: {14: 1, 8: 1},
                12: {16: 1, 10: 1, 18: 1, 22: 1},
                13: {4: 1, 7: 1, 25: 1},
                14: {7: 1, 2: 1},
                15: {26: 1, 20: 1, 24: 1},
                16: {25: 1, 12: 1, 3: 1},
                17: {8: 1, 9: 1, 22: 1, 21: 1},
                18: {23: 1, 12: 1, 25: 1, 6: 1},
                19: {3: 1, 16: 1, 22: 1},
                20: {6: 1, 1: 1, 15: 1},
                21: {17: 1, 23: 1},
                22: {12: 1, 6: 1, 5: 1},
                23: {8: 1, 21: 1, 18: 1},
                24: {9: 1, 16: 1, 22: 1},
                25: {18: 1, 13: 1, 8: 1, 16: 1},
                26: {}
                }
F3toF2_direction = {1: {20: '上', 9: '左'},
                    2: {8: '上', 9: '上', 16: '上'},
                    3: {16: '左', 19: '下'},
                    4: {13: '左', 19: '右'},
                    5: {22: '下', 10: '右'},
                    6: {22: '上', 20: '下', 18: '左'},
                    7: {14: '上', 13: '下'},
                    8: {23: '上', 11: '左', 25: '右'},
                    9: {17: '下', 1: '右'},
                    10: {12: '左', 5: '右'},
                    11: {14: '上', 8: '下'},
                    12: {16: '上', 10: '下', 18: '左', 22: '右'},
                    13: {4: '上', 7: '左', 25: '右'},
                    14: {7: '上', 2: '左'},
                    15: {26: '下', 20: '左', 24: '右'},
                    16: {25: '左', 12: '上', 3: '下'},
                    17: {8: '上', 9: '上', 22: '上', 21: '下'},
                    18: {23: '上', 12: '下', 25: '左', 6: '右'},
                    19: {3: '上', 16: '下', 22: '下'},
                    20: {6: '上', 1: '下', 15: '右'},
                    21: {17: '上', 23: '下'},
                    22: {12: '下', 6: '左', 5: '右'},
                    23: {8: '上', 21: '左', 18: '右'},
                    24: {9: '右', 16: '右', 22: '右'},
                    25: {18: '上', 13: '下', 8: '左', 16: '右'},
                    26: {}
                    }


####################################################################################################
def dijkstra(graph, source):
    visited = set()
    distance = dict((k, float("inf")) for k in graph.keys())
    distance[source] = 0
    path = [[] for i in range((len(graph) + 1))]
    while len(graph) != len(visited):
        visited.add(source)
        for next_node in graph[source]:
            if distance[next_node] > distance[source] + graph[source][next_node]:
                distance[next_node] = distance[source] + graph[source][next_node]
                # print(next_node)
                # path[next_node] = "{}{}".format(path[source],source)
                path[next_node] = path[source].copy()
                path[next_node].append(source)
        INF = float("inf")
        for node in distance.keys():
            if node not in visited and distance[node] < INF:
                INF, source = distance[node], node
    # return distance
    return path


def guide(direction, path, end):
    path[end].append(end)
    res = ""
    for _ in range(len(path[end]) - 1):
        res = "{} {}".format(res, direction[path[end][_]][path[end][_ + 1]])
        # res.append(Direction[path[end][_]][path[end][_ + 1]])
    return res[1:]


class forest(Cog_Extension):
    def pathF1toF2(self, arg, end):
        path = dijkstra(F1toF2_graph, arg)
        text = guide(F1toF2_direction, path, end)
        return text

    def pathF3toF2(self, arg, end):
        path = dijkstra(F3toF2_graph, arg)
        text = guide(F3toF2_direction, path, end)
        return text

    @commands.command()
    async def F11(self, ctx):
        text = self.pathF1toF2(23, 26)
        await ctx.send(text)

    @commands.command()
    async def f11(self, ctx):
        text = self.pathF1toF2(23, 26)
        await ctx.send(text)

    @commands.command()
    async def F12(self, ctx):
        text = self.pathF1toF2(7, 26)
        await ctx.send(text)

    @commands.command()
    async def f12(self, ctx):
        text = self.pathF1toF2(7, 26)
        await ctx.send(text)

    ############################################
    ####指定起始跟終點
    @commands.command()
    async def F1P(self, ctx, arg1, arg2):
        arg1 = int(arg1)
        arg2 = int(arg2)
        if arg1 > 25 or arg1 <= 0:
            text = "起點請輸入數字1~25"
        elif arg2 > 26 or arg2 <= 0:
            text = "終點請輸入數字1~26"
        else:
            text = self.pathF1toF2(arg1, arg2)
        await ctx.send(text)

    @commands.command()
    async def f1p(self, ctx, arg1, arg2):
        arg1 = int(arg1)
        arg2 = int(arg2)
        if arg1 > 25 or arg1 <= 0:
            text = "起點請輸入數字1~25"
        elif arg2 > 26 or arg2 <= 0:
            text = "終點請輸入數字1~26"
        else:
            text = self.pathF1toF2(arg1, arg2)
        await ctx.send(text)

    #######

    @commands.command()
    async def F1(self, ctx, arg):
        arg = int(arg)
        if arg > 25 or arg <= 0:
            text = "請輸入數字1~25"
        else:
            text = self.pathF1toF2(arg, 26)
        await ctx.send(text)

    @commands.command()
    async def f1(self, ctx, arg):
        arg = int(arg)
        if arg > 25 or arg <= 0:
            text = "請輸入數字1~25"
        else:
            text = self.pathF1toF2(arg, 26)
        await ctx.send(text)

    ############################################
    ####指定起始跟終點
    @commands.command()
    async def F3P(self, ctx, arg1, arg2):
        arg1 = int(arg1)
        arg2 = int(arg2)
        if arg1 > 25 or arg1 <= 0:
            text = "起點請輸入數字1~25"
        elif arg2 > 26 or arg2 <= 0:
            text = "終點請輸入數字1~26"
        else:
            text = self.pathF3toF2(arg1, arg2) + "\n若再2、17、19、24圖上，移動一張地圖再計算一次"
        await ctx.send(text)

    @commands.command()
    async def f3p(self, ctx, arg1, arg2):
        arg1 = int(arg1)
        arg2 = int(arg2)
        if arg1 > 25 or arg1 <= 0:
            text = "起點請輸入數字1~25"
        elif arg2 > 26 or arg2 <= 0:
            text = "終點請輸入數字1~26"
        else:
            text = self.pathF3toF2(arg1, arg2) + "\n若再2、17、19、24圖上，移動一張地圖再計算一次"
        await ctx.send(text)

    ############################################
    @commands.command()
    async def F3(self, ctx, arg):
        arg = int(arg)
        if arg > 25 or arg <= 0:
            text = "請輸入數字1~25"
        else:
            text = self.pathF3toF2(arg, 26) + "\n若再2、17、19、24圖上，移動一張地圖再計算一次"
        await ctx.send(text)

    @commands.command()
    async def f3(self, ctx, arg):
        arg = int(arg)
        if arg > 25 or arg <= 0:
            text = "請輸入數字1~25"
        else:
            text = self.pathF3toF2(arg, 26) + "\n若再2、17、19、24圖上，移動一張地圖再計算一次"
        await ctx.send(text)


############################################
def setup(bot):
    bot.add_cog(forest(bot))
