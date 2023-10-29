from discord.ext import commands
from decouple import config
import openai
import discord

# Initialize the OpenAI API client
openai.api_key = config('OPENAI_API_KEY')

# Create Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

# Instantiate the bot with the command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is logged in as {bot.user.name}')

@bot.command()
async def ask(ctx, *, question):
    # Use OpenAI API to get a response to the question
    response = openai.Completion.create(engine="text-davinci-003", prompt=question, max_tokens=150) # You can change whatever engine you want to use refer to for different engines https://platform.openai.com/docs/api-reference/introduction 
    await ctx.send(response.choices[0].text.strip())

# Run the bot
bot.run(config('DISCORD_BOT_TOKEN'))
