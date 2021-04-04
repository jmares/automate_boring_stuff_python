import requests, os, bs4, threading, time

start_time = time.time()

os.makedirs('xkcd', exist_ok=True)

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page
        print('Downloading page https://xkcd.com/%s...' % (url_number))
        res = requests.get('https://xkcd.com/%s' % (url_number))
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


# Create and start the Thread objects
download_threads = []     # a list of all the tread objects

for i in range(2000, 2140, 10):     # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0: 
        start = 1     # there is no comic 0, so set it to 1
    download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end
for download_thread in download_threads:
    download_thread.join()

end_time =  time.time()

print('Done')
print('It took %s seconds to download 140 XKCD comics (threaded)'  
    % (round(end_time - start_time, 2)))