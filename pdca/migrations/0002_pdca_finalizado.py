# Generated by Django 3.1.7 on 2021-03-26 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdca',
            name='finalizado',
            field=models.BooleanField(default=False, verbose_name='Finalizado'),
        ),
    ]
