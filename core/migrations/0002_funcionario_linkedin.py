# Generated by Django 4.0.3 on 2022-03-15 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='linkedin',
            field=models.CharField(default='#', max_length=100, verbose_name='Linkedin'),
        ),
    ]
