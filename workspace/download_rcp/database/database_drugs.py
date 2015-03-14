from sqlalchemy import *


db = create_engine('sqlite:///drug_test.db')
db.echo = True

metadata = MetaData(db)

drugs = Table('drugs', metadata,
              Column('spec_name', String(50)),
              Column('dci_name', String(50)),
              Column('rcp_id', Integer))

drugs.create()

i = drugs.insert()
i.execute({'spec_name': 'CLAMOXYL', 'dci_name': 'AMOXICILLINE', 'rcp_id': '1000'},
          {'spec_name': 'AMOXICILLINE BIOGARAN', 'dci_name': 'AMOXICILLINE', 'rcp_id': '2000'},
          {'spec_name': 'AMOXICILLINE MYLAN', 'dci_name': 'AMOXICILLINE', 'rcp_id': '3000'},
          {'spec_name': 'AMOROLFINE BIOGARAN', 'dci_name': 'AMOROLFINE', 'rcp_id': '4000'},
          {'spec_name': 'AMOROLFINE MYLAN', 'dci_name': 'AMOROLFINE', 'rcp_id': '5000'},
          {'spec_name': 'LOCERYL', 'dci_name': 'AMOROLFINE', 'rcp_id': '6000'},
        )
