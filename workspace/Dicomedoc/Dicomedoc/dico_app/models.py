from django.db import models

# Create your models here.
# created via the 'manage.py inspectdb'
class RcpTable(models.Model):
    rcp_id = models.IntegerField(primary_key=True)
    spec_name = models.TextField(blank=True)  # This field type is a guess.
    date_de_modification = models.DateField(db_column='Date de Modification', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    composition = models.TextField(db_column='Composition', blank=True)  # Field name made lowercase. This field type is a guess.
    nom_en_dci = models.TextField(db_column='Nom en DCI', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    forme = models.TextField(db_column='Forme', blank=True)  # Field name made lowercase. This field type is a guess.
    indication = models.TextField(db_column='Indication', blank=True)  # Field name made lowercase. This field type is a guess.
    posologie = models.TextField(db_column='Posologie', blank=True)  # Field name made lowercase. This field type is a guess.
    mises_en_garde = models.TextField(db_column='Mises en garde', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    contre_indications = models.TextField(db_column='Contre-indications', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    interactions = models.TextField(db_column='Interactions', blank=True)  # Field name made lowercase. This field type is a guess.
    grossesse_et_allaitement = models.TextField(db_column='Grossesse et Allaitement', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    précautions_conduite_auto = models.TextField(db_column='Précautions conduite auto', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    effets_indésirables = models.TextField(db_column='Effets indésirables', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    surdosage = models.TextField(db_column='Surdosage', blank=True)  # Field name made lowercase. This field type is a guess.
    pharmacodynamie = models.TextField(db_column='Pharmacodynamie', blank=True)  # Field name made lowercase. This field type is a guess.
    pharmacocinétique = models.TextField(db_column='Pharmacocinétique', blank=True)  # Field name made lowercase. This field type is a guess.
    etudes_pré_cliniques = models.TextField(db_column='Etudes Pré-cliniques', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    excipients = models.TextField(db_column='Excipients', blank=True)  # Field name made lowercase. This field type is a guess.
    conservation = models.TextField(db_column='Conservation', blank=True)  # Field name made lowercase. This field type is a guess.
    pré_consevation = models.TextField(db_column='Pré-consevation', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    emballage = models.TextField(db_column='Emballage', blank=True)  # Field name made lowercase. This field type is a guess.
    elimination = models.TextField(db_column='Elimination', blank=True)  # Field name made lowercase. This field type is a guess.
    titulaire_de_l_amm = models.TextField(db_column="Titulaire de l'AMM", blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    présentation = models.TextField(db_column='Présentation', blank=True)  # Field name made lowercase. This field type is a guess.
    date_de_première_autorisation = models.DateField(db_column='Date de Première autorisation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_de_révision = models.DateField(db_column='Date de Révision', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dosimétrie = models.TextField(db_column='Dosimétrie', blank=True)  # Field name made lowercase. This field type is a guess.
    radiopharmaceutique = models.TextField(db_column='Radiopharmaceutique', blank=True)  # Field name made lowercase. This field type is a guess.
    conditions_de_prescription = models.TextField(db_column='Conditions de Prescription', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rcp_table'
