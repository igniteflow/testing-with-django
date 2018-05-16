# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=50)
    num_doors = models.IntegerField()
