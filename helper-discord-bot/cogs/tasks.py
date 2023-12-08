import discord, datetime, json, os
from discord.ext import commands, tasks

with open('milkcandy_class.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

with open('setting.json', mode='r', encoding='utf8') as sfile:
    sdata = json.load(sfile)

with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)

class Task(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.tz = datetime.timezone(datetime.timedelta(hours = 8))
        self.bot = bot
        self.channel_id = jdata["class-notion-channel"]
        self.channel_GSAT = sdata["GSAT"]
        self.class_notion.start()
        self.workday_class.start()
        self.remind_me.start()

    def main(self, td_weekday, on_class, number):
        if number == 0:
            return jdata['class'][td_weekday][on_class]['name']
        elif number == 1:
            return jdata['class'][td_weekday][on_class]['classroom']
        elif number == 2:
            return jdata['class'][td_weekday][on_class]['teacher']
        elif number == 3:
            return jdata['class'][td_weekday][on_class]['number']


    @commands.command()
    async def today_class(self,ctx): 
        today = datetime.date.today()
        week = today.isoweekday()-1 # for json list
        if today.isoweekday() >=1 and today.isoweekday() <= 5:
            embed = discord.Embed(title="今日課表", color = discord.Color.random())
            for i in range (0, 10):
                embed.add_field(name=f"{self.main(week, i, 0)}({i+8}:10)",
                                value=f"教室: {self.main(week, i, 1)}\n教授: {self.main(week, i, 2)}\n座號: {self.main(week, i, 3)}",
                                inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("今天是假日~")

    @tasks.loop(seconds = 1)
    async def workday_class(self):
        now = datetime.datetime.now(self.tz)
        future = datetime.date(2024,1,20)
        today = datetime.date.today()
        week = today.isoweekday()-1 # for json list
        day = future - today
        channel = self.bot.get_channel(self.channel_id)
        channel_2 = self.bot.get_channel(self.channel_GSAT)
        if today.isoweekday() >= 1 and today.isoweekday() <= 5:
            if now.hour == 7 and now.minute == 0 and now.second == 0:
                embed = discord.Embed(title="今日課表", color = discord.Color.random())
                for i in range (0, 10):
                    embed.add_field(name=f"{self.main(week, i, 0)}({i+8}:10)",
                                    value=f"教室: {self.main(week, i, 1)}\n教授: {self.main(week, i, 2)}\n座號: {self.main(week, i, 3)}",
                                    inline=False)
                await channel.send(embed=embed)

        if (now.hour == 7 and now.minute == 0 and now.second == 0) or (now.hour == 21 and now.minute == 0 and now.second == 0):
            await channel_2.send(f"<@{807884725023932418}>") #這個人在敷衍我
            await channel_2.send(f"<@{605345372948135974}>") #迷隻順順胖胖的
            await channel_2.send(f"<@{1112994573552205938}>") #壽壽的人
            embed = discord.Embed(title="今日課表", color = discord.Color.random())
            embed = discord.Embed(title="學測倒數", color = discord.Color.random())
            embed.add_field(name=f"學測日期: 2024/1/20~1/22",value=f"你還有 **{day.days}** 天可以擺爛讀書喔~",inline=False)
            await channel_2.send(embed=embed)

    @tasks.loop(seconds = 1)
    async def class_notion(self):
        #os.system("cls")
        now = datetime.datetime.now(self.tz)
        today = datetime.date.today()
        week = today.isoweekday-1 # for json list
        channel = self.bot.get_channel(self.channel_id)
        #print(f"系統時間 = {now.hour} : {now.minute} : {now.second}")

        if today.isoweekday() >= 1 and today.isoweekday() <= 5:
            if now.hour == 8 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-1", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 0, 0)}(8:10)", 
                                value=f"教室: {self.main(week, 0, 1)}\n教授: {self.main(week, 0, 2)}\n座號: {self.main(week, 0, 3)}",
                                inline=False)
                await channel.send(embed = embed)
            
            if now.hour == 9 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-2", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 0, 0)}(9:10)", 
                                value=f"教室: {self.main(week, 1, 1)}\n教授: {self.main(week, 1, 2)}\n座號: {self.main(week, 1, 3)}",
                                inline=False)
                await channel.send(embed = embed)
            
            if now.hour == 10 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-3", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 2, 0)}(10:10)", 
                                value=f"教室: {self.main(week, 2, 1)}\n教授: {self.main(week, 2, 2)}\n座號: {self.main(week, 2, 3)}",
                                inline=False)
                await channel.send(embed = embed)
            
            if now.hour == 11 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-4", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 3, 0)}(11:10)", 
                                value=f"教室: {self.main(week, 3, 1)}\n教授: {self.main(week, 3, 2)}\n座號: {self.main(week, 3, 3)}",
                                inline=False)
                await channel.send(embed = embed)
            
            if now.hour == 12 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-5", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 4, 0)}(12:10)", 
                                value=f"教室: {self.main(week, 4, 1)}\n教授: {self.main(week, 4, 2)}\n座號: {self.main(week, 4, 3)}",
                                inline=False)
                await channel.send(embed = embed)
            
            if now.hour == 13 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-6", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 5, 0)}(13:10)", 
                                value=f"教室: {self.main(week, 5, 1)}\n教授: {self.main(week, 5, 2)}\n座號: {self.main(week, 5, 3)}",
                                inline=False)
                await channel.send(embed = embed)
            
            if now.hour == 14 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-7", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 6, 0)}(14:10)", 
                                value=f"教室: {self.main(week, 6, 1)}\n教授: {self.main(week, 6, 2)}\n座號: {self.main(week, 6, 3)}",
                                inline=False)
                await channel.send(embed = embed)
            
            if now.hour == 15 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-8", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 7, 0)}(15:10)", 
                                value=f"教室: {self.main(week, 7, 1)}\n教授: {self.main(week, 7, 2)}\n座號: {self.main(week, 7, 3)}",
                                inline=False)
                await channel.send(embed = embed)
            
            if now.hour == 16 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-9", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 8, 0)}(16:10)", 
                                value=f"教室: {self.main(week, 8, 1)}\n教授: {self.main(week, 8, 2)}\n座號: {self.main(week, 8, 3)}",
                                inline=False)
                await channel.send(embed = embed)
            
            if now.hour == 17 and now.minute == 0 and now.second == 0: 
                embed=discord.Embed(title="上課通知-10", color=discord.Color.random())
                embed.add_field(name=f"{self.main(week, 9, 0)}(17:10)", 
                                value=f"教室: {self.main(week, 9, 1)}\n教授: {self.main(week, 9, 2)}\n座號: {self.main(week, 9, 3)}",
                                inline=False)
                await channel.send(embed = embed)

    @tasks.loop(seconds = 1)
    async def remind_me(self):
        channel = self.bot.get_channel(1164590104581521469)
        with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)
        now = datetime.datetime.now(self.tz)
        today = datetime.date.today()
        if data != {}:
            keylist = list(data.keys())
            amount = len(keylist)
            if amount != 0:
                for i in range(0,amount):
                    event_key = list(data[f'{keylist[i]}'])
                    for j in range(0, len(event_key)):
                        if data[f'{keylist[i]}'][f'{event_key[j]}'] == {}:
                            continue
                        else:
                            print(event_key[j])
                            cycle = str(data[f'{keylist[i]}'][f'{event_key[j]}']['cycle']).split("-")
                            print(cycle)
                            update = str(data[f'{keylist[i]}'][f'{event_key[j]}']['update_time']).split(" ")
                            update_date = update[0].split("-")
                            update_time = update[1].split(":")
                            mode = str(data[f'{keylist[i]}'][f'{event_key[j]}']['mode'])
                            time_form = str(data[f'{keylist[i]}'][f'{event_key[j]}']['time_form'])
                            start = datetime.datetime(int(update_date[0]), int(update_date[1]), int(update_date[2]), int(update_time[0]), int(update_time[1]), int(update_time[2][:-7]))
                            now_date = datetime.datetime(now.year ,now.month, now.day, now.hour, now.minute, now.second)
                            print("into if")
                            if time_form == "after_time":
                                print("after time start")
                                result_date = start + datetime.timedelta(days=int(cycle[0]), hours=int(cycle[1]), minutes=int(cycle[2]), seconds=int(cycle[3]))
                                print("after time end")
                            else:
                                print("at start")
                                result_date = datetime.datetime(int(update_date[0]), int(update_date[1]), int(update_date[2])+int(cycle[0]), int(cycle[1]), int(cycle[2]), int(cycle[3]))
                                print("at end")
                            if now_date == result_date:
                                if mode == "one_time":
                                    print(f"{event_key[j]} one_time")
                                    await channel.send(f"<@{keylist[i]}> **{event_key[j]}**")
                                else:
                                    print(f"{event_key[j]} repeat")
                                    data[f'{keylist[i]}'][f'{event_key[j]}'].update({'update_time': f'{str(today).split()[0]} {str(now.time())}'})
                                    with open('data.json', 'w', encoding='utf-8') as f:
                                        json.dump(data, f, indent = '\t')
                                    await channel.send(f"<@{keylist[i]}> **{event_key[j]}**")  
   
            

async def setup(bot):
    await bot.add_cog(Task(bot))