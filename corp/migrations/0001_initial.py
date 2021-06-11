# Generated by Django 3.2.4 on 2021-06-10 14:17

from django.db import migrations, models
import django.db.models.deletion

# Fichier cree automatiquement apres un python3 manage.py makemigration

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adherent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CIVILITE', models.CharField(max_length=30)),
                ('NOM', models.CharField(max_length=30)),
                ('PRENOM', models.CharField(max_length=30)),
                ('PHOTO', models.ImageField(upload_to='')),
                ('STATUS', models.CharField(max_length=30)),
                ('LIEU_NAISSANCE', models.CharField(max_length=30)),
                ('DATE_NAISSANCE', models.DateField()),
                ('TEL_FIX', models.CharField(max_length=10)),
                ('TEL_PORT', models.CharField(max_length=30)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('ROLE_ADHERENT', models.CharField(max_length=30)),
                ('REMARQUE', models.CharField(max_length=500)),
                ('CLE_MOULIN', models.BooleanField(default=False)),
                ('FONCTION', models.CharField(max_length=30)),
                ('MBCA', models.BooleanField(default=False)),
                ('NUM_LICENCE', models.CharField(max_length=20)),
                ('TYPE_LICENCE', models.CharField(max_length=10)),
                ('ASSURANCE_COMP', models.CharField(max_length=30)),
                ('CLUB', models.CharField(max_length=30)),
                ('DATE_INSCRIPTION', models.DateField()),
                ('ADD_1', models.CharField(max_length=30)),
                ('ADD_2', models.CharField(max_length=30)),
                ('ADD_3', models.CharField(max_length=30)),
                ('CP', models.CharField(max_length=5)),
                ('VILLE', models.CharField(max_length=30)),
                ('PAYS', models.CharField(max_length=30)),
                ('PER_CONTACT', models.CharField(max_length=30)),
                ('NUM_PER_CONTACT', models.CharField(max_length=30)),
                ('ALLERGIE', models.BooleanField()),
                ('MDC_REF', models.CharField(max_length=30)),
                ('NUM_TEL_MDC', models.CharField(max_length=10)),
                ('DATE_RGL', models.DateTimeField()),
                ('MODE_PAIEMENT', models.CharField(max_length=10)),
                ('NB_CHEQUE', models.IntegerField()),
                ('MONTANT', models.IntegerField()),
                ('ADHESION', models.CharField(max_length=30)),
                ('LICENCE', models.BooleanField(default=False)),
                ('LOC_DETENTEUR', models.BooleanField()),
                ('LOC_STAB', models.BooleanField()),
                ('LOC_BLOC', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Assurance_Complementaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOM_ASSURANCE', models.CharField(max_length=100)),
                ('DATE_REGLEMENT', models.DateTimeField()),
                ('MODE_PAIEMENT', models.CharField(max_length=10)),
                ('NB_CHEQUE', models.IntegerField()),
                ('MONTANT', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Certif_Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_DEBUT', models.DateField()),
                ('D_FIN', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H_DEBUT', models.DateTimeField()),
                ('H_FIN', models.DateTimeField()),
                ('NB_PERS_MAX', models.IntegerField()),
                ('DATE', models.DateField()),
                ('NB_PERS', models.IntegerField()),
                ('ETAT_EVENEMENT', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOM_EVENEMENT', models.CharField(max_length=30)),
                ('ID_ADHERENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corp.adherent')),
                ('ID_EVENEMENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corp.evenement')),
            ],
        ),
        migrations.AddField(
            model_name='adherent',
            name='ID_ASSURANCE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corp.assurance_complementaire'),
        ),
        migrations.AddField(
            model_name='adherent',
            name='ID_CERTIF',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corp.certif_medical'),
        ),
    ]
