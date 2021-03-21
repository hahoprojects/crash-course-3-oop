from bs4 import BeautifulSoup
import requests

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Sucsess! Response code {response.status_code}\n')
        soup = BeautifulSoup(response.text, features='html.parser')
        print(f'Hasil request dari {url}')
        print(f'Judul: {soup.title.string}')
    else:
        print(f'Error request {response.status_code}')
except Exception as e:
    print(f'Error occured: {e}')
print('Program end.')
