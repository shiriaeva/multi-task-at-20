from urllib.request import Request, urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'


start = datetime.now()

for i in range(100):
    s = urlopen(url)
    print(unquote(s.url))


res = open('../res.txt', 'w', encoding='utf8')

for i in tqdm(range(100)):
    html = urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')

    for l in links:
        href = l.get('href')
        if href and href.startswith('http') and 'wiki' not in href:
            print(href, file=res)


links = open('../res.txt', encoding='utf8').read().split('\n')

for url in links:
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url, e)

end = datetime.now()
print(f"Время выполнения синхронной проверки ссылок: {end - start}")