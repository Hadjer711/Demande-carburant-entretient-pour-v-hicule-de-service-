# Generated by Django 2.2.5 on 2019-09-28 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carburant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prenom', models.CharField(max_length=120)),
                ('structure', models.CharField(max_length=120)),
                ('compteAnalytique', models.CharField(max_length=200)),
                ('telephonePv', models.CharField(max_length=10)),
                ('telephoneBr', models.CharField(max_length=5)),
                ('vehicule', models.CharField(max_length=100)),
                ('alimentation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entretient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prenom', models.CharField(max_length=120)),
                ('service', models.CharField(max_length=120)),
                ('immatriculation', models.CharField(max_length=200)),
                ('kilometrage', models.CharField(max_length=10)),
                ('marque', models.CharField(max_length=5)),
                ('type', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('telephonePv', models.CharField(max_length=10)),
                ('telephoneBr', models.CharField(max_length=5)),
                ('description', models.TextField()),
                ('urgence', models.CharField(max_length=50)),
            ],
        ),
    ]
