# Generated by Django 3.2.16 on 2023-07-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
