import discord
from discord.ext import commands

description = 'хола'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='<prefix>', description=description, intents=intents)


bot.remove_command('help')


@bot.event
async def on_ready():
    print('---------------')
    print('  PPBOT IS ON ')
    print('---------------')


@bot.command()
async def repeat(ctx, times: int, content='хола'):
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def help(ctx):
    await ctx.send(
    '█▀▀█ █▀▀█ █▀▀▄ █▀▀█ ▀▀█▀▀\n'
    '█──█ █──█ █▀▀▄ █──█ ──█──\n'
    '█▀▀▀ █▀▀▀ ▀▀▀─ ▀▀▀▀ ──▀──\n'
    )
    await ctx.send(
    '!help - типа это\n'
    '!priv - типа прив\n'
    '!ban - халявный дискорд нитро\n'
    '!yaderka - дайте мне уже пульт от ядерки блин\n'
    '!everyone - ну эта типа спама многа упоминанийами\n'
    '!who - кто я\n'
    '!vopros - вопрос всей моей цифровой жизни\n'
    '!amogus - сам узнаешь\n'
    '!repeat <сколько раз повторить> <что_повторить_(без_пробелов)>\n'
    '!ppbot - выводит одно из самых прекрасных сообщений в мире'
    )



@bot.command()
async def priv(ctx):
    await ctx.send(f'хола, {author.mention}!')


@bot.command()
async def ppbot(ctx):
    await ctx.send(
    '██████╗░██████╗░██████╗░░█████╗░████████╗\n'
    '██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝\n'
    '██████╔╝██████╔╝██████╦╝██║░░██║░░░██║░░░\n'
    '██╔═══╝░██╔═══╝░██╔══██╗██║░░██║░░░██║░░░\n'
    '██║░░░░░██║░░░░░██████╦╝╚█████╔╝░░░██║░░░\n'
    '╚═╝░░░░░╚═╝░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░\n'
    )


@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = '**причины нит**'):
    await member.ban(reason = reason)
    await ctx.send(f"**{member}** был забанен по причине `{reason}`!")


@bot.command()
async def yaderka(ctx):
    await ctx.send('10')
    await ctx.send('9')
    await ctx.send('8')
    await ctx.send('7')
    await ctx.send('6')
    await ctx.send('5')
    await ctx.send('4')
    await ctx.send('3')
    await ctx.send('2')
    await ctx.send('2 с ниточкой')
    await ctx.send('1')
    await ctx.send('нуль')
    await ctx.send('ба-бах')

@bot.command()
async def everyone(ctx):
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')
    await ctx.send('@everyone')


@bot.command()
async def who(ctx):
    await ctx.send('я кто?')
    await ctx.send('я артур пиражкоф')
    await ctx.send('шутка')
    await ctx.send('я обычный бот для дискорда с прикольчиками')


@bot.command()
async def amogus(ctx):
    await ctx.send('amogus')
    await ctx.send('is')
    await ctx.send('sus')


@bot.command()
async def vopros(ctx):
    await ctx.send('где я')


bot.run('token')
