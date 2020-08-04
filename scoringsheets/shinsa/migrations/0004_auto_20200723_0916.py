# Generated by Django 3.0.4 on 2020-07-23 09:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinsa', '0003_auto_20200704_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojos',
            name='dojo_number',
            field=models.CharField(blank=True, max_length=4, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(4, 'Four digits'), django.core.validators.RegexValidator('^[0-9]*$', 'only numbers')], verbose_name='道場番号'),
        ),
        migrations.AlterField(
            model_name='testee',
            name='membership_number',
            field=models.CharField(blank=True, help_text='Please enter membership number(7digits). like ”0101001” (your dojo number(4 digits) + your dojo’s membership number(3 digits). or space.', max_length=7, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(7, 'Seven digits'), django.core.validators.RegexValidator('^[0-9]*$', 'only numbers')], verbose_name='会員番号'),
        ),
        migrations.AlterField(
            model_name='testee',
            name='testee_name',
            field=models.CharField(help_text='English is okay if you difficult to enter Japanese.', max_length=20, verbose_name='Name Japanese'),
        ),
    ]