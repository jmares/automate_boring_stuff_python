import requests, sys, webbrowser, bs4

print('Searching ...')

res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('.package-snippet')

num_open = min(5, len(links))

for i in range(num_open):
    url = 'https://pypi.org' + links[i].get('href')
    print('Opening ' + url)
    webbrowser.open(url)