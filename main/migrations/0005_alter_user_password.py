# Generated by Django 4.1.1 on 2022-09-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_emial_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
