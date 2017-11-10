from model_mommy import mommy
from django.shortcuts import resolve_url
from sigemh.core.tests.mixins import BaseTest


class HomeTestCase(BaseTest):

    def setUp(self):
        self.login()
        self.response = self.client.get(resolve_url('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """Must use base.html"""
        self.assertTemplateUsed(self.response, 'index.html')
