# Generated by Django 4.2.6 on 2023-11-03 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description',
            new_name='des',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='image',
            new_name='img',
        ),
    ]
