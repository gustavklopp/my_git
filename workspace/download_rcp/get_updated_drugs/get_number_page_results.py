from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open('ansm_form_results.html'))
rst = soup.find('td', {'class': "pagination"})
rst = rst.text
m = re.search(r'/\s+(\d+)', rst)
print(m.group(1))