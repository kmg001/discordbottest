import discord, asyncio
client = discord.Client()

@client.event
async def on_message(message):
	if message.author.id == "683357183286575110":
		return

	print(message.content)
	
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
  
client.run('NjgzMzU3MTgzMjg2NTc1MTEw.XlqX_g.-jmjvM5WAHojLbsoscWVgZlmAVc') # or, if running a bot account: client.run('token')
