import discord
from discord.ext import commands
import datetime
import json

with open("config.json") as f:
    config = json.load(f)


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    guild_owner_id = config["GUILD_OWNER_ID"]
    guild_owner = bot.get_user(guild_owner_id)
    print(f"Let's Go {guild_owner}!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)




@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  req_msg = ("hi","hello","hey","helo")
  wish_msg = ("good morning","gm","morning","good afternoon","afternoon","good evening","evening","good night","gn","night")
  author = message.author
  current_time = datetime.datetime.today().hour
  
  if message.content.lower() in req_msg:
    await message.channel.send(f"Hello, {author.mention}!!!")
  
    if 5 <= current_time < 12:
      await message.channel.send(f"Good Morning!")
      return
    
    elif 12 <= current_time < 16:
      await message.channel.send(f"Good Afternoon!")
      return
    
    elif 16 <= current_time < 20:
      await message.channel.send(f"Good Evening!")
      return
  
  # elif 20 <= current_time < 24 or 0 <= current_time < 5:
  #   await message.channel.send(f"Good Night!")
    
  elif  message.content.lower() in wish_msg:
    if 5 <= current_time < 12:
      await message.channel.send(f"Good Morning, {author.mention}!")
      return
  
    elif 12 <= current_time < 16:
      await message.channel.send(f"Good Afternoon, {author.mention}!")
      return
  
    elif 16 <= current_time < 20:
      await message.channel.send(f"Good Evening, {author.mention}!")
      return
    
    elif 20 <= current_time < 24 or 0 <= current_time < 5:
      await message.channel.send(f"Good Night, {author.mention}!")
      return



@bot.event
async def on_voice_state_update(member, before, after):
  if int(member.id) != config["GUILD_OWNER_ID"]:
    print(member.id)
    return
  print("All ok")
  if before.channel == None and after.channel != None:
    await after.channel.connect()
    
  elif before.channel != None and after.channel != None:
    voice_client = discord.utils.get(bot.voice_clients, guild=member.guild)
    await voice_client.disconnect()
    await after.channel.connect()
    
  elif before.channel != None and after.channel == None:
    voice_client = discord.utils.get(bot.voice_clients, guild=member.guild)
    await voice_client.disconnect()

































  
with open("token.txt") as file:
  token = file.read()

bot.run(token)
