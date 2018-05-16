# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase


class MyFirstTestCase(TestCase):

    def test_addition(self):
        self.assertEqual(2 + 2, 4)
