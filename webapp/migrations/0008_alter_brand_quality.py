# Generated by Django 5.0.1 on 2024-02-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='quality',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
