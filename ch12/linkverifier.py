import requests,bs4

link_input = input('Enter the link to be searched: ')
res=requests.get(link_input)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')
for link in links:
    try:
        url = link['href']
        url_check = requests.get(url)

        if url_check.status_code == 404:
            print(url, 'is broken :(')
    except:
        continue
    

