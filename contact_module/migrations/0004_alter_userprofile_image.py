# Generated by Django 4.2 on 2023-07-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
