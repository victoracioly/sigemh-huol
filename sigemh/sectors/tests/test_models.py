from datetime import datetime

from sigemh.core.tests.mixins import BaseTest
from sigemh.sectors.models import Sector


class SectorModelTest(BaseTest):

    def setUp(self):
        self.obj = Sector(name='Test')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Sector.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Test', str(self.obj))
