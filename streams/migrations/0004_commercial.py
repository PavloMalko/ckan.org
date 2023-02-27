# Generated by Django 3.1 on 2021-03-25 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('streams', '0003_poweringimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.URLField(help_text='Add this Company URL')),
                ('level', models.CharField(max_length=256)),
                ('about', models.TextField(max_length=1028)),
                ('date_info', models.TextField(max_length=128)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Commercial',
                'verbose_name_plural': 'Commercials',
            },
        ),
    ]