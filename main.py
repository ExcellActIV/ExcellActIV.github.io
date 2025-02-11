import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:5500/index.html'

response = requests.get(url)
if response.status_code == 200:
    # Parsing HTML menggunakan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Contoh 1: Mengambil heading utama (h1)
    h1 = soup.find('h1')
    with open("scraping.txt", "w") as scrap:
        print('Heading Utama:', h1.get_text() if h1 else 'Tidak ditemukan')
        scrap.write(f'Heading Utama: {h1.get_text()}\n')

        #
        for level in range(1, 7):
            for heading in soup.find_all(f'h{level}'):
                print(f'H{level}:', heading.get_text())
                scrap.write(f'H{level}: {heading.get_text()}\n')

        #
        about = soup.find(name='div', id='about')
        if about:
            paragraphs = about.find_all('p')
            for idx, p in enumerate(paragraphs, 1):
                print(f'Paragraf {idx} dalam Tentang:', p.get_text())
                scrap.write(f'Paragraf {idx} dalam Tentang: {p.get_text()}\n')

        hobi = soup.find(name='div', id='hobi')
        if hobi:
            paragraphs = hobi.find_all('p')
            for idx, p in enumerate(paragraphs, 1):
                print(f'Paragraf {idx} dalam Hobi:', p.get_text())
                scrap.write(f'Paragraf {idx} dalam Hobi: {p.get_text()}\n')

        footer = soup.find(name='div', id='Contact')
        if footer:
            paragraphs = footer.find_all('p')
            for idx, p in enumerate(paragraphs, 1):
                print(f'Paragraf {idx} dalam Hobi:', p.get_text())
                scrap.write(f'Paragraf {idx} dalam Hobi: {p.get_text()}\n')
else:
    print("Gagal mengambil halaman. Status Code:", response.status_code)

