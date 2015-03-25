'''Synthesis of the different files :
From the html files inside a given folder
-convert it with the Rst compatible format
-put it inside database

using:
    1) correct_br : to correct non well formed html
    2) convert_to_text: to convert html table to RstTable 
        using the custom converter: html2ReST_table
    3) get_rcp_section: scrape each section of the html and put inside database
'''

import os
import sys
from os.path import expanduser
HOME = expanduser('~')
sys.path.insert(0, HOME + '/my_git/workspace/download_rcp/convert_to_text/')
from convert_to_text import convert_to_text
from correct_br import correct_br
from get_rcp_sections import get_rcp_sections
from shutil import copyfile


path = '../html_files'
max_nb_files = 0

for root, dirs, files in os.walk(os.path.join(path, 'rcp')):
    for file in files:
        if max_nb_files == 5:
            continue
        #copy file
        file = HOME + '/my_git/workspace/download_rcp/html_files/rcp/'+ file
        #print(file)
        head, filename = os.path.split(file)
        file_mod = os.path.join(head, '../rcp_mod/') + filename
        copyfile(file, file_mod)
        
        #modification of the file
        correct_br(file_mod)
        convert_to_text(file_mod)
        get_rcp_sections(file_mod)
        max_nb_files += 1
    
