from django.db import models


class Card(models.Model):
    VALUE_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    first_side_text = models.CharField(max_length=200)
    second_side_text = models.CharField(max_length=200)
    show_date = models.DateTimeField('show date')
    value = models.IntegerField(max_length=10, choices=VALUE_CHOICES, default=2)