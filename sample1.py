import requests
from bs4 import BeautifulSoup

def get_url(url):
    response = requests.get(url)
    return(response.text)

def get_links(html):
    output_list = []
    soup = BeautifulSoup(html,'html.parser')
    for link in soup.find_all("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])
            output_list.append(link.attrs.get('href'))
    return output_list

url = "https://www.wikihow.com/Stop-Clearing-Your-Throat"
output_html = get_url(url)
output_links = get_links(output_html)
print(output_links)
