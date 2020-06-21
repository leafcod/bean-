import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content. lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
     await message.channel.send("shut up no one wants hear your dumb ass.")

client.run('NzIzNDk1MDEyMTg4MjkxMTAy.Xu5YdQ.PJPv5Ce-vkrkn-LV4MYBdOMn1cs')

