# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationData',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('DateTime', models.DateTimeField(max_length=7)),
                ('SEX', models.CharField(blank=True, max_length=6)),
                ('AntRvWall', models.IntegerField(blank=True)),
                ('AorticMaxPressureGradient', models.DecimalField(decimal_places=2, blank=True, max_digits=7)),
                ('AorticMeanPressureGradient', models.SmallIntegerField(blank=True)),
                ('BodySurfaceArea', models.DecimalField(decimal_places=3, blank=True, max_digits=9)),
                ('ComputedMitralValveOrifice', models.DecimalField(decimal_places=2, blank=True, max_digits=6)),
                ('EDV', models.DecimalField(decimal_places=2, blank=True, max_digits=8)),
                ('EF', models.DecimalField(decimal_places=2, blank=True, max_digits=7)),
                ('EstimatedEf', models.IntegerField(blank=True)),
                ('EstimatedEfDescriptor', models.CharField(blank=True, max_length=20)),
                ('ESV', models.DecimalField(decimal_places=2, blank=True, max_digits=8)),
                ('LtAtrium', models.SmallIntegerField(blank=True)),
                ('LtVentDiastole', models.SmallIntegerField(blank=True)),
                ('LtVentSystole', models.SmallIntegerField(blank=True)),
                ('LvMass', models.DecimalField(decimal_places=4, blank=True, max_digits=9)),
                ('MitralEstValveOrifice', models.DecimalField(decimal_places=2, blank=True, max_digits=6)),
                ('MitralMaxGradient', models.DecimalField(decimal_places=2, blank=True, max_digits=7)),
                ('PaSystolicPressure', models.DecimalField(decimal_places=3, blank=True, max_digits=10)),
                ('PosteriorWall', models.IntegerField(blank=True)),
                ('PulmonicIntegral', models.SmallIntegerField(blank=True)),
                ('PulmonicMaxPressureGradient', models.SmallIntegerField(blank=True)),
                ('PulmonicMaxVelocity', models.DecimalField(decimal_places=3, blank=True, max_digits=8)),
                ('PulmonicMeanGradient', models.SmallIntegerField(blank=True)),
                ('PulmonicMeanVelocity', models.DecimalField(decimal_places=3, blank=True, max_digits=8)),
                ('RestingDiastolicBp', models.SmallIntegerField(blank=True)),
                ('RestingHeartRate', models.SmallIntegerField(blank=True)),
                ('RestingSystolicBp', models.BigIntegerField(blank=True)),
                ('Rhythm', models.CharField(blank=True, max_length=5)),
                ('Rhythm2', models.CharField(blank=True, max_length=9)),
                ('RtVentricle', models.SmallIntegerField(blank=True)),
                ('Septum', models.IntegerField(blank=True)),
                ('TricusDiasMaxPressGrad', models.DecimalField(decimal_places=5, blank=True, max_digits=10)),
                ('TricusDiasMaxVelMs', models.DecimalField(decimal_places=3, blank=True, max_digits=10)),
                ('TricusRegurgSysMaxVelms', models.IntegerField(blank=True)),
                ('TricuspidMeanGradient', models.IntegerField(blank=True)),
                ('TricuspidMeanVelocity', models.DecimalField(decimal_places=3, blank=True, max_digits=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
