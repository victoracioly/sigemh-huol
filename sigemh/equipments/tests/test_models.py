from datetime import datetime

from sigemh.core.tests.mixins import BaseTest
from sigemh.equipments.models import Equipment
from sigemh.equipments.models import EquipmentType


class EquipmentTypeModelTest(BaseTest):

    def setUp(self):
        self.obj = EquipmentType(name='Test')
        self.obj.save()

    def test_create(self):
        self.assertTrue(EquipmentType.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_slug(self):
        self.assertEqual(self.obj.slug, 'test')

    def test_str(self):
        self.assertEqual('Test', str(self.obj))


class EquipmentModelTest(BaseTest):

    def setUp(self):
        equipment_type = EquipmentType.objects.create(name='Test')
        self.obj = Equipment(equipment_type=equipment_type, patrimony='123456', serial_number='789000')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Equipment.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_patrimony(self):
        self.assertEqual(self.obj.patrimony, '123456')

    def test_patrimony(self):
        self.assertEqual(self.obj.serial_number, '789000')

    def test_str(self):
        self.assertEqual('Test - 123456', str(self.obj))
