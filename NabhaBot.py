import discord
from discord.ext import commands
import os
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='*', description="พูดมากว่ะ", intents=intents)
bot.remove_command('help')

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

# Listen
@bot.listen()
async def on_message(message):
	chatbot = ChatBot("ลูกชิ้น")
	conversation = [
   		"สวัสดีค่ะ",
    	"ดีค่ะนักเรียน",
    	"เป็นยังไงบ้างคะ",
    	"ครูสบายดี",
		"ครูอายุ 50 ปีแล้วค่ะ",
		"หัวหน้าอยู่ไหน",
		"ทำการบ้านครูกันรึยัง",
		"ครูได้ให้งานรึเปล่า",
		"เข้าใจไหมคะนักเรียน",
    	"ทำไมไม่มีใครตอบครูเลย",
	]

	trainer = ListTrainer(chatbot)
	trainer.train(conversation)
	textttt = message.content.lower()

	response = chatbot.get_response(textttt)
	output = str(response) + "\n"

	if message.author.id == bot.user.id:
		return
	await message.channel.send(output)


# Events
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="ไหนใครว่าครูเป็นลูกชิ้น"))
	print('Nabha Online !')

Token = os.environ["NabhaToken"]
bot.run(Token)
