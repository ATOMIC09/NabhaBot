import discord
from discord.ext import commands
import os
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


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
	bot.ai_core = 1
	await ctx.send("AI Core: ON ✅")

@bot.command()
async def ai_off(ctx):
	bot.ai_core = 0
	await ctx.send("AI Core: OFF ❎")

# Listen
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
                "ครูอายุ 50 ปีแล้วค่ะ",
                "หัวหน้าอยู่ไหน",
                "ทำการบ้านครูกันรึยัง",
                "ครูได้ให้งานรึเปล่า",
                "เข้าใจไหมคะนักเรียน",
                "ทำไมไม่มีใครตอบครูเลย",
                "ดีมากค่ะ",
                "นักเรียนยังอยู๋ไหมคะ",
                "ไหนใครโดดเรียน",
                "ครูเข้าใจนักเรียนคะ",
                "ไม่ต้องเถียงครูค่ะ",
                "สวัสดี ครูชื่อลูกชิ้น",
                "ยินดีที่ได้รู้จัก",
                "นักเรียนเป็นอย่างไร?",
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
                "Pai",
                "นักเรียนชอบเพลงประเภทไหน?",
                "ครูชอบเพลงป๊อป",
                "ครูชอบดนตรีแจ๊ส",
                "ครูชอบเพลงฮิปฮอป",
                "ครูชอบเพลงร็อค",
                "ครูชอบดนตรีอิเล็กทรอนิกส์",
                "อาหารที่ชื่นชอบคืออะไร?",
                "อาหารโปรดของครูคือก๋วยเตี๋ยว",
                "หนังเรื่องโปรดของนักเรียนคืออะไร",
                "ภาพยนตร์เรื่องโปรดของครูคือ Avenger",
                "ภาพยนตร์เรื่องโปรดของครูคือ Interstellar",
                "ภาพยนตร์เรื่องโปรดของครูคืออวาตาร์",
                "กีฬาโปรดของนักเรียนคืออะไร?",
                "กีฬาที่ครูชอบคือฟุตบอล",
                "กีฬาที่ครูชอบคือเทนนิส",
                "กีฬาที่ครูชอบคือบาสเก็ตบอล",
                "กีฬาที่ครูชอบคือแบตมินตัน",
                "กีฬาที่ครูชอบคือแชร์บอล",
                "นักเรียนชอบสัตว์อะไร",
                "ครูชอบสุนัข",
                "ครูชอบแมว",
                "นักเรียนชอบผลไม้ชนิดไหน",
                "นักเรียนชอบกล้วยไหม",
                "ครูชอบดูทีวี",
                "ครูชอบทำสวนมาก",
                "ครูชอบดูหนัง",
                "ครูสนุกกับการเดินทาง",
                "ครูสนใจการถ่ายภาพ",
                "ครูอ่านมาก",
                "นักเรียนสามารถพูดได้กี่ภาษา?",
                "นักเรียนสามารถร้องเพลง?",
                "ครูจะจ่าย",
                "นักเรียนต้องการกินอะไร?",
                "นักเรียนกำลังมองหาอะไร?",
                "ครูกำลังมองหารองเท้า",
                "ครูแค่มอง",
                "ครูขอลองได้ไหม",
                "ถูกต้อง",
                "ครูจะเอาอันนี้",
                "ผมชอบมันมาก",
                "ครูจะเอามัน",
                "นี่เป็นชิ้นสุดท้าย!",
                "มันดูแพง",
                "นักเรียนมีราคาถูกกว่านี้หรือไม่",
                "ราคาเท่าไหร่?",
                "ขอส่วนลดหน่อยได้มั้ยคะ",
                "นี่เป็นราคาพิเศษสำหรับนักเรียน",
                "ให้ไปส่งไหม",
                "มีประกันไหม",
                "ครูสบายดี",
                "ดีใจที่ได้ยินแบบนั้น",
                "ขอบใจจ้ะนักเรียน",
                "ขอบคุณสำหรับทุกอย่าง",
                "นั่นไม่ยุติธรรม",
                "ยินดี"
	        ]

                trainer = ListTrainer(chatbot)
                trainer.train(conversation)

                textttt = message.content.lower()
                response = chatbot.get_response(textttt)
                output = str(response) + "\n"
                await message.channel.send(output)	
		
# Events
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="ไหนใครว่าครูเป็นลูกชิ้น"))
	print('Nabha Online !')

Token = os.environ["NabhaToken"]
bot.run(Token)
