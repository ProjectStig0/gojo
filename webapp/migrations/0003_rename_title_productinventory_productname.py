# Generated by Django 5.0.1 on 2024-01-30 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_album_productinventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinventory',
            old_name='title',
            new_name='productname',
        ),
    ]
