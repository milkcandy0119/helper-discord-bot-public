import discord
from discord import app_commands
from discord.ext import commands

class Slash(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name="slash", description="test slash command")
    async def ping(self, interaction):
        bot_latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! {bot_latency} ms.")
    
    @app_commands.command(name="hello")
    async def hello(slef,interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!",ephemeral=True)

    
async def setup(bot):
    await bot.add_cog(Slash(bot))

    