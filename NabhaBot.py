import discord
from discord.ext import commands
import os
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from time import sleep
import random


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
	h.set_thumbnail(url="https://cdn.discordapp.com/attachments/778868879567880192/878973315467866152/unknown.png")
	await ctx.send(embed = h)

@bot.command()
async def send(ctx, id, *, text):
	channel = ctx.bot.get_channel(int(id))
	await channel.send(text)

@bot.command()
async def ai_on(ctx):
        await ctx.send("AI Core: ON ✅")
        sleep(1)
        bot.ai_core = 1
        

@bot.command()
async def ai_off(ctx):
        await ctx.send("AI Core: OFF ❎")
        bot.ai_core = 0

# Meme Random
@bot.command()
async def meme(ctx):
        number = random.randint(1,111)
        file = discord.File(f"A:/Documents/GitHub/NabhaBot/MemePack/clip({number}).mp4")
        await ctx.send(file=file)
        
# Listen
@bot.listen()
async def on_message(message):
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

        if "นภา" in message.content.lower():
                if message.author.id == bot.user.id:
                        return
                await message.channel.send('มีอะไรคะนักเรียน')
                await bot.change_presence(activity=discord.Game(name="AI Core: ON ✅"))
                bot.ai_core = 1

        if "ลูกชิ้น" in message.content.lower():
                if message.author.id == bot.user.id:
                        return
                await message.channel.send('มีอะไรคะนักเรียน')
                await bot.change_presence(activity=discord.Game(name="AI Core: ON ✅"))
                bot.ai_core = 1

@bot.listen()
async def on_message(message):
        if bot.ai_core == 1 and message.author.id != bot.user.id:
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

                textttt = message.content.lower()
                response = chatbot.get_response(textttt)
                output = str(response) + "\n"
                #sleep(3)
                await message.channel.send(output)
                if message.author.id == bot.user.id:
                        return	

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
