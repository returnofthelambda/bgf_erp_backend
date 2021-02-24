from django.db import models

UNITS = [
    ('MT', 'MT'),
    ('BU', 'BU'),
    ('LBS', 'LBS'),
    ('ST', 'ST'),
]

PKG = [
    ('BULK', 'BULK'),
    ('30KG', '30KG'),
    ('60#', '60#'),
]


class Purchase(models.Model):
    pass


class Sales(models.Model):
    number = models.CharField(primary_key=True, max_length=20)
    customer = models.CharField(max_length=50)  # eventually link to cust model
    variety = models.CharField(max_length=20)  # eventually link
    quantity = models.DecimalField(max_digits=15, decimal_places=3)
    units = models.CharField(max_length=10, choices=UNITS)
    pkg = models.CharField(max_length=10, choices=PKG)

    def __str__(self):
        return "{}".format(self.number)
