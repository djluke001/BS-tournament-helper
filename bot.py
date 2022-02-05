# bot.py
import os
import time
import discord
watch_list=[]
TOKEN = 'redacted'

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
       

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
@client.event

async def on_message(message):
    if message.author == client.user:
        return
    print("here")
    if message.content == '/start' and message.author.guild_permissions.mute_members:
        vc=message.author.voice.channel
        print (vc.members)
        for member in vc.members:
            print(member)
            await member.edit(mute=True)
        await message.channel.send("muteing all in channel",tts=True)
    if message.content == '/end' and message.author.guild_permissions.mute_members:
        print("wrong")
      
        for member in message.author.voice.channel.members:
            await member.edit(mute=False)
        await message.channel.send("members unmuted",tts=True)
        mess= await message.channel.send("would you like a replay or a bread",delete_after=60.0)
        await mess.add_reaction('\N{THUMBS DOWN SIGN}')
        await mess.add_reaction('\N{BREAD}')
        await mess.add_reaction('\N{THUMBS UP SIGN}')
        watch_list.append(mess)
        watch_list.append((time.time()+45))
@client.event
async def on_reaction_add(reaction, user):
    if user != client.user:
        await reaction.message.channel.send((str(user)+" reacted "+str(reaction.emoji)))
        
client.run(TOKEN)
