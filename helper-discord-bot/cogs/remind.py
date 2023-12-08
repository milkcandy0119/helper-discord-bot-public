import discord, json, datetime, asyncio
from discord.ext import commands, tasks

with open('setting.json', mode='r', encoding='utf-8') as s:
    sdata = json.load(s)

with open('data.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)

class Remind(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tz = datetime.timezone(datetime.timedelta(hours = 8))
        # self.remind_me.start()

    def time(self):
        now = datetime.datetime.now(self.tz)
        print(f"系統時間 = {now.hour} : {now.minute} : {now.second}")

    @commands.command()
    async def login(self, ctx):
        with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)

        if f'{ctx.author.id}' in data:
             await ctx.send(f"You are already login!")
             await ctx.send(f"You say {data[f'{ctx.author.id}']}")    
        else:
            data.update({f'{ctx.author.id}' : {}})
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent = '\t')
            await ctx.send(f"Got it, {ctx.author.mention} is login now!") 
        print(data)
        self.time()

    @commands.command()
    async def sign_out(self, ctx):
        with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)
            
        print(data)
        if f'{ctx.author.id}' in data:
            data.pop(f"{ctx.author.id}")
            await ctx.send(f"You are sign out!")
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent = '\t')
        else:
            await ctx.send(f"{ctx.author.mention} you are not login!") 
        print(data)
        self.time()

    @commands.command()
    async def add_event(self, ctx, *, message):
        with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)
        user_id = ctx.author.id
        if f'{user_id}' in data:
            if message in data[f'{user_id}']:
                await ctx.send(f"**{message}** is already in your list")
            else:
                data[f'{user_id}'].update({f'{message}': {}})
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent = '\t')    
                await ctx.send(f"finish! **{message}** add to your event")   
        else:
            await ctx.send(f"{ctx.author.mention} is not login! pls try again before u login")
        print(data)
        self.time()
    
    @commands.command()
    async def pop_event(self, ctx, *, message):
        with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)
        user_id = ctx.author.id
        if f'{user_id}' in data:
            if message in data[f'{user_id}']:
                data[f'{user_id}'].pop(f'{message}')
                with open('data.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent = '\t') 
                await ctx.send(f"Successful pop **{message}** from {ctx.author.mention}'s event list!")
            else:
                await ctx.send(f"There is no **{message}** in your event list")
        else:
            await ctx.send(f"{ctx.author.mention} is not login! pls try again before u login")
        print(data)
        self.time()
    
    @commands.command()
    async def show_event(self, ctx):
        with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)
        user_id = ctx.author.id
        if f'{user_id}' in data:
            cmp = list(data[f'{user_id}'].keys())
            await ctx.send(f"find {len(data[f'{user_id}'])} event in your list")
            await ctx.send(cmp)
        else:
            await ctx.send(f"{ctx.author.mention} is not login! pls try again before u login")
        print(data)
        self.time()

    @commands.command()
    async def edit_event(self, ctx, *, message):
        with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)
        today = datetime.datetime.today()
        now = datetime.datetime.now(self.tz)
        array = list(message.split(" ")) # name mode time_form cycle
        user_id = ctx.author.id
        if f'{user_id}' in data:
            if f'{array[0]}' in data[f'{user_id}']:
                if (array[1] == "one_time") or (array[1] == "repeat"):
                    if array[2] == "at":
                        data[f'{user_id}'][f'{array[0]}'].update({'mode': f'{array[1]}',
                                                                  'time_form': f'{array[2]}',
                                                                  'cycle': f'{array[3]}',
                                                                  'update_time': f'{str(today).split()[0]} {str(now.time())}'})
                    else:
                        data[f'{user_id}'][f'{array[0]}'].update({'mode': f'{array[1]}',
                                                                  'time_form': 'after_time',
                                                                  'cycle': f'{array[2]}',
                                                                  'update_time': f'{str(today).split()[0]} {str(now.time())}'})
                    with open('data.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent = '\t')
                    await ctx.send(f"Successful, the event **{array[0]}** is edited")
                else:
                    await ctx.send(f"Something wrong ! pls check your form (%edit_event name mode time_form cycle)")
        #         data[f'{user_id}'][f'{array[0]}'].update({'cycle': f'{array[1]}',
        #                                                   'update_time': f'{str(today).split()[0]} {str(now.time())}'})
        #         with open('data.json', 'w', encoding='utf-8') as f:
        #             json.dump(data, f, indent = '\t')
        #         await ctx.send(f"Successful, the event **{array[0]}**'s cycle setting to every **{array[1]}** remind 1 time")
        #     else:
        #         await ctx.send(f"There is no **{array[0]}** in your list")
        # else:
        #     await ctx.send(f"{ctx.author.mention} is not login! pls try again before u login")
    


async def setup(bot):
    await bot.add_cog(Remind(bot))


# {
#     "ID": {
#         "event-1": {
#            "mode": ""
#            "cycle":"",
#            "update_time": ""
#         }
#     }
# }

# mode: 
# one_time: just notion one time
# repeat: evert "cycle" time will notion
# time_form: 
# at time: at n(after n days)-n-n-n(accurate time e.g. 23-10-50 = 23:10:50)
# default after time