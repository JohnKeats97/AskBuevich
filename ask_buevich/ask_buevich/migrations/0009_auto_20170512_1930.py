# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_buevich', '0008_auto_20170512_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to='ask_buevich.Profile'),
        ),
    ]
