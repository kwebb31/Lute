import os
import discord
from discord.ext import commands
from ast import alias
from discord.utils import get
import bardRequest
import altBardRequest
import OpenAI
import json
import seleniumTest
currPrefix = '!'
bot = commands.Bot(command_prefix=currPrefix, intents=discord.Intents.all())


@bot.command(aliases=['Start', 'START'])
async def start(ctx):
  await ctx.send(
      "Hi, my name is Lute. I speak on behalf of Bard and I'd love to help you evaluate code snippets, answer your questions in a bardic tone and more. For information about my commands, please type '!List'."
  )


@bot.command(aliases=['List', 'LIST','l'])
async def list(ctx):
  await ctx.send(
      "Currently, my commands are: \n!Start \n!List \n!query \n!QueryS \n !bardic \n!char \n!story \n!image \nPlease feel free to try them all!"
  )


@bot.command(aliases=['query', 'Ask', 'q'])
async def Query(ctx, *, query):
  myQuery = "in 2000 characters or less, Speaking as if you were a bard from dnd 5e, talk about " + query

  result = bardRequest.query(myQuery)

  await ctx.send(result)

@bot.command(aliases=['queryS', 'Serious', 'normal', 'regular'])
async def R(ctx, *, query):
  query+= "in 2000 characters or less, "
  result = bardRequest.query(query)

  await ctx.send(result)


@bot.command(aliases=['v', 'viciousMockery', 'vicious'])
async def ViciousMockery(ctx, *, target):
  query = "in 2000 characters or less, create a fictional insult for a " + target
  result = bardRequest.query(query)
  await ctx.send(result)

@bot.command(aliases=['bardic', 'inspiration', 'Bardic', 'Inspiration', 'i'])
async def bardicInspiration(ctx, *, target):
  myQuery = "create a 5 line inspiring song verse for " + " " + target
  result = bardRequest.query(myQuery)
  final = "A verse to inspire your " + target + ":\n" + result
  await ctx.send(final)

@bot.command(aliases=['char', 'Ch', 'create', 'characterCreation'])
async def CharacterCreation(ctx, *, target):
  query = "in 2000 characters or less, Based on DND 5e rules, create a character " + target
  result = bardRequest.query(query)
  await ctx.send(result)

#calls the gemini API with a string given by the user and the beginnings of a prompt
@bot.command(aliases=['Story', 'S', 's', 'StoryCreation', 'storyCreation'])
async def story(ctx, *, target):
  query = "Write a basic, 2000 letter characters or less short story suited for a DND 5E campaign about " + target
  result = bardRequest.query(query)
  await ctx.send(result)

#calls the query command in the OpenAI file and generates an image from DALL-E
@bot.command(aliases=['image', 'im', 'imageof', 'imageCreation'])
async def Image(ctx, *, target):
  query = "Create an image " + target
  result = OpenAI.query(query)
  await ctx.send(result)
  

my_secret = os.environ['Sneakret']

bot.run(my_secret)

