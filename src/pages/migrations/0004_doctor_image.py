# Generated by Django 3.2.9 on 2021-12-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_ambulance'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]