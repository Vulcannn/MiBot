import discord
import time

from discord.ext import commands


class Commands:
    """Commands for Mibot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong!"""
        await self.bot.say('Pong!')

    @commands.command(pass_context=True)
    async def pingtime(self,ctx):
        """Get your ping time!"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        await self.bot.say(" :ping_pong: Pong! Took: {}ms".format(round((t2-t1)*1000)))
		
    @commands.command(pass_context=True)
    async def info(self, ctx):
        """Info about MiBot!"""
        embed = discord.Embed(title="MiBot", description="A Python Discord Bot", colour=0x1e90ff)
        await self.bot.say(embed=embed)
	
		
def setup(bot):
    bot.add_cog(Commands(bot))
