# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RcpTable(models.Model):
    rcp_id = models.IntegerField(blank=True, null=True)
    spec_name = models.TextField(blank=True)  # This field type is a guess.
    date_de_modification = models.DateField(db_column='Date de Modification', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    composition = models.TextField(db_column='Composition', blank=True)  # Field name made lowercase. This field type is a guess.
    nom_en_dci = models.TextField(db_column='Nom en DCI', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    forme = models.TextField(db_column='Forme', blank=True)  # Field name made lowercase. This field type is a guess.
    indication = models.TextField(db_column='Indication', blank=True)  # Field name made lowercase. This field type is a guess.
    posologie = models.TextField(db_column='Posologie', blank=True)  # Field name made lowercase. This field type is a guess.
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
