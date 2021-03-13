import discord
import requests
from datetime import datetime, timedelta, date
from bs4 import BeautifulSoup
import os

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user: #impede do bot se chamar
      return
    
    if message.content.startswith("-facom"):
      ontem = date.today() - timedelta(days=1)

      url = "https://www.facom.ufms.br/noticias/"
      r = requests.get(url)
      soup = BeautifulSoup(r.text, 'html.parser')

      div = soup.find(class_='media')
      noticia = div.find('h4')
      tag = noticia.find('a')
      titulo = tag.text
      link = tag.get('href')
      imagem = div.find('a').find('img').get('src')

      data = soup.find(class_="list-inline noticia-info").find('time').text.lower()

      dia, mes, ano = data.split(" de ")
      meses = {
        'janeiro': 1,
        'fevereiro': 2,
        'março': 3,
        'marco': 3,
        'abril': 4,
        'maio': 5,
        'junho': 6,
        'julho': 7,
        'agosto': 8,
        'setembro': 9,
        'outubro': 10,
        'novembro': 11,
        'dezembro': 12,
      }
      mes = meses[mes]
      data = str(ano)+'-'+str(mes)+'-'+str(dia)

      embed = discord.Embed(title=titulo).set_image(url=imagem)
      embed.add_field(name="noname",value=link)
      await message.channel.send(embed=embed)


client.run('')#discord tag here
