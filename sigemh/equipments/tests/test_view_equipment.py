from model_mommy import mommy
from django.shortcuts import resolve_url
from sigemh.core.tests.mixins import BaseTest


class EquipmentListViewTestCase(BaseTest):

    def setUp(self):
        self.login()
        equipment_type1 = mommy.make('equipments.EquipmentType', name='Ventilador')
        equipment_type2 = mommy.make('equipments.EquipmentType', name='Carro de Anestesia')
        mommy.make('equipments.Equipment', equipment_type=equipment_type1, serial_number='000', patrimony='0000')
        self.response = self.client.get(resolve_url('equipments:list'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'equipments/list.html')

    def test_html(self):
        contents = (
            ('<th>Nome</th>', 1),
            ('<th>Quantidade</th>', 1),
            ('Ventilador', 1),
            ('Carro de Anestesia', 1),
            ('<td>0</td>', 1),
            ('<td>1</td>', 1),
        )
        for text, count in contents:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_context_data(self):
        self.assertTrue(self.response.context['object_list'])


class EquipmentDetailViewTestCase(BaseTest):

    def setUp(self):
        self.login()
        sector = mommy.make('sectors.Sector', name='Cardiologia')
        equipment_type = mommy.make('equipments.EquipmentType', name='Ventilador')

        mommy.make('equipments.Equipment', equipment_type=equipment_type, serial_number='123', patrimony='1234',
                   sector=sector)
        mommy.make('equipments.Equipment', equipment_type=equipment_type, serial_number='456', patrimony='5678',
                   sector=sector)
        mommy.make('equipments.Equipment', equipment_type=equipment_type, serial_number='789', patrimony='9012',
                   sector=sector)
        mommy.make('equipments.Equipment', equipment_type=equipment_type, serial_number='012', patrimony='3456',
                   sector=sector)
        mommy.make('equipments.Equipment', equipment_type=equipment_type, serial_number='000', patrimony='0000')

        self.response = self.client.get(resolve_url('equipments:detail', slug=equipment_type.slug))

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'equipments/detail.html')

    def test_html(self):
        contents = (
            ('<th>Patrimônio</th>', 1),
            ('<th>Número de Série</th>', 1),
            ('<th>Setor</th>', 1),
            ('<td>123</td>', 1),
            ('<td>1234</td>', 1),
            ('<td>Cardiologia</td>', 4),
            ('<td>-</td>', 1),
            ('<td>456</td>', 1),
            ('<td>5678</td>', 1),
            ('<td>789</td>', 1),
            ('<td>9012</td>', 1),
            ('<td>012</td>', 1),
            ('<td>3456</td>', 1),
            ('<h4>Ventilador</h4>', 1),
        )
        for text, count in contents:
            with self.subTest():
                self.assertContains(self.response, text, count)


class EquipmentDetailViewNotFoundTestCase(BaseTest):

    def setUp(self):
        self.login()
        self.response = self.client.get(resolve_url('equipments:detail', slug='not-exists'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 404)


class EquipmentDetailViewNotAuthenticatedTestCase(BaseTest):

    def setUp(self):
        self.response = self.client.get(resolve_url('equipments:detail', slug='not-exists'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 302)

    def test_url(self):
        self.assertEqual(self.response.url, '/login/?next=/equipamentos/not-exists/')
