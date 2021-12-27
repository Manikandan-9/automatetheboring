import requests, os, bs4

search= input('Enter term to be searched: ')
no_images = int(input('how many images do you need: '))

os.makedirs('~/Desktop/imgurimages', exist_ok=True)
res = requests.get('http://imgur.com/search?q='+str(search))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
photos = soup.select('img')

for i in range(no_images):
    try:
        photo_url = 'http:' + photos[i].get('src')
        print('Downloading image %s...' % (photo_url))
        res = requests.get(photo_url)
        res.raise_for_status()
    except:
        continue
    filename = os.path.join('~/Desktop/imgurimages',os.path.basename(photo_url))
    file = open(filename,'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)
    file.close() 
    