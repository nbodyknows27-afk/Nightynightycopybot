import discord
from discord.ext import commands
import asyncio
import random

repeating = {}

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix=',',
    self_bot=True,
    intents=intents,
    help_command=None
)
async def delete_cmd(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

@bot.event
async def on_ready():
    print(f'{bot.user} loaded Nighty-style system')

# ================= HELP =================
@bot.command(aliases=["cmds","commands"])
async def help(ctx):
    await delete_cmd(ctx)
    await ctx.send("""
🔥 COMMANDS 🔥

FUN:
gayrate, loverate, hack

SPAM:
rep, stop, spam

UTIL:
ping, say, math

MOD:
clear, kick, ban

INFO:
avatar, serverinfo
""")

# ================= REP =================
@bot.command(aliases=["repeat","loop"])
async def rep(ctx, *, msg):
    await delete_cmd(ctx)

    if ctx.channel.id in repeating:
        return await ctx.send("Already running")

    repeating[ctx.channel.id] = True

    while repeating.get(ctx.channel.id):
        await ctx.send(msg)
        await asyncio.sleep(ctx.channel.slowmode_delay or 2)

@bot.command(aliases=["end","halt"])
async def stop(ctx):
    await delete_cmd(ctx)
    repeating.pop(ctx.channel.id, None)

# ================= SPAM =================
@bot.command(aliases=["flood","blast"])
async def spam(ctx, amount: int, *, msg):
    await delete_cmd(ctx)

    for _ in range(amount):
        await ctx.send(msg)
        await asyncio.sleep(1)

# ================= FUN =================
@bot.command(aliases=["gay","rate"])
async def gayrate(ctx, user: discord.Member=None):
    await delete_cmd(ctx)
    user = user or ctx.author
    await ctx.send(f"{user} is {random.randint(0,100)}% gay 🌈")

@bot.command(aliases=["love","ship"])
async def loverate(ctx, u1: discord.Member, u2: discord.Member=None):
    await delete_cmd(ctx)
    u2 = u2 or ctx.author
    await ctx.send(f"❤️ {u1} + {u2} = {random.randint(0,100)}%")

@bot.command(aliases=["hackuser","ipgrab"])
async def hack(ctx, user: discord.Member):
    await delete_cmd(ctx)
    steps = ["Finding IP...", "Cracking password...", "Injecting malware...", "Done."]
    for s in steps:
        await ctx.send(s)
        await asyncio.sleep(1)

# ================= UTIL =================
@bot.command(aliases=["p"])
async def ping(ctx):
    await delete_cmd(ctx)
    await ctx.send(f"{round(bot.latency*1000)}ms")

@bot.command(aliases=["echo"])
async def say(ctx, *, msg):
    await delete_cmd(ctx)
    await ctx.send(msg)

@bot.command(aliases=["calc"])
async def math(ctx, *, expr):
    await delete_cmd(ctx)
    try:
        await ctx.send(eval(expr))
    except:
        await ctx.send("Error")

# ================= MOD =================
@bot.command(aliases=["purge","wipe"])
async def clear(ctx, amount: int=5):
    await delete_cmd(ctx)
    async for m in ctx.channel.history(limit=amount):
        try:
            await m.delete()
        except:
            pass

bot.run("YOUR_USER_TOKEN")
