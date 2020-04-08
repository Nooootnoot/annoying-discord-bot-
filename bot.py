import discord
import random
import time
from discord.ext import commands
import datetime 


now = datetime.datetime.now()
client = commands.Bot(command_prefix = '.') #prefix appelle commande du bot


# add events bot 

@client.event
async def on_ready():
    print("Trop bien je marche")

@client.event
async def on_member_join(member):                                      #useless af
    print (f'cette pute de {member} a rejoint le serveur')

@client.event                                                          #useless af
async def on_member_remove(member):
    print (f'Moquez vous ce péon de {member} a quitté le serv')

#add bot commands

@client.command(aliases = ["linkednigga"])
async def nigga(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/666241120505823245/686924478248124426/image0.jpg")


#@client.command(aliases = ["filednigga"])
#async def niggo(ctx):
#    my_files = [
#    discord.File(some_fp, 'nigga.jpg')                                 #envoie img stfu  nigga
#    ]
#    await channel.send('nigga.jpg', files=my_files)

@client.command()
async def latence(ctx):
    print(f'{now.hour}h{now.minute} : {ctx.message.author.name} a utilisé .latence')
    await ctx.send(f'J\'ai {round(client.latency * 1000)} ms')

@client.command()
async def spam(ctx, phrase, nb):
    i = 1
    print(f'{now.hour}h{now.minute} : {ctx.message.author.name} a utilisé .spam')
    while i <= int(nb):
        await ctx.send(f'{phrase}')
        i+=1

@client.command(aliases = ['jsuiscon'])
async def spam_infini(ctx, phrase):
    print(f'{now.hour}h{now.minute} : {ctx.message.author.name} a utilisé .jsuiscon')
    i = 1
    while True:
        await ctx.send(f'{phrase} (Affiché {i} fois)')
        i += 1

@client.command()
async def aled(ctx, phrase):
    print(f'{now.hour}h{now.minute} : {ctx.message.author.name} a utilisé .aled')
    while True:                                                                         #spam infini
        await ctx.send(f'{phrase}')

#@client.command()
#async def clear(ctx, amount = 5):                                                       #ne pas toucher / desac trop dangereux
#    await ctx.channel.purge(limit = amount + 1)

@client.command()
async def dm(ctx, victim: discord.User, message):
    print(f'{now.hour}h{now.minute} : {ctx.message.author.name} a utilisé .dm')
    while True:
        if victim.id == 258604211795787776:
            await ctx.author.send(f'{message}')                         #spam dm avec self defense
        else:
            await victim.send(f'{message}')
            
@client.command()
async def roulette(ctx):
    print(f'{now.hour}h{now.minute} : {ctx.message.author.name} a utilisé .roulette')
    i=1
    if random.randint(1,9) == 8:
        await ctx.send("Dommage t'as gagné")
    else:                                                                   #roulette russe 1/9 de win solo only
        await ctx.send("Voici 100 mp pour ta victoire")
        while i < 100:
            i += 1
            await ctx.author.send(f'T\'as perdu')

@client.command()
async def temp(ctx):
    print(f'{now.hour}h{now.minute} : {ctx.message.author.name} a utilisé .temp')
    x = ctx.guild.members       
    bullied = x[random.randint(0,len(x))]                       #roulette russe sur serveur entier
    if len(bullied.mention):
        await ctx.send(f'Tu fais chier ton pseudo est trop long {bullied}')
    else:
        await ctx.send(f'{bullied.mention}')

@client.command()
async def caca(ctx, message):
    print(f'{now.hour}h{now.minute} : {ctx.message.author.name} a utilisé .caca')
    while True:
        for victime in ctx.guild.members:
            if victime.id == 258604211795787776 or victime.bot == True:            #spam serveur entier avec self defense
                None      
            else:    
                await victime.send(f'{message}')

@client.command()
async def command(ctx):
    print(f'{now.hour}h{now.minute} : {ctx.message.author.name} a utilisé .command')
    await ctx.send("Commandes utile pour vous les kheys:  \n         .spam \"phrase\" nb_de_rep : spam nombre de fois demandé\n         .jsuiscon phrase : spam infini (avec compteur) \n         .aled phrase : spam infini (sans compteur)\n         .dm  @pseudo \"message\" : envoie d'un message en dm a la personne ciblé a l'infini \n         .roulette : roulette russe \n         .temp : notifie une personne au hasard sur le serveur \n         .caca \"messsage\" nb : Spam mp pour toutes personnes du serveur d'un message \n          avec un nombre de répétition défini")



client.run('caca') #ne pas leek le token sinon ca pu