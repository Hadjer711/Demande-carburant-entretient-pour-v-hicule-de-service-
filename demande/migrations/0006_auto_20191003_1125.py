# Generated by Django 2.2.5 on 2019-10-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demande', '0005_auto_20191003_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entretient',
            name='telephoneBr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='entretient',
            name='telephonePv',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='entretient',
            name='urgence',
            field=models.CharField(max_length=100),
        ),
    ]
