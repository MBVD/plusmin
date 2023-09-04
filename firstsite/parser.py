import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


for page_num in range(1, 2): #5042
    url = f'http://matol.kz/comments/{page_num}/show'
    headers = {'accept': '*/*',
               'user-agent': UserAgent().random,
               }
    response = requests.get(url, headers=headers)
    print(response)
    try:
        soup = bs(response.text, 'html.parser')
        print(soup)
    except Exception:
        print("Connection Error")
    # with open('parsed.txt', 'w') as f_obj:
        # f_obj.write() Запись в txt файл