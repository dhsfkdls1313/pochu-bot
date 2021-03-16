import discord #디스코드 모듈 불러오기
import asyncio
token = "aDY3NTYyNzYwMTIxNzQ1NDA5.W0mJwA.Qn2mxehdhRmzW_Em0-VSTC7FQo8" #토큰 불러오기
client = discord.Client() #client 설정하기

@client.event
async def on_ready(): #봇이 준비되었을 때
    print("=======ready=======")

@client.event
async def on_message(message): 
    if message.content == "!핑":
        await message.channel.send("퐁")

    if message.content.startswith("!알람"):
        number = int(message.content.split(" ")[1])

        await message.channel.send(f"{message.author.mention}, {number} 초 알람 설정")
        await asyncio.sleep(number)
        await message.channel.send(f"{message.author.mention} 알람 시각")
    




client.run(token)