import os
import discord
from discord.ext import commands
from ast import alias
from discord.utils import get
import bardRequest

currPrefix = '!'
bot = commands.Bot(command_prefix=currPrefix, intents=discord.Intents.all())

#prints a welcome blurb and introduces some potential commands
@bot.command(aliases=['Start', 'START'])
async def start(ctx):
  await ctx.send(
      "Hi, my name is Lute. I speak on behalf of Bard and I'd love to help you create a character, create a story, answer your questions in a bardic tone and much more. For information about my commands, please type '!List'."
  )

#lists out all the commands that are currently available
@bot.command(aliases=['List', 'LIST','l', 'Help', 'help'])
async def list(ctx):
  await ctx.send(
      "Currently, my commands are: \n !Start \n !List \n !Code \n !Question \n !Enbard \n !ViciousMockery \n Please feel free to try them all!"
  )

#queries as if the bot is a d&d bard
@bot.command(aliases=['query', 'Ask', 'q'])
async def Query(ctx, *, query):
  myQuery = "Speaking as if you were a bard from dnd 5e, " + query

  result = bardRequest.query(myQuery)

  await ctx.send(result)

#writes an insult for a specific target
@bot.command(aliases=['v', 'viciousMockery', 'vicious'])
async def ViciousMockery(ctx, *, target):
  myQuery = "create some unique pointed fictional insults for a(n) " + " " + target
  result = bardRequest.query(myQuery)
  final = "Some insults for your " + target + ":\n" + result
  await ctx.send(final)

#creates a short inspiring verse for a bard
@bot.command(aliases=['bardic', 'inspiration', 'Bardic', 'Inspiration', 'i'])
async def bardicInspiration(ctx, *, target):
  myQuery = "create a 5 line inspiring song verse for " + " " + target
  result = bardRequest.query(myQuery)
  final = "A verse to inspire your " + target + ":\n" + result
  await ctx.send(final)

#creates a character using the bard query method
@bot.command(aliases=['char', 'Ch', 'create', 'characterCreation'])
async def CharacterCreation(ctx, *, target):
  query = "Based on DND 5e rules, create a character " + target
  result = bardRequest.query(query)
  await ctx.send(result)

#create a story for a DND campaign
@bot.command(aliases=['Story', 'S', 's', 'StoryCreation', 'storyCreation'])
async def story(ctx, *, target):
  query = "Write a story suited for a DND 5E campaign about " + target
  result = bardRequest.query(query)
  await ctx.send(result)



#@bot.command(aliases=['p', 'previous', "Previous"])
#async def prev(ctx):
  

my_secret = os.environ['Sneakret']

bot.run(my_secret)
