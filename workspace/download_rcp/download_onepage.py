import requests # web crawler
from bs4 import BeautifulSoup # html parser
from urllib.parse import urljoin # url relative to absolute


with open('./rcp/output.html', 'wb') as file:
    # Get text
    response = requests.get('http://agence-prd.ansm.sante.fr/php/ecodex/rcp/R0250726.htm')
    text_binary = response.text.encode('iso-8859-1',errors="ignore")
    file.write(text_binary)
    # Get images
    soup = BeautifulSoup(response.text)
    images_url = [x['src'] for x in soup.find_all('img')]
    images_url = [urljoin(response.url, url) for url in images_url]
    for image_url in images_url:
        with open('./images/R0250726/%s' % image_url.split('/')[-1], 'wb') as f:
            response_img = requests.get(image_url)
            f.write(response_img.content)
