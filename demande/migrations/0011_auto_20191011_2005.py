# Generated by Django 2.2.5 on 2019-10-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demande', '0010_auto_20191010_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='carburant',
            name='traite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entretient',
            name='traite',
            field=models.BooleanField(default=False),
        ),
    ]
