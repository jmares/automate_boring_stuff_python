import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
count = 0

while not url.endswith('#') and count < 10:
    # Download the page
    print('Downloading from page %s ...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Find the url of the comic image
    comic = soup.select('#comic img')
    if comic == []:
        print('Could not find comic image.')
    else:
        comic_url = 'https:' + comic[0].get('src')
        # Download the image
        print('Downloading image %s ...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()
        # Save the image to ./xkcd
        image = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in res.iter_content(100000):
            image.write(chunk)
        image.close()
    # Get the prev button's url
    prevlink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevlink.get('href')
    count += 1
    

print('Done')