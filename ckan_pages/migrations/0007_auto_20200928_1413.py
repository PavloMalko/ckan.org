# Generated by Django 3.1.1 on 2020-09-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckan_pages', '0006_auto_20200928_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ckanforpage',
            name='upper_text',
            field=models.TextField(blank=True, help_text='Upper text block', max_length=2056),
        ),
    ]