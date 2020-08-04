from discord.ext import commands


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(client.user.id)
    print("Bot Ready!")


@client.command()
async def 접속(ctx):
    await ctx.send('welcome')


try:
    f = open('token.txt', 'r')
    token = f.readline()
finally:
    f.close()

if not token:
    key = str(input('Input Token >> '))
else:
    key = token

client.run(key)