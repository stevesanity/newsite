from django.db import models

# Create your models here.
class Account(models.Model):
    FirstName = models.CharField(max_length=15)
    LastName = models.CharField(max_length=15)
    EmailAddress = models.EmailField (primary_key=True)
    PassWord = models.CharField(max_length=15)

class MedicationData(models.Model):
    ID = models.IntegerField(primary_key=True)
    DateTime = models.DateTimeField(max_length=7)
    SEX = models.CharField(max_length=6, blank=True)
    AntRvWall = models.IntegerField(blank=True)
    AorticMaxPressureGradient = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    AorticMeanPressureGradient = models.SmallIntegerField(blank=True)
    BodySurfaceArea = models.DecimalField(max_digits=9, decimal_places=3, blank=True)
    ComputedMitralValveOrifice = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    EDV = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    EF = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    EstimatedEf = models.IntegerField(blank=True)
    EstimatedEfDescriptor = models.CharField(max_length=20, blank=True)
    ESV = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    LtAtrium = models.SmallIntegerField(blank=True)
    LtVentDiastole = models.SmallIntegerField(blank=True)
    LtVentSystole = models.SmallIntegerField(blank=True)
    LvMass = models.DecimalField(max_digits=9, decimal_places=4, blank=True)
    MitralEstValveOrifice = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    MitralMaxGradient = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    PaSystolicPressure = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    PosteriorWall = models.IntegerField(blank=True)
    PulmonicIntegral = models.SmallIntegerField(blank=True)
    PulmonicMaxPressureGradient = models.SmallIntegerField(blank=True)
    PulmonicMaxVelocity = models.DecimalField(max_digits=8, decimal_places=3, blank=True)
    PulmonicMeanGradient = models.SmallIntegerField(blank=True)
    PulmonicMeanVelocity = models.DecimalField(max_digits=8, decimal_places=3, blank=True)
    RestingDiastolicBp = models.SmallIntegerField(blank=True)
    RestingHeartRate = models.SmallIntegerField(blank=True)
    RestingSystolicBp = models.BigIntegerField(blank=True)
    Rhythm = models.CharField(max_length=5, blank=True)
    Rhythm2 = models.CharField(max_length=9, blank=True)
    RtVentricle = models.SmallIntegerField(blank=True)
    Septum = models.IntegerField(blank=True)
    TricusDiasMaxPressGrad = models.DecimalField(max_digits=10, decimal_places=5, blank=True)
    TricusDiasMaxVelMs = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    TricusRegurgSysMaxVelms = models.IntegerField(blank=True)
    TricuspidMeanGradient = models.IntegerField(blank=True)
    TricuspidMeanVelocity = models.DecimalField(max_digits=8, decimal_places=3, blank=True)

class Medicationdataa:
    db_table = 'my_medication'
    unique_together = ("ID", "DateTime")
