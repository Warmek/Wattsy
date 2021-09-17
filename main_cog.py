import discord
from discord.ext import commands

import music_cog

class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.admin = 'Dr.Warmek#7292'
        self.help_message = """
```
General commands:
/help - displays all the available commands
/clear amount - will delete the past messages with the amount specified

Image commands:
/search <keywords> - will change the search to the keyword
/get - will get the image based on the current search

Music commands:
/p <keywords> - finds the song on youtube and plays it in your current channel
/q - displays the current music queue
/skip - skips the current song being played
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        #await self.send_to_all(self.help_message)


        await self.bot.change_presence(activity=discord.Game(name="Yo mama"))


        print("Bot ready")

    """
        @commands.command(name="help", help="Displays all the available commands")
        async def help(self, ctx):
            await ctx.send(self.help_message)

        async def send_to_all(self, msg):
            for text_channel in self.text_channel_list:
                await text_channel.send(msg)
    """

    @commands.command(name="invite", help="Generates invite link")
    async def invite_link(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=717745411594387625&permissions=8&scope=bot")

    @commands.command(name="say", help="Makes bot say things", pass_context=True)
    async def say(self, ctx, *, mg=None):
        await commands.delete_message(ctx.message)

        if not mg:
            await self.bot.say("Please specify a message to send")
        else:
            await self.bot.say(mg)

    @commands.command(name="speak", pass_context=True)
    async def speak(self, ctx, *args):
        if (str(ctx.message.author) == self.admin):
            await ctx.channel.purge(limit=1)
            text = " ".join(args)
            await ctx.send(text)
        else:
            await ctx.send("<https://www.youtube.com/watch?v=dQw4w9WgXcQ>")

    @commands.command(name="Kill_him", pass_context=True)
    async def kh(self, ctx, number : int):
        if (str(ctx.message.author) == self.admin):
            await ctx.channel.purge(limit=number+1)
        else:
            await ctx.send("<https://www.youtube.com/watch?v=dQw4w9WgXcQ>")


    @commands.command(name="clean_up", help="Clears a specified amount of messages")
    async def clean_up(self, ctx, arg):
        #extract the amount to clear
        amount = 5
        try:
            amount = int(arg)
        except Exception: pass

        await ctx.channel.purge(limit=amount)
