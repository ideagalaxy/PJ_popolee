# Generated by Django 5.1.1 on 2025-04-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='instaID',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='realname',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
