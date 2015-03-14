from bs4 import BeautifulSoup
from sqlalchemy import *
import os
import datetime
import re

def find_text(name, soup):
    text = ""
    parent = soup.find('a', {'name': name}).parent
    while True:
        if parent == None:
            return text
 
        next_sibling = parent.find_next_sibling()
        try:
            class_sib = next_sibling['class'][0]
        #         print(class_sib)
        #         print(next_sibling)
            if class_sib == "AmmAnnexeTitre1" \
                 or class_sib == "AmmAnnexeTitre2":
                 return text
            text += "\n" + next_sibling.text
        except:
            pass
        parent = next_sibling
         
def get_rcp_sections(file):
    soup = BeautifulSoup(open(file, encoding='utf-8'))
    
    head, filename = os.path.split(file)
    filename = filename.split('.')[0]

    spec_name = soup.find('p', {'class': "AmmDenomination"}).text
    date_modif = soup.find('p', {'class': "DateNotif"}).text
    date_modif = re.search(r'(\d\d)/(\d\d)/(\d\d\d\d)', date_modif)
    if date_modif:
        date_modif = datetime.date(int(date_modif.group(3)), int(date_modif.group(2)), int(date_modif.group(1)))
    else:
        date_modif = None
    
    composition = find_text('RcpCompoQualitQuanti', soup).strip()
    comp_split = composition.split('\n')[0]
    dci_name = re.sub(r'([\w ]*?)(\.)+([\w ]*?)', '', comp_split)

    forme = find_text('RcpFormePharm', soup).strip()
    indication = find_text('RcpIndicTherap', soup).strip()
    posologie = find_text('RcpPosoAdmin', soup).strip()
    contre_indic = find_text('RcpContreIndic', soup).strip()
    mise_en_garde = find_text('RcpMisesEnGarde', soup).strip()
    interaction = find_text('RcpInteractions', soup).strip()
    grossesse_all = find_text('RcpGrossAllait', soup).strip()
    automobile = find_text('RcpConduite', soup).strip()
    effets_indesir = find_text('RcpEffetsIndesirables', soup).strip()
    surdosage = find_text('RcpSurdosage', soup).strip()
    pharmacodynamie = find_text('RcpPropPharmacodynamie', soup).strip()
    pharmacocinetique = find_text('RcpPropPharmacocinetique', soup).strip()
    pre_clinique = find_text('RcpSecuritePreclinique', soup).strip()
    excipients = find_text('RcpListeExcipients', soup).strip()
    conservation = find_text('RcpDureeConservation', soup).strip()
    pre_conservation = find_text('RcpPrecConservation', soup).strip()
    emballage = find_text('RcpEmballage', soup).strip()
    try:
        elimin = find_text('RcpPrecEmpl', soup).strip()
    except:
        elimin = find_text('RcpUtilManipElim', soup).strip()
    titulaire_amm = find_text('RcpTitulaireAmm', soup).strip()
    presentation = find_text('RcpPresentation', soup).strip()
    premiere_autoris = find_text('RcpPremiereAutorisation', soup).strip()
    premiere_autoris = re.search(r'(\d\d)/(\d\d)/(\d\d\d\d)', premiere_autoris)
    if premiere_autoris:
        premiere_autoris = datetime.date(int(premiere_autoris.group(3)), int(premiere_autoris.group(2)), int(premiere_autoris.group(1)))
    else:
        premiere_autoris = None
        
    date_revision = find_text('RcpDateRevision', soup).strip()
    date_revision = re.search(r'(\d\d)/(\d\d)/(\d\d\d\d)', date_revision)
    if date_revision:
        date_revision = datetime.date(int(date_revision.group(3)), int(date_revision.group(2)), int(date_revision.group(1)))
    else:
        date_revision = None
    try:
        dosimetrie = find_text('RcpDosimetrie', soup).strip()
    except:
        dosimetrie = None
    try:
        radiopharma = find_text('RcpInstPrepRadioph', soup).strip()
    except: 
        radiopharma = None
    prescription = find_text('RcpCondPrescription', soup).strip()
    
#     print(filename) 
    
    db = create_engine('sqlite:///../../kivy_rcpBase/MyApp/rcp_database.db')
    db.echo = True
    metadata = MetaData(db)
    rcp_table = Table('rcp_table', metadata, autoload=True)
    i = rcp_table.insert()
    i.execute({'rcp_id': filename, 
               'spec_name': spec_name,
               'Date de Modification': date_modif,
               'Composition': composition,
               'Nom en DCI': dci_name,
               'Forme': forme,
               'Indication': indication,
               'Posologie': posologie,
               'Contre-indications': contre_indic,
               'Interactions': interaction,
               'Grossesse et Allaitement': grossesse_all,
               'Précautions conduite auto': automobile,
               'Effets indésirables': effets_indesir,
               'Surdosage': surdosage,
               'Pharmacodynamie': pharmacodynamie,
               'Pharmacocinétique': pharmacocinetique,
               'Etudes Pré-cliniques': pre_clinique,
               'Excipients': excipients,
               'Conservation': conservation,
               'Pré-consevation': pre_conservation,
               'Emballage': emballage,
               'Elimination': elimin,
               'Titulaire de l\'AMM': titulaire_amm,
               'Présentation': presentation,
               'Date de Première autorisation': premiere_autoris,
               'Date de Révision': date_revision,
               'Dosimétrie': dosimetrie,
               'Radiopharmaceutique': radiopharma,
               'Conditions de Prescription': prescription})

if __name__ == "__main__":
    file = "../html_files/rcp_mod/00100000.html"
    get_rcp_sections(file)