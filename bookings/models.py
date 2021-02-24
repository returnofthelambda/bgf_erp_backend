import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from contracts.models import Sales as SalesContracts

RAILYARD = [('NS', 'NorfolkSouthern'),
            ('CSX', 'CSX'),
            ]
CONTAINER_SIZE = [('20', '20 foot'),
                  ('40S', '40 foot standard'),
                  ('40H', '40 foot highcube'),
                  ]

STEAMSHIPS = [('CMA', 'CMA'),
              ('HMM', 'Hyundai'),
              ('MSC', 'MSC'),
              ('OOCL', 'OOCL'),
              ('ONE', 'ONE'),
              ('ZIM', 'ZIM'),
              ]

STATUS = [('PS', 'Pre-Shipment'),
          ('LG', 'Loading'),
          ('LD', 'Loaded'),
          ('DP', 'Departed'),
          ('SL', 'Sailed'),
          ]

PKG = [
    ('BULK', 'BULK'),
    ('30KG', '30KG'),
    ('60#', '60#'),
]

class Booking(models.Model):
    number = models.CharField(primary_key=True, max_length=25)
    steamship = models.ForeignKey('Steamship',
                                  on_delete=models.CASCADE,)
    railyard = models.CharField(max_length=20, choices=RAILYARD)
    num_of_containers = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    container_size = models.CharField(max_length=20, choices=CONTAINER_SIZE)
    sales_contract = models.ForeignKey(SalesContracts,
                                       on_delete=models.CASCADE)
    # variety = models.CharField(max_length=20)
    # internal_variety = models.CharField(max_length=20)
    destination = models.CharField(max_length=50)
    port_of_loading = models.CharField(max_length=50)
    railcut = models.DateField()
    pkg = models.CharField(max_length=20, choices=PKG, default='BULK')
    lot = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS,
                              default='Pre-Shipment')

    def __str__(self):
        return "{}".format(self.number)


class Steamship(models.Model):
    abbreviation = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=50, blank=True, null=True)
    street2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.abbreviation)
