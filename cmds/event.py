from discord.ext import commands
from core.classes import Cog_Extension
import datetime
from datetime import timezone, timedelta


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, ctx):
        keyword = ['開組ㄌㄇ', '開組了嗎', '開團了?', '開組了ㄇ', 'Edda開了嗎', 'edda開ㄌㄇ',
                   'EDDA開ㄌㄇ', 'EDDA開 講一下', 'edda開組講一下', 'EDDA開了講一下', '還有EDDA嗎',
                   'EDDA打了嗎', '還有團嗎', '有團嗎', '開團']
        if ctx.content in keyword:
            tzutc_8 = timezone(timedelta(hours=8))
            local_time = int(
                datetime.datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tzutc_8).strftime("%H%M"))
            if 2120 > local_time > 2050:
                await ctx.channel.send(f'要打就來據點')
            elif 2359 > local_time > 2120:
                await ctx.channel.send(f'明天請早')
            elif 2049 > local_time > 0000:
                await ctx.channel.send(f'太早了，還沒開團')
        else:
            pass


def setup(bot):
    bot.add_cog(Event(bot))
