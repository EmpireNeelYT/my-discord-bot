import os
import discord
from discord.ext import commands
from PIL import Image

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Bot ready event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Example image command (Pillow)
@bot.command()
async def image(ctx):
    img = Image.new("RGB", (200, 200), color=(255, 0, 0))
    img.save("test.png")
    await ctx.send(file=discord.File("test.png"))

# Run bot safely using environment variable
bot.run(os.getenv("DISCORD_TOKEN"))
