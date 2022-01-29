import discord
import os 

token = os.environ.get('OTM0NDM2NzMwNzcyJmxNTg0.YewEBQ.Y-mKAQVp63S2wtJdJymPmthJtJw')
client = discord.Client()

@client.event
async def on_ready():
    print('BOT Telah siap {0.user}'.format(client))
    
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hallo') :
         await message.channel.send('hai')

client.run(token)


