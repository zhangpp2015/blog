# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161101_1036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['index', '-id'], 'verbose_name': '\u5e7f\u544a', 'verbose_name_plural': '\u5e7f\u544a'},
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(default=0, verbose_name='0\uff1a\u7537\uff0c1\uff1a\u5973', choices=[(0, b'\xe7\x94\xb7'), (1, b'\xe5\xa5\xb3')]),
        ),
    ]
