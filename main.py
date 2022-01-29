import discord
import random
from  discord.ui import Button,View
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(['We Are Work','We are One'])

token = 'OTM0NDM2NzMwNzcyMjkxNTg0.YewEBQ.Y-mKAQVp63S2wtJdJymPmthJtJw'
client = discord.Client()

bot = commands.Bot(command_prefix=">>>")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Do Not Disturb'))
    change_status.start()
    print('BOT Telah siap {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            button1 = Button(label="Click me!", style=discord.ButtonStyle.green,emoji="<:Sad:878479543764127744>")
            view = View()
            view.add_item(button)
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'yourname':
            await message.channel.send(f'MY Name is DS-DISCORDBOT#8284,  {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'see you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        if user_message.lower() == '!anywhere':
            await message.channel.send('This can be used anywhere!')
            return

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run('OTM0NDM2NzMwNzcyMjkxNTg0.YewEBQ.Y-mKAQVp63S2wtJdJymPmthJtJw')


