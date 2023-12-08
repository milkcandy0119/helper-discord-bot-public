import discord, json, time, asyncio
from discord.ext import commands
from random import randint

with open('food.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if message.content == "hello":
            await message.channel.send("hello!")
        
        if "五條悟" in message.content:
            await message.channel.send("~~2.5條悟~~")
        
        if message.content == "誇我":
            id = 807884725023932418
            #message.author.mention
            await message.channel.send(f"{message.author.mention} YYDS!!!")
            time.sleep(1)
            await message.channel.send(f"{message.author.mention} 大佬!!!")
            time.sleep(1)
            await message.channel.send(f"{message.author.mention} 電爛!!!")
            time.sleep(1)
            await message.channel.send(f"{message.author.mention} 椒麻!!!")
        
        if  (message.content == "OwO") or (message.content == "owo") :
            await message.channel.send("OuO") 

        if message.content.endswith("的機率"):
            await message.channel.send(f'{randint(1, 99)} %')
        
        if message.content.endswith("吃甚麼?") or message.content.endswith("吃甚麼？") or message.content.endswith("吃什麼?") or message.content.endswith("吃什麼？"):
            food = randint(1, 3)
            if food == 1:
                eat = randint(0, len(jdata['rice'])-1)
                await message.channel.send(f"{jdata['rice'][eat]}")
            if food == 2:
                eat = randint(0, len(jdata['noodle'])-1)
                await message.channel.send(f"{jdata['noodle'][eat]}")
            if food == 3:
                eat = randint(0, len(jdata['other'])-1)
                await message.channel.send(f"{jdata['other'][eat]}")
            
        if "小助手" in message.content:
            text_random = randint(1, 1000)
            if text_random <= 400:
                await message.channel.send("( ╹⁠▽⁠╹⁠ )")
            elif text_random <= 650:
                await message.channel.send("ヾ(≧▽≦)o")
            elif text_random <= 900:
                await message.channel.send("(⁠☞ﾟ⁠∀*ﾟ)⁠☞")
            elif text_random <= 990:
                await message.channel.send("ᕙ⁠(⁠＠⁠°⁠▽⁠°⁠＠⁠)⁠ᕗ")
            elif text_random <= 999:
                await message.channel.send("(((o(*ﾟ▽ﾟ**)o)))")
            else:
                await message.channel.send("ଲ(ⓛ ω ⓛ)ଲ")
     
async def setup(bot):
    await bot.add_cog(React(bot))
