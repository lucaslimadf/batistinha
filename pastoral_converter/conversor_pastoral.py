import PyPDF2

# Abrir o arquivo PDF em modo leitura binária
with open('boletim.02.04.23.pdf', 'rb') as pdf_file:
    # Criar um objeto PdfReader para ler o arquivo PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Percorrer todas as páginas do arquivo PDF
    for page in pdf_reader.pages:
        # Extrair o texto da página atual
        text = page.extract_text()

        # Imprimir o texto
        print(text)

