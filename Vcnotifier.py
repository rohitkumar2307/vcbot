import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")  # Bot token from Railway
VC_ROLE_NAME = "VC-Notify"          # Role name in your server
ALERT_CHANNEL_ID = 123456789012345678  # Replace with text channel ID

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        guild = member.guild
        channel = bot.get_channel(ALERT_CHANNEL_ID)

        if channel:
            role = discord.utils.get(guild.roles, name=VC_ROLE_NAME)
            if role:
                await channel.send(f"🔔 {member.mention} just joined **{after.channel.name}**! {role.mention}")

bot.run(TOKEN)
