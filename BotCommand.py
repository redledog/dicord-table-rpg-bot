from discord.ext import commands


client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print(client.user.id)
    print("Bot Ready!")


@client.command('접속')
async def connect(ctx, arg):
    await ctx.send(f'welcome {arg}')


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