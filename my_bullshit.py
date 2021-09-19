import discord
from discord.ext import commands
import os
import requests

class Meme(commands.Cog):
    def __init__(self, client):

        self.client = client




    @commands.command(name="meme", help="Sends memes. You can pass redit and amount (up to 50) as arguments",)
    async def meme(self, ctx, *args):
        if len(args) > 2:
            if int(args[0]) > 50:
                await ctx.send("https://i.ytimg.com/vi/ZEmEtPkd4IQ/hqdefault.jpg")
            else:
                response = requests.get("https://meme-api.herokuapp.com/gimme" + "/" + "/".join(args))
                count = response.json()['count']
                if count < 1:
                    url = response.json()['url']
                    await ctx.send(url)
                else:
                    memes = response.json()['memes']
                    for x in range(count):
                        url = memes[x].get('url')
                        await ctx.send(url)
        else:
            print(args[1])
            if int(args[1]) > 50:
                await ctx.send("https://i.ytimg.com/vi/ZEmEtPkd4IQ/hqdefault.jpg")
            else:
                response = requests.get("https://meme-api.herokuapp.com/gimme" + "/" + "/".join(args))
                count = response.json()['count']
                if count < 1:
                    url = response.json()['url']
                    await ctx.send(url)
                else:
                    memes = response.json()['memes']
                    for x in range(count):
                        url = memes[x].get('url')
                        await ctx.send(url)
