from django.db import models





class Salesmans(models.Model):
    name = models.CharField(max_length=123)
    surname = models.CharField(max_length=123)
    email = models.CharField(max_length=123)
    number = models.BigIntegerField()

class Buyers(models.Model):
    name = models.CharField(max_length=123)
    surname = models.CharField(max_length=123)
    email = models.CharField(max_length=123)
    number = models.BigIntegerField()

class Models(models.Model):
    name = models.CharField(max_length=123)
    dataproizvoystva = models.DateField()


class Cars(models.Model):
    mark = models.CharField(max_length=20)
    model = models.ForeignKey(Models, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    salesman = models.ManyToManyField(Salesmans)

class Sostoyanie(models.Model):
    maxspeed = models.BigIntegerField()
    probeg = models.BigIntegerField()
    sostoyanie = models.CharField(max_length=99999)
    car = models.ManyToManyField(Cars)

class Reviews(models.Model):
    name = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    review = models.CharField(max_length=999999)

class korzina(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)

class otzivi(models.Model):
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    car = models.ManyToManyField(Cars)
    otziv = models.CharField(max_length=35000)
