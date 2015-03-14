'''Detect table in html, and convert it to ReST Grid Table'''

from bs4 import BeautifulSoup

def replace_table(text):
    table_result = ""
    result = []
    soup = BeautifulSoup(text)
    table = soup.find('table')
    allrows = table.findAll('tr')
    for row in allrows:
        result.append([])
        allcols = row.findAll('td')
        for col in allcols:
            result[-1].append(col.text.strip())
            if col.has_attr('colspan'):
                for i in range(int(col['colspan'])-1):
                    result[-1].append('X') 
            
    print(result)
    max_col = [max(len(str(x)) for x in line) for line in zip(*result)]  
    '''zip(*..) allows to unzip : ex : zip(*test) with test = [[1,2,3], [a,b,c]]
                                       -> [1, a] and [2, b] and [3, c]''' 
    print(max_col)
    
    for row_idx, row_val in enumerate(result):
        table_result +='\n+'
        for col_idx, col_val in enumerate(row_val):
            if row_idx == 1:
                table_result += '='*(max_col[col_idx])+'+'  # make it the headers row
            else:
                table_result += '-'*(max_col[col_idx])+'+'
        table_result += '\n|'
        for col_idx, col_val in enumerate(row_val):
            table_result += col_val.ljust(max_col[col_idx], ' ') + '|'  # ljust allows to left justified
        if row_idx == len(result)-1:  # last row
            table_result += '\n+'
            for col_idx, col_val in enumerate(row_val):
                table_result += '-'*max_col[col_idx] + '+'
    print(table_result)
    return table_result

if __name__ == "__main__":
    replace_table('''
<table border="1" cellpadding="0" cellspacing="0" class="AmmCorpsTexteTable" style="margin-left:5.4pt;border-collapse:collapse;border:none">
<thead>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Classe de système dorganes</span></b></p>
</td>
<td colspan="4" style="width:360.0pt;border:solid windowtext 1.0pt;
border-left:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="480">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Effets indésirables, par fréquence</span></b></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt"> </span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Très fréquent</span></b></p>
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">≥ 1/10</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Fréquent</span></b></p>
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">≥ 1/100, &lt; 1/10</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Peu fréquent</span></b></p>
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">≥ 1/1 000, &lt; 1/100</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Fréquence indéterminée (ne peut être estimée à partir des données disponibles)</span></b></p>
</td>
</tr>
</thead>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections du système immunitaire</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><b><span style="font-size:10.0pt"> </span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><b><span style="font-size:10.0pt"> </span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hypersensibilité </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:23.15pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Troubles du métabolisme et de la nutrition</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Anorexie</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Diminution de lappétit</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:58.1pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections psychiatriques</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dépression</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Paranoïa </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Etat confusionnel</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Désorientation</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Modifications de létat mental</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Anxiété</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Euphorie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dysphorie</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Labilité émotionnelle</span><span style="font-size: 10.0pt"><br> </br></span><span style="font-size:10.0pt;font-family:Arial">Troubles de lattention</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hallucinations</span></p>
</td>
</tr>
<tr style="height:101.9pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections du système nerveux</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Vertiges</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Céphalées</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Somnolence</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial"> </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Amnésie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Parosmie </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dysgueusie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Tremblement</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Léthargie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hypoesthésie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Insomnie</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Troubles du sommeil</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Convulsions</span></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections oculaires</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Vision floue</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:23.5pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections cardiaques</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Tachycardie </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Bradycardie</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections vasculaires</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hypotension</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:23.5pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections respiratoires,  </span></b></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">thoraciques et médiastinales</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dyspnée</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Douleur oro-pharyngée</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Sensation de constriction de la gorge</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dépression respiratoire</span></p>
</td>
</tr>
<tr style="height:190.65pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections gastro-intestinales</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Nausées</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Stomatite</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Vomissements</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Constipation</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Sécheresse buccale</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Ulcération buccale</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Ulcération gingivale</span></p>
<p class="SPCNormal"><span style="font-size:10.0pt;font-family:Arial">Ulcération labiale</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Vidange gastrique retardée</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Douleur abdominale</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dyspepsie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Gêne gastrique</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Affection de la langue</span></p>
<p class="SPCNormal"><span style="font-size:10.0pt;font-family:Arial">Stomatite aphteuse</span></p>
<p class="SPCNormal"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p class="SPCNormal"><span style="font-size:10.0pt;font-family:Arial">dème de la langue</span></p>
<p class="SPCNormal"><span style="font-size:10.0pt;font-family:Arial">Diarrhée</span></p>
<p class="SPCNormal"><span class="MsoFootnoteReference"><span style="font-size: 10.0pt"> </span></span></p>
</td>
</tr>
<tr style="height:22.1pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections de la peau et du tissu sous-cutané</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hyperhidrose</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Lésion cutanée </span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Rash</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Prurit allergique</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Prurit</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Sueurs nocturnes</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Tendance accrue aux ecchymoses</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections musculo-squelettiques et systémiques</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Arthralgies</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Raideur musculo-squelettiques</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Raideur articulaire</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections des organes de reproduction et du sein</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dysfonction érectile</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:48.1pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Troubles généraux et anomalies au site dadministration</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Fatigue</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Syndrome de sevrage </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Asthénie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Malaise</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Bouffée vasomotrice et bouffée de chaleur</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">dème périphérique</span> </p>
</td>
</tr>
<tr style="height:48.1pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Lésions, intoxications et complications liées aux procédures</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Surdosage accidentel</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Chutes</span></p>
</td>
</tr>
</table>
<p class="AmmCorpsTexte"><b>Déclaration des effets indésirables suspectés</b></p>
<p class="AmmCorpsTexte">La déclaration des effets indésirables suspectés après autorisation du médicament est importante. Elle permet une surveillance continue du rapport bénéfice/risque du médicament. Les professionnels de santé déclarent tout effet indésirable suspecté via le système national de déclaration : Agence nationale de sécurité du médicament et des produits de santé (Ansm) et réseau des Centres Régionaux de Pharmacovigilance - Site internet: <a href="http://www.ansm.sante.fr/"><span style="color:windowtext; text-decoration:none">www.ansm.sante.fr</span></a>.</p>
<p class="AmmAnnexeTitre2"><a name="RcpSurdosage">4.9. Surdosage</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278931">Les symptômes attendus en cas de surdosage par fentanyl sont de même nature que son action pharmacologique. Leffet indésirable le plus grave est la dépression respiratoire qui peut entraîner un arrêt respiratoire.</a></p>
<p class="AmmCorpsTexte">Les mesures à prendre immédiatement en présence dun surdosage morphinique consistent à retirer immédiatement le comprimé sublingual dABSTRAL de la bouche du patient sil sy trouve encore, effectuer des stimulations physiques et verbales du patient, déterminer son niveau de conscience. La perméabilité des voies respiratoires doit être assurée et une ventilation assistée (assistance respiratoire) doit être instaurée si nécessaire. Une température corporelle adéquate doit être maintenue et un apport liquidien par voie parentérale doit être instauré.</p>
<p class="AmmCorpsTexte">Pour le traitement du surdosage (ingestion accidentelle) chez une personne qui na jamais reçu de traitement morphinique, administrer de la naloxone ou dautres antagonistes morphiniques en se référant aux indications cliniques et au résumé des caractéristiques du produit en question. En cas de dépression respiratoire prolongée, il peut être nécessaire de répéter ladministration de lantagoniste morphinique. </p>
<p class="AmmCorpsTexte">La naloxone et les autres antagonistes morphiniques doivent être utilisés avec prudence dans le traitement du surdosage chez les patients sous morphiniques en raison du risque de déclenchement dun syndrome de sevrage aigu.</p>
<p class="AmmCorpsTexte">Une hypotension sévère ou persistante doit évoquer une hypovolémie, à prendre en charge par un apport liquidien approprié par voie parentérale.</p>
<p class="AmmCorpsTexte">Le fentanyl et dautres morphiniques ont été associés à une rigidité musculaire inhibant la respiration. Dans ce cas, une intubation endotrachéale, linstauration dune ventilation assistée et ladministration dun antagoniste des morphiniques ainsi que, dun curarisant, peuvent être nécessaires.</p>
<p class="AmmAnnexeTitre1"><a name="RcpPropPharmacologie">5. PROPRIETES PHARMACOLOGIQUES</a></p>
<p class="AmmAnnexeTitre2"><a name="RcpPropPharmacodynamie">5.1. Propriétés pharmacodynamiques</a></p>
<p class="AmmCorpsTexteGrasCar"><a name="_Toc142278933">Classe pharmacothérapeutique : Analgésiques, opioïdes, dérivés de la phénylpipéridine, code ATC : N02AB03</a><span style="background:white; font-weight:normal"> </span></p>
<p class="AmmCorpsTexte">Le fentanyl est un puissant analgésique agissant sur le récepteur morphinique µ et présente un effet analgésique rapide et une courte durée daction. Le fentanyl présente un effet analgésique environ 100 fois plus puissant que celui de la morphine. </p>
<p class="AmmCorpsTexte">Les effets secondaires du fentanyl sur le système nerveux central (SNC) et les fonctions respiratoire et gastro-intestinale sont ceux des analgésiques morphiniques et sont considérés comme des effets de classe.</p>
<p class="AmmCorpsTexte">Les effets analgésiques du fentanyl sont liés aux concentrations plasmatiques en substance active. Chez les sujets nayant jamais reçu de traitement morphinique, les concentrations sanguines minimales de fentanyl produisant un effet analgésique efficace sont comprises entre 0,3 et 1,2 ng/ml. Les concentrations comprises entre 10 et 20 ng/ml produisent un effet anesthésique chirurgical et une profonde dépression respiratoire.</p>
<p class="AmmCorpsTexte">Chez des patients cancéreux dont les douleurs chroniques étaient contrôlées<span style="text-transform:uppercase"> </span>par des administrations régulières de doses stables de morphiniques, une amélioration statistiquement significative a été observée sur la différence dintensité de la douleur avec ABSTRAL comparativement au placebo, dès 10 minutes après ladministration (voir figure 1 ci-dessous). La nécessité de recourir à un traitement analgésique de secours a été significativement réduite. </p>
<p class="AmmCorpsTexte"><i>Figure 1. Différence moyenne dintensité de la douleur par rapport à la situation initiale (</i><i><u><span style="font-size:11.0pt">±</span></u> ET) pour Abstral comparé à un placebo (mesurée sur une échelle de Likert de 0 à 10)</i></p>
<p class="AmmCorpsTexte" style="margin-bottom:0cm;margin-bottom:.0001pt; page-break-after:avoid"><span style="position:absolute;z-index:1;margin-left: 0px;margin-top:0px;width:502px;height:324px"><img height="324" src="../images/R0250726/image003.gif" width="502"/></span><img border="0" height="451" src="../images/R0250726/image004.gif" width="699">Linnocuité et lefficacité dABSTRAL ont été évaluées chez des patients prenant le médicament dès lapparition de laccès douloureux paroxystique. Lutilisation préventive dABSTRAL dans les épisodes douloureux prévisibles na pas été étudiée dans les essais cliniques.</img></p>
<p class="AmmCorpsTexte">Comme tous les agonistes des récepteurs morphiniques µ, le fentanyl provoque une dépression respiratoire dose-dépendante. Le risque est plus élevé chez les sujets nayant jamais reçu de traitement morphinique que chez les patients souffrant de douleurs sévères et recevant un traitement morphinique de fond. Le traitement prolongé par morphiniques entraîne généralement le développement dune accoutumance à leurs effets secondaires. </p>
<p class="AmmCorpsTexte">Bien que les morphiniques augmentent en général la tonicité du muscle lisse urétral, leffet global est variable, entraînant dans certains cas des urgences mictionnelles et dans dautres cas une dysurie.</p>
<p class="AmmCorpsTexte">Les morphiniques augmentent la tonicité et réduisent les contractions péristaltiques du muscle lisse intestinal, prolongeant la durée du transit intestinal, pouvant ainsi être à lorigine de leffet constipant du fentanyl.</p>
<p class="AmmAnnexeTitre2"><a name="RcpPropPharmacocinetique">5.2. Propriétés pharmacocinétiques</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278934">Le fentanyl est un médicament très lipophile ; il est absorbé très rapidement par la muqueuse buccale et plus lentement par le tractus gastro-intestinal. Administré par voie orale, le fentanyl subit un métabolisme par effets de premier passage hépatique et intestinal prononcés. </a></p>
<p class="AmmCorpsTexte">ABSTRAL se présente sous la forme de comprimé sublingual à dissolution rapide. Le fentanyl est absorbé rapidement, au cours des 30 minutes suivant ladministration dABSTRAL. La biodisponibilité absolue dABSTRAL est de 54 %. Les concentrations plasmatiques maximales moyennes de fentanyl sont comprises entre 0,2 et 1,3 ng/ml (après administration de 100 à 800 µg dABSTRAL). Elles sont obtenues respectivement en 22,5 et<span style="text-transform:uppercase"> </span>240 minutes.</p>
<p class="AmmCorpsTexte">Environ 80 à 85 % du fentanyl se lie aux protéines plasmatiques, essentiellement à lα-1 glycoprotéine et dans une moindre mesure à lalbumine et aux lipoprotéines. Le volume de distribution du fentanyl à létat déquilibre est denviron 3 à 6 l/kg.</p>
<p class="AmmCorpsTexte">Le fentanyl est métabolisé en plusieurs métabolites pharmacologiquement inactifs, notamment en norfentanyl essentiellement sous leffet du CYP3A4. Après administration intraveineuse de fentanyl, environ 75 % de la dose administrée est excrétée dans les urines dans les 72 heures, essentiellement sous forme de métabolites. Seuls 10 % sont excrétés sous forme inchangée. Environ 9 % de la dose est excrétée dans les selles, essentiellement sous forme de métabolites. La clairance plasmatique totale du fentanyl est denviron 0,5 l/h/kg. Après administration dABSTRAL, la demi-vie délimination principale du fentanyl est denviron 7 heures (3 à 12,5 heures) et sa demi-vie délimination terminale denviron 20 heures (11,5 à 25 heures).</p>
<p class="AmmCorpsTexte">Les paramètres pharmacocinétiques dABSTRAL sont dose-proportionnels pour la gamme de dosages disponibles (100 à 800 µg). Les études pharmacocinétiques ont montré quune dose composée de plusieurs comprimés est bioéquivalente à un comprimé unique de la dose équivalente.</p>
<p class="AmmCorpsTexte"><b>Insuffisance hépatique ou rénale</b></p>
<p class="AmmCorpsTexte">Linsuffisance hépatique ou rénale risque dentraîner une augmentation des concentrations sériques. La clairance du fentanyl pourrait être réduite chez les patients âgés, cachectiques ou affaiblis, ce qui pourrait entraîner la prolongation de la demi-vie terminale du produit (<u>voir rubriques 4.2</u> et <u>4.4</u>).</p>
<p class="AmmAnnexeTitre2"><a name="RcpSecuritePreclinique">5.3. Données de sécurité préclinique</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278935">Les données de pharmacologie de sécurité et de toxicologie en administration répétée nont pas révélé dautre risque particulier chez lhomme que ceux indiqués dans les autres rubriques de ce RCP. Des études sur le rat ont montré une réduction de la fertilité et une augmentation de la mortalité embryonnaire. Aucun effet tératogène na toutefois été démontré.</a></p>
<p class="AmmCorpsTexte">Des tests de mutagénicité bactérienne et chez le rongeur ont abouti à des résultats négatifs. Comme d'autres morphiniques, le fentanyl a fait preuve deffets mutagènes <i>in vitro</i> sur des cellules de mammifères. Il semble improbable que lutilisation thérapeutique entraîne un risque mutagène puisque les effets ont été induits uniquement à des concentrations très élevées.</p>
<p class="AmmCorpsTexte">Les études de cancérogénicité cancérogenèse (test alternatif par voie cutanée chez la souris transgénique Tg.AC durant 26 semaines, étude de cancérogénèse par voie sous-cutanée chez le rat durant deux ans) avec le fentanyl nont pas révélé de résultats suggérant un potentiel oncogène. Lanalyse de coupes de cerveau provenant de létude de cancérogenèse réalisée chez le rat a montré des lésions cérébrales chez les animaux ayant reçu des doses élevées de citrate de fentanyl. La pertinence clinique de ces résultats nest pas connue. </p>
<p class="AmmAnnexeTitre1"><a name="RcpDonneesPharmaceutiques">6. DONNEES PHARMACEUTIQUES</a></p>
<p class="AmmAnnexeTitre2"><a name="RcpListeExcipients">6.1. Liste des excipients</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278937">Mannitol (E421)</a></p>
<p class="AmmCorpsTexte">Cellulose microcristalline silicifiée</p>
<p class="AmmCorpsTexte">Croscarmellose sodique</p>
<p class="AmmCorpsTexte">Stéarate de magnésium</p>
<p class="AmmAnnexeTitre2"><a name="RcpIncompatibilites">6.2. Incompatibilités</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278938">Sans objet. </a></p>
<p class="AmmAnnexeTitre2"><a name="RcpDureeConservation">6.3. Durée de conservation</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278939">3 ans</a></p>
<p class="AmmAnnexeTitre2"><a name="RcpPrecConservation">6.4. Précautions particulières de conservation</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278940">À conserver à une température ne dépassant pas 25 °C.</a></p>
<p class="AmmCorpsTexte">À conserver dans lemballage extérieur dorigine, à l'abri de lhumidité.</p>
<p class="AmmAnnexeTitre2"><a name="RcpEmballage">6.5. Nature et contenu de l'emballage extérieur</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278941">10 ou 30 comprimés sublinguaux sous plaquettes thermoformées avec sécurité enfant (alvéoles OPA/Aluminium/PVC munies dun film protecteur papier/polyester/Aluminium) sous étui extérieur en carton. Emballage comportant un code couleur pour chaque dosage de comprimés sublinguaux ABSTRAL. </a></p>
<p class="AmmCorpsTexte"><i>Toutes les présentations peuvent ne pas être commercialisées.</i></p>
<p class="AmmAnnexeTitre2"><a name="RcpPrecEmpl">6.6. Précautions particulières délimination et de manipulation</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278942">Les déchets doivent être éliminés en toute sécurité. Les patients et le personnel soignant doivent être incités à retourner tous les produits non utilisés à la pharmacie. Tout produit non utilisé ou déchet doit être éliminé conformément à la réglementation en vigueur.</a></p>
<p class="AmmAnnexeTitre1"><a name="RcpTitulaireAmm">7. TITULAIRE DE LAUTORISATION DE MISE SUR LE MARCHE</a></p>
<p class="AmmTitulaireNom"><a name="_Toc142278943"><span lang="EN-GB" style="text-transform:none">PROSTRAKAN LTD </span></a></p>
<p class="AmmTitulaireAdresse"><span lang="EN-US" style="text-transform:none">GALABANK BUSINESS PARK </span></p>
<p class="AmmTitulaireAdresse"><span lang="EN-US" style="text-transform:none">TD1 1QH GALASHIELS </span></p>
<p class="AmmTitulaireAdresse"><span style="text-transform:none">ROYAUME-UNI</span></p>
<p class="AmmAnnexeTitre1"><a name="RcpPresentation">8. NUMERO(S) DAUTORISATION DE MISE SUR LE MARCHE</a></p>
<p class="AmmListePuces1"><a name="_Toc142278944"><span style="font-family:Symbol">·<span style='font:7.0pt "Times New Roman"'> </span></span>391 042-9 ou 34009 391 042 9 4 : 10 comprimés sous plaquettes thermoformées avec sécurité enfant (alvéoles OPA/Aluminium/PVC munies dun film protecteur papier/polyester/Aluminium) </a></p>
<p class="AmmListePuces1"><span style="font-family:Symbol">·<span style='font:7.0pt "Times New Roman"'> </span></span>391 043-5 ou 34009 391 043 5 5 : 30 comprimés sous plaquettes thermoformées avec sécurité enfant (alvéoles OPA/Aluminium/PVC munies dun film protecteur papier/polyester/Aluminium) </p>
<p class="AmmAnnexeTitre1"><a name="RcpPremiereAutorisation">9. DATE DE PREMIERE AUTORISATION/DE RENOUVELLEMENT DE LAUTORISATION</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278945">[à compléter par le titulaire]</a></p>
<p class="AmmAnnexeTitre1"><a name="RcpDateRevision">10. DATE DE MISE A JOUR DU TEXTE</a></p>
<p class="AmmCorpsTexte"><a name="_Toc142278946">[à compléter par le titulaire]</a></p>
<p class="AmmAnnexeTitre1"><a name="RcpDosimetrie">11. DOSIMETRIE</a></p>
<p class="AmmCorpsTexte">Sans objet.</p>
<p class="AmmAnnexeTitre1"><a name="RcpInstPrepRadioph">12. INSTRUCTIONS POUR LA PREPARATION DES RADIOPHARMACEUTIQUES</a></p>
<p class="AmmCorpsTexte">Sans objet.</p>
<div style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm">
<p class="AmmAnnexeTitre"><a name="RcpCondPrescription">CONDITIONS DE PRESCRIPTION ET DE DELIVRANCE</a></p>
</div>
<p class="AmmCorpsTexte">Stupéfiant</p>
<p class="AmmCorpsTexte">Prescription limitée à 28 jours</p>
<p class="AmmCorpsTexte">Délivrance fractionnée de 7 jours maximum, sauf mention expresse du prescripteur « délivrance en une fois »</p>
<p class="AmmCorpsTexte">Prescription sur ordonnance répondant aux spécifications fixées par larrêté du 31 mars 1999.</p>
<b><span style="font-size:12.0pt;font-family:Arial;color:#0B3D92;text-transform:
uppercase"><br clear="all"/>
</span></b>
</body>
</html>

<table border="1" cellpadding="0" cellspacing="0" class="AmmCorpsTexteTable" style="margin-left:5.4pt;border-collapse:collapse;border:none">
<thead>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Classe de système dorganes</span></b></p>
</td>
<td colspan="4" style="width:360.0pt;border:solid windowtext 1.0pt;
border-left:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="480">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Effets indésirables, par fréquence</span></b></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt"> </span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Très fréquent</span></b></p>
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">≥ 1/10</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Fréquent</span></b></p>
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">≥ 1/100, &lt; 1/10</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Peu fréquent</span></b></p>
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">≥ 1/1 000, &lt; 1/100</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="center" class="AmmCorpsTexte" style="text-align:center"><b><span style="font-size:10.0pt;font-family:Arial">Fréquence indéterminée (ne peut être estimée à partir des données disponibles)</span></b></p>
</td>
</tr>
</thead>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections du système immunitaire</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><b><span style="font-size:10.0pt"> </span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><b><span style="font-size:10.0pt"> </span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hypersensibilité </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:23.15pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Troubles du métabolisme et de la nutrition</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Anorexie</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Diminution de lappétit</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.15pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:58.1pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections psychiatriques</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dépression</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Paranoïa </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Etat confusionnel</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Désorientation</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Modifications de létat mental</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Anxiété</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Euphorie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dysphorie</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Labilité émotionnelle</span><span style="font-size: 10.0pt"><br> </br></span><span style="font-size:10.0pt;font-family:Arial">Troubles de lattention</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:58.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hallucinations</span></p>
</td>
</tr>
<tr style="height:101.9pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections du système nerveux</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Vertiges</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Céphalées</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Somnolence</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial"> </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Amnésie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Parosmie </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dysgueusie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Tremblement</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Léthargie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hypoesthésie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Insomnie</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Troubles du sommeil</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:101.9pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Convulsions</span></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections oculaires</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Vision floue</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:23.5pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections cardiaques</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Tachycardie </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Bradycardie</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections vasculaires</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hypotension</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:23.5pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections respiratoires,  </span></b></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">thoraciques et médiastinales</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dyspnée</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Douleur oro-pharyngée</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Sensation de constriction de la gorge</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:23.5pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dépression respiratoire</span></p>
</td>
</tr>
<tr style="height:190.65pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections gastro-intestinales</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Nausées</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Stomatite</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Vomissements</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Constipation</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Sécheresse buccale</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Ulcération buccale</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Ulcération gingivale</span></p>
<p class="SPCNormal"><span style="font-size:10.0pt;font-family:Arial">Ulcération labiale</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Vidange gastrique retardée</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Douleur abdominale</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dyspepsie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Gêne gastrique</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Affection de la langue</span></p>
<p class="SPCNormal"><span style="font-size:10.0pt;font-family:Arial">Stomatite aphteuse</span></p>
<p class="SPCNormal"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:190.65pt" valign="top" width="120">
<p class="SPCNormal"><span style="font-size:10.0pt;font-family:Arial">dème de la langue</span></p>
<p class="SPCNormal"><span style="font-size:10.0pt;font-family:Arial">Diarrhée</span></p>
<p class="SPCNormal"><span class="MsoFootnoteReference"><span style="font-size: 10.0pt"> </span></span></p>
</td>
</tr>
<tr style="height:22.1pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections de la peau et du tissu sous-cutané</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Hyperhidrose</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Lésion cutanée </span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Rash</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Prurit allergique</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Prurit</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Sueurs nocturnes</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Tendance accrue aux ecchymoses</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:22.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections musculo-squelettiques et systémiques</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Arthralgies</span></p>
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Raideur musculo-squelettiques</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Raideur articulaire</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr>
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Affections des organes de reproduction et du sein</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Dysfonction érectile</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
</tr>
<tr style="height:48.1pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Troubles généraux et anomalies au site dadministration</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Fatigue</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Syndrome de sevrage </span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Asthénie</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Malaise</span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><span style="font-size: 10.0pt;font-family:Arial">Bouffée vasomotrice et bouffée de chaleur</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">dème périphérique</span> </p>
</td>
</tr>
<tr style="height:48.1pt">
<td style="width:90.0pt;border:solid windowtext 1.0pt;
border-top:none;padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p align="left" class="AmmCorpsTexte" style="text-align:left"><b><span style="font-size:10.0pt;font-family:Arial">Lésions, intoxications et complications liées aux procédures</span></b></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Surdosage accidentel</span></p>
<p class="AmmCorpsTexte"><span style="font-size:10.0pt"> </span></p>
</td>
<td style="width:90.0pt;border-top:none;border-left:
none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
padding:2.85pt 5.4pt 2.85pt 5.4pt;height:48.1pt" valign="top" width="120">
<p class="AmmCorpsTexte"><span style="font-size:10.0pt;font-family:Arial">Chutes</span></p>
</td>
</tr>
</table>''')