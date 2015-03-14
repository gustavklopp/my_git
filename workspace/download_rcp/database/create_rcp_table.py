from sqlalchemy import *

db = create_engine('sqlite:///../../kivy_rcpBase/MyApp/rcp_database.db')
db.echo = True

metadata = MetaData(db)

rcp_table = Table('rcp_table', metadata,
               Column('rcp_id', Integer),
               Column('spec_name', String),
               Column('Date de Modification', Date, nullable=True),
               Column('Composition', String),
               Column('Nom en DCI', String),
               Column('Forme', String),
               Column('Indication', String),
               Column('Posologie', String),
               Column('Contre-indications', String),
               Column('Interactions', String),
               Column('Grossesse et Allaitement', String),
               Column('Précautions conduite auto', String),
               Column('Effets indésirables', String),
               Column('Surdosage', String),
               Column('Pharmacodynamie', String),
               Column('Pharmacocinétique', String),
               Column('Etudes Pré-cliniques', String),
               Column('Excipients', String),
               Column('Conservation', String),
               Column('Pré-consevation', String),
               Column('Emballage', String),
               Column('Elimination', String),
               Column('Titulaire de l\'AMM', String),
               Column('Présentation', String), 
               Column('Date de Première autorisation', Date, nullable=True),
               Column('Date de Révision', Date, nullable=True),
               Column('Dosimétrie', String),
               Column('Radiopharmaceutique', String),
               Column('Conditions de Prescription', String)
               )

rcp_table.create(checkfirst=True)

