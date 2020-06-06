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
    
    while True:
        channel = client.get_channel('718811732243382345')
        
        print(datetime.datetime.now().minute)
        if(datetime.datetime.now().minute==14):
            print("eeee")
            await client.send_message(channel, 'おはよう' + str(datetime.datetime.now()))
            await asyncio.sleep(1)
        elif(datetime.datetime.now().minute==15):
            await client.send_message(channel, 'gtegegeegう' + str(datetime.datetime.now()))
            await asyncio.sleep(1)
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
        await client.send_message(channel,"メッセージ")

client.run(token)
