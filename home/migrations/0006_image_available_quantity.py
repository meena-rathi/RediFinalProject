# Generated by Django 4.2.6 on 2023-11-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='available_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
