# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RcpTable',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('rcp_id', models.IntegerField(null=True, blank=True)),
                ('spec_name', models.TextField(blank=True)),
                ('date_de_modification', models.DateField(null=True, blank=True, db_column='Date de Modification')),
                ('composition', models.TextField(blank=True, db_column='Composition')),
                ('nom_en_dci', models.TextField(blank=True, db_column='Nom en DCI')),
                ('forme', models.TextField(blank=True, db_column='Forme')),
                ('indication', models.TextField(blank=True, db_column='Indication')),
                ('posologie', models.TextField(blank=True, db_column='Posologie')),
                ('contre_indications', models.TextField(blank=True, db_column='Contre-indications')),
                ('interactions', models.TextField(blank=True, db_column='Interactions')),
                ('grossesse_et_allaitement', models.TextField(blank=True, db_column='Grossesse et Allaitement')),
                ('précautions_conduite_auto', models.TextField(blank=True, db_column='Précautions conduite auto')),
                ('effets_indésirables', models.TextField(blank=True, db_column='Effets indésirables')),
                ('surdosage', models.TextField(blank=True, db_column='Surdosage')),
                ('pharmacodynamie', models.TextField(blank=True, db_column='Pharmacodynamie')),
                ('pharmacocinétique', models.TextField(blank=True, db_column='Pharmacocinétique')),
                ('etudes_pré_cliniques', models.TextField(blank=True, db_column='Etudes Pré-cliniques')),
                ('excipients', models.TextField(blank=True, db_column='Excipients')),
                ('conservation', models.TextField(blank=True, db_column='Conservation')),
                ('pré_consevation', models.TextField(blank=True, db_column='Pré-consevation')),
                ('emballage', models.TextField(blank=True, db_column='Emballage')),
                ('elimination', models.TextField(blank=True, db_column='Elimination')),
                ('titulaire_de_l_amm', models.TextField(blank=True, db_column="Titulaire de l'AMM")),
                ('présentation', models.TextField(blank=True, db_column='Présentation')),
                ('date_de_première_autorisation', models.DateField(null=True, blank=True, db_column='Date de Première autorisation')),
                ('date_de_révision', models.DateField(null=True, blank=True, db_column='Date de Révision')),
                ('dosimétrie', models.TextField(blank=True, db_column='Dosimétrie')),
                ('radiopharmaceutique', models.TextField(blank=True, db_column='Radiopharmaceutique')),
                ('conditions_de_prescription', models.TextField(blank=True, db_column='Conditions de Prescription')),
            ],
            options={
                'db_table': 'rcp_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
