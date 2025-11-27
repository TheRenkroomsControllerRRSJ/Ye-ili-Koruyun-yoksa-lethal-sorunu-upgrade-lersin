import discord
from discord.ext import commands
from get_class import get_class
import os, random
import requests
from botmantik import emoji_olusturucu, yazi_tura, sifre_olusturucu
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Selam! Ben bir botum!')

@bot.command()
async def smile(ctx):
    await ctx.send(emoji_olusturucu())

@bot.command()
async def coin(ctx):
    await ctx.send(yazi_tura())

@bot.command(name='pass')
async def generate_pass(ctx):
    await ctx.send(sifre_olusturucu(10))

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def fikra(ctx):
    dosyalar = os.listdir('fikralar')
    fikra_dosyasi = random.choice(dosyalar)
    dosya_yolu = os.path.join('fikralar', fikra_dosyasi)
    with open(dosya_yolu, 'rb') as f:
        dosya = discord.File(f)
    await ctx.send(file=dosya)

@bot.command()
async def mem(ctx):
    with open('images/mem1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def sound(ctx):
    with open('sounds/audio.mp3', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    dosyalar = os.listdir('images')
    mem_dosyasi = random.choice(dosyalar)
    dosya_yolu = os.path.join('images', mem_dosyasi)
    with open(dosya_yolu, 'rb') as f:
        resim = discord.File(f)
    await ctx.send(file=resim)

@bot.command()
async def sound2(ctx):
    dosyalar = os.listdir('sounds')
    mem_dosyasi = random.choice(dosyalar)
    dosya_yolu = os.path.join('sounds', mem_dosyasi)
    with open(dosya_yolu, 'rb') as f:
        ses = discord.File(f)
    await ctx.send(file=ses)

@bot.command()
async def cevretemizmikirlimi(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            try:
                file_name = attachment.filename
                await attachment.save(f"./{file_name}")

                response = get_class(
                    model_path="model_unquant.tflite",  #Burada kendi yolunuzu seçip değiştrmelisiniz.
                    labels_path="labels.txt",
                    image_path=f"./{attachment.filename}"
                )

                await ctx.send(response)

            except Exception as e:
                await ctx.send(f"🚫 Görsel işlenemedi: {str(e)}")
    else:
        await ctx.send("📎 Görsel yüklemediğiniz için işlem yapılamadı. Lütfen bir resim ekleyin.")


bot.run("Tokeni buraya yazın")

