import discord.utils
import discord
import os
import random
import time

#Piecey Discord Bot.
#By:  ViridianTelamon

client = discord.Client()

token = "Put Discord Bot Token Here."

#On Ready Event.
@client.event
async def on_ready():
  print("Bot Ready.")
  time.sleep(1)
  print("Logged In As:  {0.user}".format(client))

#Poll 1.
async def poll_1(message):
    poll = await message.channel.send("Who Is Better Luffy (🔴) or Zoro (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#Poll 2.
async def poll_2(message):
    poll = await message.channel.send("Who Is Better Nami (🔴) or Robin (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#Poll 3.
async def poll_3(message):
    poll = await message.channel.send("Who Is Better Aokiji (🔴) or Fujitora (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#Poll 4.
async def poll_4(message):
    poll = await message.channel.send("Who Is Better Blackbeard (🔴) or Whitebeard (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#Poll 5.
async def poll_5(message):
    poll = await message.channel.send("Who Is Better Sabo (🔴) or Ace (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#Poll 6.
async def poll_6(message):
    poll = await message.channel.send("Which Fruit Is Better Suke Suke No Mi (🔴) or Mane Mane No Mi (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#Poll 7. 
async def poll_7(message):
    poll = await message.channel.send("Which Fruit Is Better Magu Magu No Mi (🔴) or Yuki Yuki No Mi (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#Poll 8.
async def poll_8(message):
    poll = await message.channel.send("Which Fruit Is Better Ope Ope No Mi (🔴) or Toki Toki No Mi (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#Poll 9.
async def poll_9(message):
    poll = await message.channel.send("Which Fruit Is Better Mera Mera No Mi (🔴) or Doku Doku No Mi (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#Poll 10.
async def poll_10(message):
    poll = await message.channel.send("Which Fruit Is Better Giro Giro No Mi (🔴) or Gasu Gasu No Mi (🔵).")
    await poll.add_reaction("🔴")
    await poll.add_reaction("🔵")

#If The Bot Recieves A Message Event.
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("!poll"):
    poll_list = [poll_1, poll_2, poll_3, poll_4, poll_5, poll_6, poll_7, poll_8, poll_9, poll_10]
    poll_choice = random.choice(poll_list)
    await poll_choice(message)

client.run(token)
