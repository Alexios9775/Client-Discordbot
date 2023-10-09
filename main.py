import discord

from bot_logic1 import gen_pass
#from bot_logic2 import rd_emoji

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hello!")

    elif message.content.startswith('bye'):
        await message.channel.send("Bye!")

    elif message.content.startswith('Hello'):
        await message.channel.send("Hello!")

    elif message.content.startswith('How are you?'):
        await message.channel.send("Im good what about you? 😊")

    elif message.content.startswith('how are you'):
        await message.channel.send("Im good what about you? 😊")

    elif message.content.startswith('cya'):
        await message.channel.send("Cya!")
    
    elif message.content.startswith('Cya'):
        await message.channel.send("Cya!")

    elif message.content.startswith('Greetings'):
        await message.channel.send("Hello there!")

    elif message.content.startswith('greetings'):
        await message.channel.send("Hello there!")


    elif message.content.startswith('$GenPass'):
        await message.channel.send("Password: " + gen_pass(14))

    """elif message.content.startswith('$RdEmoji'):
        await message.channel.send(rd_emoji)"""

client.run("YOUR BOT TOKEN!")
