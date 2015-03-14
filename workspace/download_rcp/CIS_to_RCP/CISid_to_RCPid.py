import re

CISid = "62375644"

with open('My_file.txt', 'r', encoding='iso8859-1') as f:
#     m = re.search(r"%s\t[^\t]+\t[^\t]+\t[^\t]+\t[^\t]+\t[^\t]+\t[^\t]+\t([^\t]+)" %CISid, f.read())
#     print(m.group(1))
    max_lines = 0
    for line in f.readlines():
        print(line.rsplit('\t')[-2])
        max_lines += 1
        if max_lines == 10:
            break