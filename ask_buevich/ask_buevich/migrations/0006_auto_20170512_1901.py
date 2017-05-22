# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_buevich', '0005_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
