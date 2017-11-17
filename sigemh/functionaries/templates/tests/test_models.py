from datetime import datetime

from sigemh.core.tests.mixins import BaseTest
from sigemh.functionaries.models import Functionary


class SectorModelTest(BaseTest):

    def setUp(self):
        self.obj = Functionary(name='Test')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Functionary.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Test', str(self.obj))