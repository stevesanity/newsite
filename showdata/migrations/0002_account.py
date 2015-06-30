# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('FirstName', models.CharField(max_length=15)),
                ('LastName', models.CharField(max_length=15)),
                ('EmailAddress', models.EmailField(max_length=75, serialize=False, primary_key=True)),
                ('PassWord', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
