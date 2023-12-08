import discord, datetime
from discord.ext import commands    

class Time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tz = datetime.timezone(datetime.timedelta(hours = 8))
        self.now = datetime.datetime.now(self.tz)

    @commands.command()
    async def time(self, ctx):
        await ctx.send(self.now)

async def setup(bot):
    await bot.add_cog(Time(bot))
