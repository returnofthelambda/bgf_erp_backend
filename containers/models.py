import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

from smart_selects.db_fields import ChainedForeignKey

from bookings.models import Booking, Steamship

RAILYARD = [('NS', 'NorfolkSouthern'),
            ('CSX', 'CSX'),
            ]
CONTAINER_SIZE = [('20', '20 foot'),
                  ('40S', '40 foot standard'),
                  ('40H', '40 foot highcube'),
                  ]


STATUS = [('PS', 'Pre-Shipment'),
          ('LG', 'Loading'),
          ('LD', 'Loaded'),
          ('DP', 'Departed'),
          ('SL', 'Sailed'),
          ]


class Container(models.Model):
    number = models.CharField(max_length=12, validators=[RegexValidator(
        regex=r'[a-zA-Z]{4}\d{6}\-\d{1}', message="Please enter in the format\
        : ABCD123456-7.")])
    pickup_date = models.DateField()
    load_date = models.DateField(null=True, blank=True)
    departure_date = models.DateField(null=True, blank=True)
    steamship = models.ForeignKey(Steamship,
                                  on_delete=models.CASCADE,)
    booking = ChainedForeignKey(
        Booking,
        chained_field='steamship',
        chained_model_field='steamship',
        show_all=False,
        auto_choose=True,
        blank=True,
        null=True)
    railyard = models.CharField(max_length=20, choices=RAILYARD)
    size = models.CharField(max_length=20, choices=CONTAINER_SIZE)
    status = models.CharField(max_length=10, choices=STATUS,
                              default='Pre-Shipment', blank=True)

    def __str__(self):
        return "{}".format(self.number)


class Booking(Booking):
    pass
