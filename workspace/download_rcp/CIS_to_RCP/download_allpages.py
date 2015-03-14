import os
import re
import requests # web crawler
from bs4 import BeautifulSoup # html parser
from urllib.parse import urljoin # url relative to absolute


def CISid_to_RCPid(text):
    m = text.rsplit('\t')[-2]
    if m != "":
        return m
    else:
        return ""

def download_page(RCPid):
    with open('./rcp/%s.html' %RCPid, 'wb') as file:
        # Get text
        response = requests.get('http://agence-prd.ansm.sante.fr/php/ecodex/rcp/R%s.htm' %RCPid)
        text_binary = response.text.encode('windows-1252',errors="ignore")
        file.write(text_binary)
        # Get images
        soup = BeautifulSoup(response.text)
        images_url = [x['src'] for x in soup.find_all('img')]
        images_url = [urljoin(response.url, url) for url in images_url]
        if len(images_url) != 0:
            os.makedirs('./images/R%s' %RCPid)
        for image_url in images_url:
            with open('./images/R%s/%s' % (RCPid, image_url.split('/')[-1]), 'wb') as f:
                response_img = requests.get(image_url)
                f.write(response_img.content)

with open('My_file.txt', 'r', encoding='windows-1252') as f:
    max_line = 0
    for line in f.readlines():
        CISid = re.match(r'\d+', line)
        RCPid = CISid_to_RCPid(line)
        print(RCPid)
        if RCPid != "":
            if not os.path.exists('./rcp/%s.html' %RCPid):
                download_page(RCPid)
            else:
                print('Already downloaded')
        else:
            print(RCPid+" has no RCP doc.")

        max_line += 1
#         if max_line  == 50:
#             break 