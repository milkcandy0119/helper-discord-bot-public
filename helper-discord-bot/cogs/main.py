import discord, json, datetime, asyncio
from discord.ext import commands
from random import randint

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def countdown(self, ctx, t: int):
        await ctx.send(f"Counting down from {t}s")
        while t > 0:
            t -= 1
            # Sleep for 1 second
            await asyncio.sleep(1)
        await ctx.send("Countdown end reached")
    
    @commands.command()
    async def say(self, ctx, *, message: str):
        await ctx.message.delete()
        await ctx.send(f"Somebody say: {message}")

    @commands.command()
    async def choose(self, ctx, *, message: str):
        array = list(message.split("/"))
        num = len(array)
        rand = randint(0,num-1)
        await ctx.send(f"I think **{array[rand]}** is a good choose")

    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{ctx.author.mention}")

    @commands.command()
    async def probaility_table(self,ctx):
        await ctx.send("( ⁠╹⁠▽⁠╹⁠ ) => 40%\nヾ(≧▽≦)o => 25%\n⁠(⁠☞ﾟ⁠∀*ﾟ)⁠☞ => 25%\nᕙ⁠(⁠＠⁠°⁠▽⁠°⁠＠⁠)⁠ᕗ => 9%\n(((o(*ﾟ▽ﾟ**)o))) => 0.9%\n ଲ(ⓛ ω ⓛ)ଲ 0.1%")

    @commands.command()
    async def dm(self, ctx):
        embed=discord.Embed(title="**小助手 - 簡介**")
        embed.set_thumbnail(url="https://cdn.custom-cursor.com/db/pointer/pointer_2351.png")
        embed.set_author(name="milkcandy0119", url="https://github.com/milkcandy0119", icon_url="https://avatars.githubusercontent.com/u/96375831?v=4")
        embed.add_field(name="Reaction: (p.s. --是可以填字)", 
                        value="打 **--小助手--** → 會和你打招呼\n打 **--的機率** → 會幫你預測分析(迷信不要當真)\n打 **--吃甚麼?** → 會幫你做決定", 
                        inline=False)
        embed.add_field(name="Slash commands:", 
                        value="**/hello** → 打招呼(only you can see)\n**/say** → 你想他說的話(不會匿名)\n**/slash** → bot ping", 
                        inline=False)
        embed.add_field(name="%commands:", 
                        value="**%choose (object_1/object_2/....)** → 做決定\n**%say** → 用機器人講話(匿名)\n**%dm** → 呼叫此列表\n**%ping** → tag 你(測試用指令)\n**%probaility_table** → 小助手打招呼表情機率表\n**%time** → 現在標準時間\n**%countdown (秒數)** → 倒數\n**%help** → 指令表", 
                        inline=False)
        embed.add_field(name="(%)remind me (Bata test version - only save message):", 
                        value="**%login** → 註冊使用權\n**%sign_out** → 刪除使用權\n**%add_event (event_name)** → 新增事件(event_name 不能空格,用底線)\n**%pop_event (event_name)** → 刪除事件(event_name 不能空格,用底線)\n**%show_event** → 列出所有事件\n**%edit_event event_name mode time_form cycle** → 編輯事件提醒時間\n==============\nevent_name 不能空格,用底線\nmode:one_time: just notion one time, repeat: evert -cycle- time will notion\ntime_form: at time: at n(after n days)-n-n-n(accurate time e.g. 23-10-50 = 23:10:50), default -after time-\ncycle: d=天 h=小時 m=分鐘 s=秒 沒有寫0", 
                        inline=False)
        embed.set_footer(text="2023/10/24 edit by milkcandy")
        await ctx.send(embed=embed)

           

async def setup(bot):
    await bot.add_cog(Main(bot))