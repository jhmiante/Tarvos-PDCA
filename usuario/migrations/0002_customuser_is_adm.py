# Generated by Django 3.1.7 on 2021-03-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_adm',
            field=models.BooleanField(default=False, verbose_name='Usuário Administrativo'),
        ),
    ]