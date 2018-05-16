# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse


class IndexTestCase(TestCase):

    def test_success(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)