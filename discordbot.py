import asyncio
import discord
import os
import datetime

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    asyncio.ensure_future(greeting_gm())

async def greeting_gm():
    channel = client.get_channel('718811732243382345')
    while True:
        print(datetime.datetime.now().minute)
        if(datetime.datetime.now().minute==47):
            await message.channel.send('  ( ☞三☞´3｀ )☞三☞それそれたそー')
            await asyncio.sleep(1)
        if(datetime.datetime.now().minute==48):
            print("eeee")
            await message.channel.send('おはよう' + str(datetime.datetime.now()))
            await asyncio.sleep(55)
        elif(datetime.datetime.now().minute==49):
            await message.channel.send('gtegegeegう' + str(datetime.datetime.now()))
            await asyncio.sleep(55)
        else:
            await asyncio.sleep(1)

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    channel = client.get_channel('718811732243382345')
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        #await client.send_message(channel,'にゃーん')
        await message.channel.send("メッセージ")

client.run(token)
