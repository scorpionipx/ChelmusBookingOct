# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-21 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0006_advertisement_main_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='main_image',
            field=models.ImageField(blank=True, default=None, help_text='Imaginea de prezentare', null=True, upload_to='profiles/%Y/%m/%d', verbose_name='Imaginea de profil'),
        ),
        migrations.AlterUniqueTogether(
            name='advertisement',
            unique_together=set([]),
        ),
    ]