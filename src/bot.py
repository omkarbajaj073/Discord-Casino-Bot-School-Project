import discord
from game import Game


games = {}

client = discord.Client()
TOKEN = "OTEwMTkxOTY4NDMxMjQ3NDQw.YZPQUw.8lobqubSVdeeVL9OCWeL5BhKjfE"

@client.event
async def on_connect():
    print("Bot connected.")
    

@client.event
async def on_message(message):
    content = message.content
    channel = message.channel
    name = message.author.name
    if message.author == client.user:
        return
    
    if content == "!bj":
        await channel.send("Starting blackjack with " + name)
        if channel in games:
            game = games[channel]
            if game.active:
                await channel.send("This channel already has an active game.")
            else:
                game.players.append(name)
                await game.start_game()
        else:
            game = Game(channel, [name])
            games[channel] = game
            await game.start_game()
            
    elif content == "!join":
        if channel in games and games[channel].active:
            games[channel].add_player(name)
        else:
            await channel.send("There is no active game in this channel.")
            
    elif content == "!hit":
        if name in games:
            game = games[name]
            if game.active:
                await game.hit()
            else:
                await channel.send("You don't have an active game " + name)
        else:
            await channel.send("You don't have an active game " + name)
            
    elif content == "!stay":
        if name in games:
            game = games[name]
            if game.active:
                await game.stay()
            else:
                await channel.send("You don't have an active game " + name)
        else:
            await channel.send("You don't have an active game " + name)

    elif content == "!surrender":
        if name in games:
            game = games[name]
            if game.active:
                await game.surrender()
            else:
                await channel.send("You don't have an active game " + name)
        else:
            await channel.send("You don't have an active game " + name)
            
            
client.run(TOKEN)