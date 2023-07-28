import discord
from discord.ext import commands
import random
import pyfiglet
import asyncio
import time

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!ml ", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command()
async def michael(ctx):
    await ctx.send('I am running from michaels computer')

@bot.command(name='ascii', help="😁 Make ascii", usage='text')
async def ascii(ctx, *, text: str):
    if len(text) > 15:
        await ctx.send("Error: Text is too long (max 50 characters).")
    else:
        # Generate the ASCII art from the given text
        ascii_art = pyfiglet.figlet_format(text)

        # Send the ASCII art as a message
        await ctx.send(f"```{ascii_art}```")

@bot.command(name='8ball', help="🎱 Ask a yes or no question, and the magic 8-ball will answer", usage='question')
async def magic_8_ball(ctx, *, question: str = None):
    if not question:
        await ctx.send("Please provide a question.")
        return

    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    response = random.choice(responses)
    await ctx.send(f'Question: {question}\n:8ball: Answer: {response}')

snipes = {}

@bot.event
async def on_message_delete(message):
    global snipes  # Use the global dictionary
    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'message': message.content,
        'snipee_id': message.author.id 
    }
    print(f'{message.author} just deleted {message.content}')

@bot.command()
async def snipe(ctx):
    global snipes  # Use the global dictionary

    channel_id = str(ctx.channel.id)
    if channel_id in snipes:
        message_content = snipes[channel_id]['message']
        snipee = await bot.fetch_user(snipes[channel_id]['snipee_id'])
        sniped_by = ctx.author

        snipe_message = f"Message by {snipee}: `{message_content}`\nSniped by {sniped_by}"

        await ctx.send(snipe_message)
    else:
        await ctx.send("No message found to snipe in this channel.")

is_game_running = False  # Flag to check if the game is running or not
potato_holder = None  # Variable to keep track of the current potato holder

is_game_running = False  # Flag to check if the game is running or not
potato_holder = None  # Variable to keep track of the current potato holder
potato_hold_start = None  # Variable to keep track of when the potato was passed

@bot.command()
async def hotpotato(ctx):
    global is_game_running
    global potato_holder
    global potato_hold_start
    if is_game_running:
        await ctx.send("A game is already running!")
        return

    is_game_running = True
    members = [m for m in ctx.guild.members if not m.bot]  # Get all non-bot members
    potato_holder = random.choice(members)  # Choose a member at random
    potato_hold_start = time.time()  # Record the time when the potato was passed
    await ctx.send(f'@everyone a game of hot potato has started and {potato_holder.mention} is currently it. They have 30 seconds to pass it on before they get burned. Mention a user to pass it on. You have 30 seconds before the game ends!')

    # Countdown from 30
    for i in range(60, 0, -1):
        await asyncio.sleep(1)
        if time.time() - potato_hold_start >= 10:  # The potato holder has had the potato for more than 5 seconds
            await ctx.send(f'Game over! {potato_holder.mention} held the hot potato for too long and got burned!')
            is_game_running = False  # The game is over
            potato_holder = None  # Reset the potato holder
            return
        if i % 5 == 0:  # Every 5 seconds, send an update
            await ctx.send(f'{i} seconds left...')

    # End the game
    await ctx.send(f'Game over! {potato_holder.mention} was holding the hot potato and got burned!')
    is_game_running = False  # The game is over
    potato_holder = None  # Reset the potato holder

@bot.event
async def on_message(message):
    global is_game_running
    global potato_holder
    global potato_hold_start
    if is_game_running and message.author == potato_holder and message.mentions:
        # The potato holder mentioned someone, pass the potato
        new_potato_holder = message.mentions[0]  # The first mentioned user is the new potato holder
        if new_potato_holder.bot:
            # The mentioned user is a bot, don't pass the potato and send an error message
            await message.channel.send(f"Sorry, {message.author.mention}, you can't pass the potato to a bot!")
            return
        potato_holder = new_potato_holder  # Update the current potato holder
        potato_hold_start = time.time()  # Record the time when the potato was passed
        await message.channel.send(f'{potato_holder.mention}, you have the potato! You have 5 seconds to pass it on!!!')
    await bot.process_commands(message)  # Continue processing commands



bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')
