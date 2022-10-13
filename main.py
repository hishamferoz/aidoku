#import
import os
import time
import discord
import discord.ext
from discord.ext import commands
import random
import discord
import aiohttp




  
#intent
intent = discord.Intents.all()
intent.members = True
intent.message_content = True

#prefix
client = commands.Bot(command_prefix="!", intents=intent)


#bot is ready
@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))


#ping
@client.command()
async def ping(ctx):
  before = time.monotonic()
  message = await ctx.send("🏓  Pong!")
  ping = (time.monotonic() - before) * 1000
  await message.edit(content=f"🏓  Pong!  `{int(ping)}ms`")


#hello
@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('hello , wassup !')


#coinflip
determine_flip = [1, 0]


@client.command()
async def toss(ctx):
  if random.choice(determine_flip) == 1:
    embed = discord.Embed(
      title="🪙 Coinflip",
      description=f"{ctx.author.mention} Flipped coin, we got **Heads**!")
    embed.set_image(
      url="https://media.tenor.com/nEu74vu_sT4AAAAM/heads-coinflip.gif")
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(
      title="🪙 Coinflip",
      description=f"{ctx.author.mention} Flipped coin, we got **Tails**!")
    embed.set_image(
      url="https://media.tenor.com/kK8D7hQXX5wAAAAM/coins-tails.gif")
    await ctx.send(embed=embed)


#welcome
@client.event
async def on_member_join(member):
  channel = client.get_channel(730128671133663283)
  embed = discord.Embed(title="Welcome!",
                        description=f"{member.mention} Just Joined")
  await channel.send(embed=embed)


#avatar
@client.command()
async def avatar(ctx,
                 *,
                 member: discord.Member = None
                 ):  # set the member object to None
  if not member:  # if member is no mentioned
    member = ctx.message.author  # set member as the author
  userAvatar = member.avatar.url
  await ctx.send(userAvatar)


#meme
@client.command(pass_context=True)
async def meme(ctx):
  embed = discord.Embed(title="Meme", description="Dank Memes")

  async with aiohttp.ClientSession() as cs:
    async with cs.get(
        'https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
      res = await r.json()
      embed.set_image(
        url=res['data']['children'][random.randint(0, 25)]['data']['url'])
      await ctx.send(embed=embed)


#token
my_secret = os.environ['Token']
client.run(my_secret)

#network


