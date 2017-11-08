'''
A COG BY ME ~ NOBLE
'''
from __future__ import division
import discord
import operator
import asyncio
import random
import time
import datetime
import io
import aiohttp
import json
import PIL
import os
import shutil
import requests
import urllib.parse
import urbanasync
import glob
import moviepy.editor as mpy
from discord.ext import commands
from bs4 import BeautifulSoup
from sympy import solve
from PIL import Image,ImageFilter,ImageDraw,ImageFont
from discord.ext import commands
from discord.ext import commands
from ext.utility import parse_equation
from ext.colours import ColorNames
from random import randint, choice

class Noble:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def textgif(self,ctx,*,args):
        '''Turn TEXT to GIF'''
        img = Image.new('RGB', (500, 45),"black")
        d = ImageDraw.Draw(img)
        c = 0
        length = int(len(args))
        font = ImageFont.truetype('Tabitha.ttf', 27)
        for m in range(length):
            x = 9
            d.text((x+c, 5), args[m], fill=(255, 255, 255), font = font)
            img.save('{}.png'.format(m))
            c += 12
        gif_name = 'content'
        fps = 10
        file_list = glob.glob('*.png') # Get all the pngs in the current directory
        list.sort(file_list) # Sort the images by #, this may need to be tweaked for your use case
        clip = mpy.ImageSequenceClip(file_list, fps=fps)
        clip.write_gif('{}.gif'.format(gif_name), fps=fps)
        await ctx.send(file=discord.File('content.gif'))
        await ctx.message.delete()
        for f in glob.glob("*.png"):
            os.remove(f)

    @commands.command()
    async def pil(self, ctx,args, *,member : discord.Member=None):
        '''A SIMPLE DEMO FOR WELCOMING (DEV)'''
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        url = avi
        response = requests.get(url, stream=True)
        with open('img.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        img = Image.open("img.png")
        img.thumbnail((200, 200))
        new_im = Image.new("RGBA", (400,400))
        img.thumbnail((150,150))
        new_im.paste(img,(100,100))
        font = ImageFont.truetype('arial.ttf', 19)
        xoff, yoff = (10,5)
        d = ImageDraw.Draw(new_im)
        d.text((90, 280), args, fill="white",font = font)
        new_im.save("on_test.png")
        await ctx.send(file=discord.File('on_test.png'))
        await ctx.message.delete()

    @commands.command()
    async def pictext(self,ctx,*,args):
        '''Turn Text to PIC'''
        font = ImageFont.truetype('arial.ttf', 21)
        xoff, yoff = (10,5)
        img = Image.new('RGB', (500, 45),'black')
        d = ImageDraw.Draw(img)
        d.text((9, 5), args, fill="white",font = font)
        img.save('content.jpeg')
        await ctx.message.delete()
        await ctx.send(file=discord.File('content.jpeg'))

 



def setup(bot):
    bot.add_cog(Noble(bot))
