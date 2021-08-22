import discord
from discord.ext import commands
import os


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

# Events
@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="ไหนใครว่าครูเป็นลูกชิ้น"))
	print('Nabha Online !')

Token = os.environ["NabhaToken"]
bot.run(Token)
