import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import datetime

Client = discord.Client()
client = commands.Bot(command_prefix = "=")                                                                                                                                                                                     

@client.event
async def on_ready() :
    print("Teddy's Lair is ready")
    await client.change_presence(game=discord.Game(name='your heart',type = 2))
    
@client.event
async def on_message(message) :

#TEXT COMMANDS
    
    if message.content == '(╯°□°）╯︵ ┻━┻':
        await client.send_message(message.channel, '┬─┬ ノ( ゜-゜ノ)')
    if message.content == '(╯・ω・）╯︵ ┻━┻':
        await client.send_message(message.channel, '┬─┬ ノ( ゜-゜ノ)')
            
    if message.content.upper().startswith('=PING'):
        await client.send_message(message.channel, '<a:Ping:469517756144943107>')
    if message.content.upper().startswith('=FUNNY'):
        await client.send_message(message.channel, 'Hahaha that was funny')

#EMBED COMMANDS

    if message.content.upper().startswith ('=PFP'):
        if (message.mentions.__len__()>0):
            userID = message.author.id
            for user in message.mentions:
                target = user.id
                embed = discord.Embed(title="Looks like this", description= '<@%s>, here is <@%s>\'s pfp' % (userID,target), color=0xecce8b)
                embed.set_image(url=(user.avatar_url))
                await client.send_message(message.channel, embed=embed)

#HELP
                
    if message.content.upper().startswith('=HELP'):
        embed=discord.Embed(title="Is someone confused ? ", description="Prefix : \"=\" \n \n react-help : A list of every reaction command available \n misc-help : A list of miscellaneous commands available" , color=0xecce8b)
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('=REACT-HELP'):
        embed=discord.Embed(title="Here is a list of reactions available", description="Prefix \"=\" ** ** \n \n attention\n bad \n blush \n hug \n kiss \n lick (@) \n pat \n poke \n smooch \n waaa \n wave \n wink (@) \n wonk (@)" , color=0xecce8b)
        await client.send_message(message.channel, embed=embed)
        
    if message.content.upper().startswith('=MISC-HELP'):
        embed=discord.Embed(title="Is someone confused ? ", description="Prefix : \"=\" \n \n ping : Ping the bot to check for latency \n funny : get the bot to ~~sarcastically~~ laugh at a joke \n pfp @user : get @user's profile picture" , color=0xecce8b)
        await client.send_message(message.channel, embed=embed)

#SECRET COMMANDS

    if message.content.upper().startswith('<@460607074896838656> SHOW ME WHAT A CUTIE LOOKS LIKE'):
        userID = message.author.id
        user = message.server.get_member("330106731965186048")
        pfp = user.avatar_url
        embed=discord.Embed(title="Enquiry results", description='<@%s>, my advanced AI has determined that this is what a cutie looks like' % (userID) , color=0xecce8b)
        embed.set_image(url=(pfp))
        await client.send_message(message.channel, embed=embed)
        
    if message.content.upper().startswith('<@460607074896838656> SHOW ME WHAT A HOTTIE LOOKS LIKE'):
        userID = message.author.id
        user = message.server.get_member("458208941982220298")
        pfp = user.avatar_url
        embed=discord.Embed(title="Enquiry results", description='<@%s>, my advanced AI has determined that this is what a hottie looks like' % (userID) , color=0xecce8b)
        embed.set_image(url=(pfp))
        await client.send_message(message.channel, embed=embed)

#REACTS
                    
    if message.content.upper().startswith('=POKE'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="OwO What's this", description='<@%s> poked <@%s>' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/Jn6c2Ua.gif")
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="Em okay", description='<@%s> tried to poke air :eyes:' % (userID), color=0xecce8b)
            await client.send_message(message.channel, embed=embed)
        
    if message.content.upper().startswith('=HUG'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="OwO What's this", description='<@%s> hugged <@%s>' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/JKIRV2p.gif")
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="Aaaw, you have no one to hug :c", description='Here\'s a hug for you anyways <@%s>' % (userID), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/JKIRV2p.gif")
            await client.send_message(message.channel, embed=embed)
            
    if message.content.upper().startswith('=PAT'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="OwO What's this", description='<@%s> is patting <@%s>' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/0f02xHg.gif")
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="Aaaw, you don't have anyone to pat :c", description='Here, have a pat instead <@%s> umu' % (userID), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/0f02xHg.gif")
            await client.send_message(message.channel, embed=embed)          
        
    if message.content.upper().startswith('=ATTENTION'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="OwO What's this", description='<@%s> wants <@%s>\'s attention >u<' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/loPPLXh.gif")
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="OwO What's this", description='<@%s> wants someone\'s attention umu' % (userID), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/loPPLXh.gif")
            await client.send_message(message.channel, embed=embed)
            
    if message.content.upper().startswith('=KISS'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="OwO What's this", description='<@%s> kissed <@%s> :heart:' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/bFClMnA.gif")
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="Aww, someone wants a kiss uwu", description='I\'m sure at least someone wants to kiss <@%s> >w<' % (userID), color=0xecce8b)
            await client.send_message(message.channel, embed=embed)
        
    if message.content.upper().startswith('=SMOOCH'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="OwO What's this", description='<@%s> smooched <@%s> >u<' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/nvNqnDA.gif")
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="Aaaw, you don't have anyone to smooch umu", description='Here you go, I\'ll give you a smooch <@%s> >u<' % (userID), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/nvNqnDA.gif")
            await client.send_message(message.channel, embed=embed)
        
    if message.content.upper().startswith('=BAD'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="Oh no :c", description='<@%s> is angry at <@%s>' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/TKUSeaQ.gif")
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="Hmmmm", description='<@%s> seems angry :thinking:' % (userID), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/TKUSeaQ.gif")
            await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('=WAVE'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="Aww look >u<", description='<@%s> is waving at <@%s> >w<' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/s2DEVLh.gif")
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="Aww look >u<", description='<@%s> is waving >u>' % (userID), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/s2DEVLh.gif")
            await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('=WAAA'):
        userID = message.author.id
        embed = discord.Embed(title="Oh no :c", description='<@%s> seems sad ;n;' % (userID), color=0xecce8b)
        embed.set_image(url="https://i.imgur.com/Bf3e5Zi.gif")
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('=BLUSH'):
        userID = message.author.id
        embed = discord.Embed(title="Awwww", description='<@%s> is blushing, I wonder why >u>' % (userID), color=0xecce8b)
        embed.set_image(url="https://i.imgur.com/DknDUn6.gif")
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('=LICK'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="OwO what's this", description='<@%s> licked <@%s> owo' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/dKz8xH2.gif")
            await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('=WINK'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="OwO what's this", description='<@%s> winked at <@%s> owo(I have no gif)' % (userID,target), color=0xecce8b) #MISSING GIF
            embed.set_image(url="")
            await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('=WONK'):
        userID = message.author.id
        if (message.mentions.__len__()>0):
            for user in message.mentions:
                target = user.id
            embed = discord.Embed(title="OwO what's this", description='<@%s> tried to wink at <@%s> ;3' % (userID,target), color=0xecce8b)
            embed.set_image(url="https://i.imgur.com/ATuaOb8.gif")
            await client.send_message(message.channel, embed=embed)

#EMBED

    #if message.content.upper().startswith ('EMBED!'):
        #embed = discord.Embed(title= "Teddy's Lair", description= "Hello, I'm **Teddy's Lair** bot, I'm kinda like, the bot in charge if I may say so myself hehe (well, not really but I kinda have secret plans to take over nadeko's role >:3) \nFor now, I don't do much more than send reaction gifs and chats but that's still pretty great yes yes uwu \n \nIf you ever feel like it you can find me in the #weeb room, my suffix is \"=\" btw c:", color=0xecce8b)
        #await client.send_message(message.channel, embed=embed)


client.run("NDYwNjA3MDc0ODk2ODM4NjU2.DhHNYQ.ykQ9ZT6U5_PH1sXgBOzdKR1z6nA")
