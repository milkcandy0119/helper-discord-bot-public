import discord, os, asyncio, json
from discord.ext import commands
from discord import app_commands

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

# client is connect with discord, intents is requare for bot premissions
intents = discord.Intents.all() #all premission
bot = commands.Bot(command_prefix = '%', intents = intents)

# if bot is on
@bot.event
async def on_ready():
    os.system("cls")
    activity = discord.Game(name = "use %dm to start")
    await bot.change_presence(status = discord.Status.idle, activity = activity)
    print(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)") # len => length
    except Exception as e:
        print(e)

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: '{thing_to_say}'")

# load command code file
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# unload command file
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# reload command file
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")

# when start the bot, it will load all commeand file
async def load_extensions():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(jdata['bot-token'])


# if this file is .py
if __name__ == "__main__":
    asyncio.run(main())

    