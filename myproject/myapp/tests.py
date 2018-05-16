# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from .models import Car


# models
class CarTestCase(TestCase):

    def test_name(self):
        car = Car(name="foo")
        self.assertEqual(
            car.name, "foo"
        )

    def test_car_doors(self):
        car = Car(num_doors=1)
        self.assertEqual(
            car.num_doors, 1
        )


# views
class IndexTestCase(TestCase):

    def test_success(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)