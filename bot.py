import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='f!')

@bot.command()
async def сказать(ctx, *, text):
    await ctx.send(text)
    await ctx.message.delete()

@bot.command()
async def очистить(ctx, amount=None):
    await ctx.channel.purge(limit=int(amount))
    await ctx.channel.send('<a:679326929895161882:861173648852385793> Сообщения успешно удалены.')

@bot.event
async def on_ready():
    activity = discord.Game(name="f!помощь | шард #5", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

@bot.command()
async def аватар(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command()
@commands.has_permissions(kick_members=True)
async def выгнать(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} успешно выгнан с сервера.")



@bot.command()
@commands.has_permissions(ban_members=True)
async def забанить(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} успешно забанен на этом сервере.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует!**', color=0x0c0c0c))

@bot.command()
async def помощь(ctx):
    embed = discord.Embed(
        title = 'Все команды бота </>:',
        description = '''**Привет, я бот Fanzy. Вот все мои команды:**
**Модерирование**
`забанить`, `выгнать`, `очистить`, `сказать`, `старт`, `стоп`.
**Утилиты**
`очистить`, `юзер`,`аватар`, `почта`.
**Системные команды**
`очистить`, `сказать`, `старт`, `стоп`.
**[Поддержать(Донат)](https://www.donationalerts.com/r/frame11)**''',
        colour = discord.Colour.from_rgb(106, 192, 245)
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def юзер(ctx,member:discord.Member = None, guild: discord.Guild = None):
    await ctx.message.delete()
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)

@bot.command()
async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0xff9900, title = 'Рандомный котик') 
    embed.set_image(url = json_data['link']) 
    embed.set_footer(text=f"Request by: {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed) 

@bot.command()  
async def почта(ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(content)
        await ctx.send('<a:679326929895161882:861173648852385793> успешно отправлено пользоваетелю!')


token = os.environ.get('BOT_TOKEN')

bot.run(str(token))discord.py

