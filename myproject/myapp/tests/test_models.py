# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import skip

from django.test import TestCase

from ..models import Car


class CarTestCase(TestCase):

    def test_name(self):
        car = Car(name="foo")
        self.assertEqual(
            car.name, "foo"
        )

    @skip('Skipping')
    def test_car_doors(self):
        car = Car(num_doors=1)
        self.assertEqual(
            car.num_doors, 1
        )