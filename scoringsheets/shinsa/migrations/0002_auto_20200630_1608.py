# Generated by Django 3.0.4 on 2020-06-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinsa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testee',
            name='testee_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name Japanese'),
        ),
    ]