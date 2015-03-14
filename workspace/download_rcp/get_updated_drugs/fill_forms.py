import requests


url = 'http://agence-prd.ansm.sante.fr/php/ecodex/index.php#result'
payload = {
           # blank values
           'txtCaracteres': "",
           'txtDateDebut': "",
           'txtDateFin': "",
           'lstEtat': "0",
           'lstComm': "0",
           # search values
           'lstRecherche': "denomination", #i.e "specialité"
           'txtDebutMAJ': "09/12/2014",
           'txtFinMAJ': "10/12/2014",
           'lstDoc': "200000",
           # hidden values :
           'page': "2",
           'cherche': "1",
           'subsid': "       ",
           'nonsubs': "",
           'affliste': "0",
           'listeopen': "0",
           'button': "OK",
           'DateDuJour': "21/01/2015"}
try:
    response = requests.post(url, data=payload)
    print(response.text)
except Exception as e:
    print(e)
# with open('updated_drugs.html', 'wb') as file:
#     # Get text
#     response = requests.post(url, data=payload)
#     text_binary = response.text.encode('iso-8859-1',errors="ignore")
#     file.write(text_binary)