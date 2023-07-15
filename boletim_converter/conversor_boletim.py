import os
import csv
import tkinter as tk
from tkinter import filedialog
import re
from datetime import datetime

# cria a janela e oculta ela
root = tk.Tk()
root.withdraw()

# solicita ao usuário que selecione a pasta desejada
folder_selected = filedialog.askdirectory()

# lista todos os arquivos da pasta selecionada e monta a lista de tuplas
file_list = []
for filename in os.listdir(folder_selected):
    # Procura uma data no nome do arquivo no formato dd.mm.aa
    date_match = re.search(r'\b(\d{2}\.\d{2}\.\d{2})\b', filename)
    if date_match:
        # Converte a data para o formato aaaa-mm-dd
        date_str = datetime.strptime(date_match.group(1), '%d.%m.%y').strftime('%Y-%m-%d')
        # Captura a hora da última modificação do arquivo
        mtime_str = datetime.fromtimestamp(os.path.getmtime(os.path.join(folder_selected, filename))).strftime('%H:%M:%S')
        # Monta a string com a data e hora
        datetime_str = f'{date_str} {mtime_str}'
        # Adiciona a tupla à lista
        file_list.append((filename, datetime_str))

# ordena a lista em ordem decrescente de data e hora
file_list.sort(key=lambda x: x[1], reverse=False)

# abre o arquivo CSV para escrita
if not os.path.exists('boletins.csv'):
    # first_id = input('Informe o ID do primeiro registro: ') COMENTAR A LINHA 37 E DESCOMENTAR 35, 36 E 50 PARA INSERIR ID MANUALMENTE
    # id = int(first_id)
    id = ""
else:
    with open('boletins.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        id = int(rows[-1][0]) + 1

# escreve os registros no arquivo CSV na ordem da lista
with open('boletins.csv', mode='a', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    for filename, datetime_str in file_list:
        writer.writerow([id, datetime_str, f'/uploads/{filename}'])
        # id += 1
