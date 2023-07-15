import requests
from bs4 import BeautifulSoup
import csv
import os.path
from datetime import datetime
import pytz
utc = pytz.utc

# solicita o ID a ser utilizado
if not os.path.exists('youtube_videos.csv'):
    print('Criando arquivo CSV...')
    # id = input("Informe o ID inicial: ") DESCOMENTAR ESSA LINHA E A 17 CASO QUEIRA INSERIR MANUALMENTE O ID. REMOVER A 18.
else:
    with open('youtube_videos.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        # id = str(int(rows[-1][0])+1)
        id = ""

# solicita a URL do vídeo
url = input("Informe a URL do vídeo do YouTube: ")
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('title').text.replace(' - YouTube', '')
description = 'Instagram: @pibdesobradinho Facebook: www.facebook.com/PrimeiraIgrejaBatistaDeSobradinho Site: www.pibsobradinho.org.br'
date_str = soup.find("meta", itemprop="startDate")["content"]
date = datetime.fromisoformat(date_str)
video_url = f'{soup.find("link", {"rel": "canonical"})["href"]}'
image = 'images/image_tall_1.jpg'

# Verifica se o autor está no título
with open('autores.txt', 'r', encoding='utf-8') as f:
    autores = f.read().splitlines()
for autor in autores:
    if autor in title:
        author = autor.replace('| ', '').replace('- ', '').strip()
        title = title.replace(f"{autor}", "").strip()
        if title[-1] in ['|', '-']:
            title = title[:-1].strip()
        break
else:
    author = "Pr. Washington Luiz"

# Cria o arquivo CSV caso ele ainda não exista
csv_file = 'youtube_videos.csv'
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

# Adiciona as informações no arquivo CSV. Ordem correta: ID DATA LINK IMAGEM TITULO DESCRIÇÃO AUTOR
with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow([id, date.strftime('%Y-%m-%d %H:%M:%S'), video_url, image, title, description, author])
    
print('Informações salvas com sucesso!')
