# Generated by Django 4.1 on 2022-09-07 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTenis', '0002_integrantesclub_delete_catcuarta_delete_catdamas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantesclub',
            name='genero',
            field=models.CharField(max_length=5),
        ),
    ]
