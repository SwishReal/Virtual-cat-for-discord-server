# EDIT THE BOT BEFORE USING IT
# Bot authon - @swishyt

import discord
from discord.ext import commands
import pickle

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

global feed_stats
feed_stats = 0
global stroke_stats
stroke_stats = 0

try:
    with open('feed.txt', 'rb') as fed:
        feed_stats = pickle.load(fed)

    with open('stroke.txt', 'rb') as str:
        stroke_stats = pickle.load(str)
    print('save file is found')
    print('stats = ',feed_stats, stroke_stats)
except FileNotFoundError:
        with open('feed.txt', 'wb') as fed:
            pickle.dump(feed_stats, fed, protocol=pickle.HIGHEST_PROTOCOL)

        with open('stroke.txt', 'wb') as str:
            pickle.dump(stroke_stats, str, protocol=pickle.HIGHEST_PROTOCOL)
        print("save file is not found, creating new file")

@bot.command()
async def feed(ctx):
    global feed_stats
    feed_stats = feed_stats + 1
    with open('feed.txt', 'wb') as fed:
        pickle.dump(feed_stats, fed, protocol=pickle.HIGHEST_PROTOCOL)
        print("feed_stats saving")
    await ctx.send(f"Text {feed_stats}")

@bot.command()
async def stroke(ctx):
    global stroke_stats
    stroke_stats = stroke_stats + 1
    with open('stroke.txt', 'wb') as str:
        pickle.dump(stroke_stats, str, protocol=pickle.HIGHEST_PROTOCOL)
        print('stroke_stats saving')
    await ctx.send(f"Text {stroke_stats}")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="List of commands", description="В кратце узнаете о всех командах для моего бота 'Сеня <3'")
    embed.add_field(name="field", value=f"description")
    embed.set_footer(text="footer")
    embed.set_thumbnail(url="image url")
    await ctx.send(embed=embed)

@bot.command()
async def changelog(ctx):
    embed = discord.Embed(title="Changelog", description="your bot name")
    embed.add_field(name="Возможность сохранить статистику", value=f"description")
    embed.set_footer(text="footer")
    embed.set_thumbnail(url="image url")
    await ctx.send(embed=embed)

@bot.command()
async def статистика(ctx):
    global feed_stats
    global stroke_stats
    embed = discord.Embed(title="Statistics", description="Description")
    embed.add_field(name="How many times have you been fed?", value=f"text {feed_stats}! text")
    embed.add_field(name="How many times ironed?", value=f"text {stroke_stats}! text")
    embed.set_footer(text="footer")
    embed.set_thumbnail(url="https://i.postimg.cc/d1wR7VN6/senya.webp")
    await ctx.send(embed=embed)

bot.run('Your token')