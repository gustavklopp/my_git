'''Give it table with soup, and provide Rest Colspan aware string table'''

from texttable import *
from bs4 import BeautifulSoup
import re
import textwrap

'''list of examples for textable module '''
# table = Texttable()
# table.set_cols_align(["l", "r", "c"])
# table.set_cols_valign(["t", "m", "b"])
# table.add_rows([ ["Name", "Age", "Nickname"], 
#                  ["Mr\nXavier\nHuon", 32, "Xav'"],
#                  ["Mr\nBaptiste\nClement", 1, "Baby"] ])
# # print(table.draw() + "\n")
# 
# table = Texttable()
# table.set_deco(Texttable.HEADER)
# table.set_cols_dtype(['t',  # text 
#                       'f',  # float (decimal)
#                       'e',  # float (exponent)
#                       'i',  # integer
#                       'a']) # automatic
# table.set_cols_align(["l", "r", "r", "r", "l"])
# table.add_rows([["text",    "float", "exp", "int", "auto"],
#                 ["abcd",    "67",    654,   89,    128.001],
#                 ["efghijk", 67.5434, .654,  89.6,  12800000000000000000000.00023],
#                 ["lmn",     5e-78,   5e-78, 89.4,  .000000000000128],
#                 ["opqrstu", .023,    5e+78, 92.,   12800000000000000000000]])
# # print(type(table.draw()))


'''extract table from soup and convert to a list'''
def htmltable2list(text):
    result = []
    span = []
    rowspan = []
    soup = BeautifulSoup(text)
    table = soup.find('table')
    allrows = table.findAll('tr')
    for idx_row, row in enumerate(allrows):
        result.append([])
        allcols = row.findAll('td')
        for idx_col, col in enumerate(allcols):
            cell_val = col.text.strip()
            cell_val = textwrap.fill(cell_val, 30) #TextTable doesn't work if cell too long...
            cell_val_s = cell_val.split('\n') 
            '''Pb with TextTable: Headers are centered, ReST doesn't like it... Need to manually ljustified
               the text inside the headers'''
            max_s = max(len(s) for s in cell_val_s)
            cell_val_complete = ""
            for str in cell_val_s:
                cell_val_complete += str.ljust(max_s, '_') + "\n"
            cell_val = cell_val_complete
#             print(cell_val, idx_row, idx_col)
            '''Create the list of rowspan'''
            if col.has_attr('rowspan'):
                # take only the portion before the '\n' for the colspan table
                cell_val_split = cell_val.split('\n')
                for inside_cell in cell_val_split:
                    if inside_cell == '': continue
                    rowspan.append([idx_row, idx_col, cell_val])                 
                    
            result[-1].append(cell_val)
            '''Put 'x' if there's colspan'''
            if col.has_attr('colspan'):
                # take only the portion before the '\n' for the colspan table
                cell_val_split = cell_val.split('\n')
                for inside_cell in cell_val_split:
                    if inside_cell == '': continue
                    span.append([inside_cell, int(col['colspan'])])
                # put 'X' where colspan says it
                for i in range(int(col['colspan'])-1):
                    result[-1].append('X') 
    '''put 'X' for rowspan'''
    for i in rowspan:
        row = i[0]
        col = result[row].index(i[2])
        result[row+1].insert(col, 'X')
             
#     print('Result :', result)
#     print(span)
#     print(rowspan)
    my_dic = {"result_list": result, "span_list": span}          
    return my_dic

'''convert list to ReST compatible string'''
def list2stringtable(table_list):
    table_tt = Texttable(max_width=0)  # no limit on the column width (default : 80)
    table_tt.add_rows(table_list)
   #     print(table_tt.draw())
    return table_tt.draw()

'''Replace function for regex SUB function: Number of colspan and then,
number of '|' and 'X' to delete'''
def replace(my_dic, my_dic_idx):
    repl = "\\1 \\2 "
    idx = 3
    for nb in range(my_dic["span_list"][my_dic_idx][1]-2):
        repl += "\\" + str(idx) + " " + "\\"  + str(idx+1) + " "
        idx += 2
#     print('repl =', repl)
    return repl
# print(replace()) 

def stringtable_colspan(my_dic, my_dic_idx, ReST_table):
    patt = "(.*" + my_dic["span_list"][my_dic_idx][0]+ "\s*?)\|(\s+)[X ]"
    for nb_span in range(my_dic["span_list"][my_dic_idx][1]-2):
        patt += "(.*?)\|(\s+)[X ]"
#     print('patt = ', patt)
    tabl = [ReST_table]
    pattern = re.compile(patt, re.DOTALL)
#     print('ReST before :\n', [ReST_table])
    string_changed = pattern.sub(replace(my_dic, my_dic_idx), ReST_table, count=1)
#     print('Rest After :\n', [string_changed])
    return string_changed

''' synthesis of the above functions'''
def html2ReST_table(table):
    my_dic = htmltable2list(table)
    ReST_table = list2stringtable(my_dic["result_list"])
    # COlspan is not working in KIVY...
#     if len(my_dic["span_list"]) != 0:
#         for my_dic_idx, val in enumerate(my_dic['span_list']):
#             ReST_table = stringtable_colspan(my_dic, my_dic_idx, ReST_table)
#         ReST_table = ReST_table.replace('_', ' ')  # finish the manually ljustified: remove the '_' put before
    ReST_table_final = ReST_table.replace('_', ' ')  # finish the manually ljustified: remove the '_' put before
    return ReST_table_final
    

if __name__ == "__main__":
    table_test = '''
<table>
<tr>
<td>Name</td>
<td colspan="4">Features</td>
</tr>

<tr>
<td>Me Roseline\n Huon</td>
<td>32</td>
<td>Rose</td>
<td>Female</td>
<td>Programer</td>
</tr>

<tr>
<td>Mr Baptiste Clement</td>
<td>36</td>
<td>Baby</td>
<td>male</td>
<td>Graphist</td>
</tr>
</table>'''
#     print(html2ReST_table(table_test))
    table_test2 ='''
<table border="1" cellpadding="0" cellspacing="0" class="AmmCorpsTexteTable" style="border-collapse:collapse;border:none">
<tr>
<td style="width:250.1pt;border:solid windowtext 1.0pt;
padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">Dosage (en µg) du premier comprimé sublingual par accès douloureux paroxystique</p>
</td>
<td style="width:250.1pt;border:solid windowtext 1.0pt;
border-left:none;padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">Dosage (en µg) du second comprimé sublingual, à administrer au besoin 15 à 30 minutes après le premier comprimé</p>
</td>
</tr>
<tr>
<td style="width:250.1pt;border:solid windowtext 1.0pt;
border-top:none;padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">100</p>
</td>
<td style="width:250.1pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">100</p>
</td>
</tr>
<tr>
<td style="width:250.1pt;border:solid windowtext 1.0pt;
border-top:none;padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">200</p>
</td>
<td style="width:250.1pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">100</p>
</td>
</tr>
<tr>
<td style="width:250.1pt;border:solid windowtext 1.0pt;
border-top:none;padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">300</p>
</td>
<td style="width:250.1pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">100</p>
</td>
</tr>
<tr>
<td style="width:250.1pt;border:solid windowtext 1.0pt;
border-top:none;padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">400</p>
</td>
<td style="width:250.1pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">200</p>
</td>
</tr>
<tr>
<td style="width:250.1pt;border:solid windowtext 1.0pt;
border-top:none;padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">600</p>
</td>
<td style="width:250.1pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">200</p>
</td>
</tr>
<tr>
<td style="width:250.1pt;border:solid windowtext 1.0pt;
border-top:none;padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center">800</p>
</td>
<td style="width:250.1pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:0cm 5.4pt 0cm 5.4pt" valign="top" width="333">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><i>-</i></p>
</td>
</tr>
</table>'''

    table_test3 = '''
<table border="1" cellpadding="0" cellspacing="0" class="AmmCorpsTexteTable" style="margin-left:5.4pt;border-collapse:collapse;border:none">
<thead>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Classe de système d'organes</span></b></p>
</td>
<td colspan="4" style="width:360.0pt;border:solid windowtext 1.0pt;
border-left:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="480">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Effets indésirables, par fréquence</span></b></p>
</td>
</tr>
</thead>
</table>
'''
    table_test4 = """
<table border=1>
<tr>
<td rowspan="2">Name</td>
<td colspan="2">Features</td>
<td rowspan="2">Height</td>
</tr>

<tr>
<td>Eye color</td>
<td>Hair color</td>
</tr>

<tr>
<td>Me Roseline\n Huon</td>
<td>BLue</td>
<td>Rose</td>
<td>1m65</td>
</tr>

<tr>
<td>Mr Baptiste Clement</td>
<td>Brown</td>
<td>Blondy</td>
<td>1m85</td>
</tr>
</table>"""
    print(htmltable2list(table_test4))
#     print(html2ReST_table(table_test4))    
    
#     print(table.draw() + "\n")
#     table = Texttable(max_width=0)
    
#     table.add_rows([ ['Affections cardiaques\n', '\n', '\n', 'Tachycardie  Bradycardie\n', '\n'], 
#                  ['Affections cardiaques\n', '\n', '\n', 'Tachycardie  Bradycardie\n', '\n'],
#                  ['Affections cardiaques\n', '\n', '\n', 'Tachycardie  Bradycardie\n', '\n'] ])
#     table.add_rows([ ["Name", "Age", "Nickname", '\n', '\n'], 
#                  ["Mr\nXavier\nHuon", 32, "Xav'", '\n', '\n'],
#                  ["Mr\nBaptiste\nClement", 1, "Baby", ' \n', ' \n'] ])
#     print(table.draw() + "\n")
