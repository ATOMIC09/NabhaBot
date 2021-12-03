import discord
from discord.ext import commands
import os
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from time import sleep
import random
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
from dotenv import load_dotenv
from discord.utils import get
import gtts
from discord import FFmpegPCMAudio
import asyncio


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='*', description="พูดมากว่ะ", intents=intents)
bot.remove_command('help')
bot.ai_core = 0

# Commands
@bot.command()
async def info(ctx):
        h = discord.Embed(title = "ℹ️ ข้อมูลครู", color = 0x00FF00)
        h.add_field(name="**ชื่อ**", value="นภา เติมเต็ม")
        h.add_field(name="**ฉายา**", value="ลูกชิ้น")
        h.add_field(name="**วันเกิด**", value="7 สิงหาคม 2514")
        h.add_field(name="**ขอมีม**", value="`นภาขอมีม`")
        h.add_field(name="**ความช่วยเหลือ**", value="`นภาช่วยด้วย`")
        h.add_field(name="**พูด**", value="`นภาพูด`")
        h.add_field(name="**ร้องเพลง**", value="`นภาร้องเพลงหน่อย`")
        h.add_field(name="**ไล่**", value="`นภาออกไป`")
        h.add_field(name="**ปิด Ai**", value="`นภาเงียบ`, `นภาหุบ...`, `ลูกชิ้นหุบ...`")
        h.add_field(name="**เปิด Ai**", value="`นภามานี่`, `ลูกชิ้นมานี่`")
        h.set_thumbnail(url="https://cdn.discordapp.com/attachments/778868879567880192/878973315467866152/unknown.png")
        await ctx.send(embed = h)

# Commands
@bot.command()
async def help(ctx):
        h = discord.Embed(title = "ℹ️ ช่วยเหลือ", color = 0x00FF00)
        h.add_field(name="**🎵 เพลง**", value="`*help_music`")
        h.add_field(name="**📤 ส่งข้อความ**", value="`*send [TC_ID] [ข้อความ]`")
        h.add_field(name="**🧠 เปิด Ai**", value="`*ai_on`")
        h.add_field(name="**❌ ปิด Ai**", value="`*ai_on`")
        h.add_field(name="**😆 สุ่มมีม**", value="`*meme`")
        await ctx.send(embed = h)

@bot.command()
async def help_music(ctx):
        m = discord.Embed(title = "🎵 **เพลง**", color = 0x00FF00)
        m.add_field(name="เรียกนภา", value="`&summon`")
        m.add_field(name="เตะนภา", value="`&dis`")
        m.add_field(name="นภาร้องเพลง", value="`&p [URL]`")
        m.add_field(name="นภาพัก", value="`&pause`")
        m.add_field(name="นภาเล่นต่อ", value="`&resume`")
        m.add_field(name="นภาหุปปาก", value="`&stop`")
        await ctx.send(embed = m)

@bot.command()
async def send(ctx, id, *, text):
	channel = ctx.bot.get_channel(int(id))
	await channel.send(text)

@bot.command()
async def ai_on(ctx):
        await ctx.send("AI Core: ON ✅")
        sleep(1)
        bot.ai_core = 1
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
                await voice.move_to(channel)
        else:
                voice = await channel.connect()
        
        

@bot.command()
async def ai_off(ctx):
        await ctx.send("AI Core: OFF ❎")
        bot.ai_core = 0
        voice_client = ctx.guild.voice_client
        await voice_client.disconnect()


# Meme Random
@bot.command()
async def meme(ctx):
        number = random.randint(1,146)
        file = discord.File(f"A:/Documents/GitHub/NabhaBot/MemePack/clip({number}).mp4")
        await ctx.send(file=file)

# Meme Random
@bot.listen()
async def on_message(message):
        if "นภาขอมีม" in message.content.lower():
                number = random.randint(1,146)
                file = discord.File(f"A:/Documents/GitHub/NabhaBot/MemePack/clip({number}).mp4")
                await message.channel.send(file=file)

@bot.listen()
async def on_message(message):
        if "นภาช่วยด้วย" in message.content.lower():
                file = discord.File("nabha.jpg")
                await message.channel.send(file=file)

        if "นภาเรียกใคร" in message.content.lower():
                file = discord.File("you.jpeg")
                await message.channel.send(file=file)
        
# Send File
@bot.command()
async def sendatt(ctx, id, filename: str):
        channel = ctx.bot.get_channel(int(id))
        file = discord.File(f"A:/Documents/GitHub/NabhaBot/Attachments/{filename}")
        await channel.send(file=file)

# Listen
@bot.listen()
async def on_message(message):
        voice = get(bot.voice_clients, guild=message.channel.guild)
        channel = message.author.voice.channel

        if "นภาหุบ" in message.content.lower():
                if message.author.id == bot.user.id:
                        return
                await message.channel.send('ไม่พูดแล้วค่ะ')
                await bot.change_presence(activity=discord.Game(name="AI Core: OFF ❎"))
                bot.ai_core = 0

        if "นภาเงียบ" in message.content.lower():
                if message.author.id == bot.user.id:
                        return
                await message.channel.send('ไม่พูดแล้วค่ะ')
                await bot.change_presence(activity=discord.Game(name="AI Core: OFF ❎"))
                bot.ai_core = 0

        if "ลูกชิ้นหุบ" in message.content.lower():
                if message.author.id == bot.user.id:
                        return
                await message.channel.send('ไม่พูดแล้วค่ะ')
                await bot.change_presence(activity=discord.Game(name="AI Core: OFF ❎"))
                bot.ai_core = 0

        if "shutup napha" in message.content.lower():
                if message.author.id == bot.user.id:
                        return
                await message.channel.send('ไม่พูดแล้วค่ะ')
                await bot.change_presence(activity=discord.Game(name="AI Core: OFF ❎"))
                bot.ai_core = 0

        if "นภามานี่" in message.content.lower():
                if message.author.id == bot.user.id:
                        return
                await message.channel.send('มีอะไรคะนักเรียน')
                await bot.change_presence(activity=discord.Game(name="AI Core: ON ✅"))
                bot.ai_core = 1

        if "ลูกชิ้นมานี่" in message.content.lower():
                if message.author.id == bot.user.id:
                        return
                await message.channel.send('มีอะไรคะนักเรียน')
                await bot.change_presence(activity=discord.Game(name="AI Core: ON ✅"))
                bot.ai_core = 1

        if "นภาพูด" in message.content.lower():
                # เช็คว่าอยู่ใน Voice Channel ไหม
                if voice and voice.is_connected():
                        await voice.move_to(channel)
                else:
                        voice = await channel.connect()
                number = random.randint(1,26)
                voice.play(discord.FFmpegPCMAudio(executable="A:/Documents/GitHub/NabhaBot/ffmpeg.exe",source=f"A:/Documents/GitHub/NabhaBot/Audio/napha({number}).wav"))

        if "นภาออกไป" in message.content.lower():
                voice = await channel.disconnect()

        if "นภาร้องเพลงหน่อย" in message.content.lower():
                # เช็คว่าอยู่ใน Voice Channel ไหม
                if voice and voice.is_connected():
                        await voice.move_to(channel)
                else:
                        voice = await channel.connect()
                number = random.randint(1,6)
                voice.play(discord.FFmpegPCMAudio(executable="A:/Documents/GitHub/NabhaBot/ffmpeg.exe",source=f"A:/Documents/GitHub/NabhaBot/Music/napha_music({number}).mp3"))

# Ai Core
chatbot = ChatBot("ลูกชิ้น")
conversation = [
"สวัสดีค่ะ",
"ดีค่ะนักเรียน",
"เป็นยังไงบ้างคะ",
"ครูสบายดี",
"นักเรียนอายุเท่าไหร่",
"นักเรียนมีใบแปะก๊วยมั้ย",
"เทพนรินทร์ ลาพาสระน้อย",
"ครูอายุ 50 ปีแล้วค่ะ",
"หัวหน้าอยู่ไหน",
"ทำการบ้านครูกันรึยัง",
"ครูได้ให้งานรึเปล่า",
"เข้าใจไหมคะนักเรียน",
"ทำไมไม่มีใครตอบครูเลย",
"ดีมากค่ะ",
"นักเรียนยังอยู่ไหมคะ",
"ไหนใครโดดเรียน",
"ครูเข้าใจนักเรียนคะ",
"ไม่ต้องเถียงครูค่ะ",
"สวัสดี ครูชื่อลูกชิ้น",
"ยินดีที่ได้รู้จัก",
"นักเรียนเป็นไงบ้าง?",
"สบายดีแล้วนักเรียนแล้วนักเรียนล่ะ?",
"ครูไม่เป็นไร แล้วนักเรียน",
"นักเรียนมาจากที่ไหน?",
"ครูมาจากประเทศไทย",
"นักเรียนอายุเท่าไร?",
"วันเกิดนักเรียนเมื่อไหร่",
"17 ส.ค. 2514",
"นักเรียนมีโทรศัพท์มือถือหรือไม่",
"ใช่",
"ไม่",
"นักเรียนอยู่ที่นี่มานานเท่าไหร่แล้ว",
"นักเรียนเป็นคนสัญชาติอะไร",
"ทุกคนสามารถเป็นเพื่อนของครูได้",
"ก็เลยได้เจอกันอีกใช่ไหม",
"นักเรียนทำอะไรอยู่",
"การฝึกอบรม",
"ใครคือนักร้องที่นักเรียนชื่นชอบ?",
"ใครคือ Pai",
"นักเรียนชอบเพลงประเภทไหน?",
"ครูชอบเพลงป๊อป",
"กีฬาที่ครูชอบคือแชร์บอล",
"นักเรียนชอบสัตว์อะไร",
"ครูชอบแมว",
"นักเรียนชอบผลไม้ชนิดไหน",
"นักเรียนชอบกล้วยไหม",
"ครูชอบดูทีวี",
"ครูชอบดูหนัง",
"ครูสนุกกับการเดินทาง",
"ครูสนใจการถ่ายภาพ",
"นักเรียนพูดได้กี่ภาษา?",
"นักเรียนร้องเพลงได้ไหม?",
"นักเรียนอยากกินอะไร?",
"นักเรียนกำลังมองหาอะไร?",
"ครูกำลังมองหารองเท้า",
"ครูแค่มอง",
"ถูกต้อง",
"ไม่ถูกต้อง",
"ครูจะเอาอันนี้",
"ครูชอบมันมาก",
"ให้ไปส่งไหม",
"ครูสบายดี",
"ขอบใจจ้ะนักเรียน",
"ขอบคุณจ้ะ",
"นั่นไม่ยุติธรรม",
"ยินดี"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

@bot.listen()
async def on_message(message):
        if bot.ai_core == 1 and message.author.id != bot.user.id:
                voice = get(bot.voice_clients, guild=message.channel.guild)
                if message.author.id == bot.user.id:
                        return
                else:
                        text = message.content.lower()
                        response = chatbot.get_response(text)

                        tts = gtts.gTTS(text=str(response),lang='th')
                        tts.save('speak.mp3')
                        voice.play(discord.FFmpegPCMAudio(executable="A:/Documents/GitHub/NabhaBot/ffmpeg.exe",source='speak.mp3'))

                        os.remove("speak.mp3")

        elif "นภาหุบ" in message.content.lower():
                await message.channel.send('ไม่พูดแล้วค่ะ')
                await bot.change_presence(activity=discord.Game(name="AI Core: OFF ❎"))
                bot.ai_core = 0

        elif "ลูกชิ้นหุบ" in message.content.lower():
                await message.channel.send('ไม่พูดแล้วค่ะ')
                await bot.change_presence(activity=discord.Game(name="AI Core: OFF ❎"))
                bot.ai_core = 0

        
        
		
# Events
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="AI Core: OFF ❎"))
	print('Nabha Online !')

Token = os.environ["NabhaToken"]
bot.run(Token)
