import discord
from discord.ext import commands
import random


class player:
    
    def __init__(self , member):
        self.member = member
        self.wins = 0
        self.spy = False
        self.suspicions = 0
    
    #adds to players wins for scoreboard
    def wins(self):
        self.wins += 1

    #reinitiates player spy status
    def replay(self):
        self.spy = False

    #sets the player as the spy
    def setSpy(self):
        self.spy = True    

class Game:
    def __init__(self):
        self.GameStarted = False
        self.players = []
        self.gameMessage = None
        self.startMessage = None
        self.channel = None



#creates the client
client = commands.Bot(command_prefix='/')

# a dictionary of games
games = {}


async def callStartMessage(game):
    channel = game.channel
    game.startMessage = await channel.send('Are you ready, Agent?!')
    await game.startMessage.add_reaction('➕')

#This event makes sure that the bot is online
@client.event
async def on_ready():
    print('Bot is online!')
    
    
# makes the bot ready
@client.command()
async def SpyOnServer(ctx):
    guild = ctx.message.guild
    game = Game()
    games[guild] = game
    game.channel = await guild.create_text_channel('Top Secret Channel')
    everyoneRole = guild.get_role(guild.id)
    await game.channel.set_permissions(everyoneRole , read_messages = True , send_messages = False)
    await callStartMessage(game)


#Starts the Game
@client.command()
async def GameStart(ctx):
    guild = ctx.message.guild
    game = games[guild]
    game.gameMessage = await game.channel.send('Beep! Beep! Beep!')

    # checks if the game has begun and send relative message
    if game.GameStarted == False:
        game.GameStarted = True
        await game.channel.send('To All Agents! \nATTENTION! \nThere is a Spy among us! Find the culprit and bring him in ASAP!')

    else:
        await game.channel.send('The search has already begun! Continue to find the Spy!')
    



        
    


client.run('NzU0ODc2MDY1MDU4NjUyMjMx.X17HHg.eVWNrxitZs3GTY2zy9y9TIBAmOc')#recieves the token generated by discord. This token will be regenerated.