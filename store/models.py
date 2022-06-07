from django.db import models

from users.models import User


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)

    def __str__(self):
        return self.name


    


class Yard(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name        


class OverheadCost(models.Model):
    yard = models.ForeignKey(Yard, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    cost = models.IntegerField()

    def __str__(self):
        return self.name    


class MixMaterial(models.Model):
    yard = models.ForeignKey(Yard, on_delete=models.CASCADE)
    alu = models.IntegerField()
    zn = models.IntegerField()
    aluc = models.IntegerField()
    ss = models.IntegerField()
    pb = models.IntegerField()
    pvc = models.IntegerField()
    fibre = models.IntegerField()
    others1 = models.IntegerField()
    others2 = models.IntegerField()
    nm = models.IntegerField()

    total = models.IntegerField()

    def __str__(self):
        return self.name


class MatMix(models.Model):
    yard = models.ForeignKey(Yard, on_delete=models.CASCADE)
    cha = models.IntegerField()
    oil = models.IntegerField()
    vp = models.IntegerField()
    oh = models.IntegerField()
    dep = models.IntegerField()
    trans = models.IntegerField()
    flux = models.IntegerField()
    cusi = models.IntegerField()
    extrasi = models.IntegerField()
    gst = models.IntegerField()
    extracost = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.name        


class MaterialMixP(models.Model):
    yard = models.ForeignKey(Yard, on_delete=models.CASCADE)
    alu = models.IntegerField()
    zn = models.IntegerField()
    aluc = models.IntegerField()
    ss = models.IntegerField()
    pb = models.IntegerField()
    pvc = models.IntegerField()
    fibre = models.IntegerField()
    others1 = models.IntegerField()
    others2 = models.IntegerField()
    nm = models.IntegerField()

    total = models.IntegerField()

    def __str__(self):
        return self.name        








