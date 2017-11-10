from model_mommy import mommy
from django.shortcuts import resolve_url
from sigemh.core.tests.mixins import BaseTest
from sigemh.sectors.models import Sector


class SectorViewListTestCase(BaseTest):

    def setUp(self):
        self.login()
        mommy.make('sectors.Sector', name='Test')
        self.response = self.client.get(resolve_url('sectors:list'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'sectors/list.html')

    def test_html(self):
        contents = (
            ('<th>Nome</th>', 1),
            ('Test</a>', 1),
        )
        for text, count in contents:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_context_data(self):
        self.assertTrue(self.response.context['object_list'])


class SectorViewListNotAuthenticatedTestCase(BaseTest):

    def setUp(self):
        self.response = self.client.get(resolve_url('sectors:list'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 302)

    def test_url(self):
        self.assertEqual(self.response.url, '/login/?next=/setores/')


class SectorCreateViewGetTestCase(BaseTest):

    def setUp(self):
        self.login()
        self.response = self.client.get(resolve_url('sectors:create'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'sectors/form.html')

    def test_html(self):
        contents = (
            ('<input', 2),
            ('type="text', 2),
            ('type="submit', 1),
        )
        for text, count in contents:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_context_data(self):
        self.assertTrue(self.response.context['form'])


class SectorViewListGetNotAuthenticatedTestCase(BaseTest):

    def setUp(self):
        self.response = self.client.get(resolve_url('sectors:create'))

    def test_get(self):
        self.assertEqual(self.response.status_code, 302)

    def test_url(self):
        self.assertEqual(self.response.url, '/login/?next=/setores/novo/')


class SectorCreateViewPostTestCase(BaseTest):

    def setUp(self):
        self.login()
        data = {
            'name': 'Setor 1'
        }
        self.response = self.client.post(resolve_url('sectors:create'), data=data)

    def test_post(self):
        self.assertEqual(self.response.status_code, 302)

    def test_url(self):
        self.assertEqual(self.response.url, '/setores/')

    def test_objects_exists(self):
        self.assertTrue(Sector.objects.exists())


class SectorCreateViewPostNotAuthenticatedTestCase(BaseTest):

    def setUp(self):
        data = {
            'name': 'Setor 1'
        }
        self.response = self.client.post(resolve_url('sectors:create'), data=data)

    def test_post(self):
        self.assertEqual(self.response.status_code, 302)

    def test_url(self):
        self.assertEqual(self.response.url, '/login/?next=/setores/novo/')

    def test_objects_not_exists(self):
        self.assertFalse(Sector.objects.exists())


class SectorUpdateViewGetTestCase(BaseTest):

    def setUp(self):
        self.login()
        sector = mommy.make('sectors.Sector', name='Test')
        self.response = self.client.get(resolve_url('sectors:update', pk=sector.pk))

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'sectors/form.html')

    def test_html(self):
        contents = (
            ('<input', 2),
            ('type="text', 2),
            ('type="submit', 1),
        )
        for text, count in contents:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_context_data(self):
        self.assertTrue(self.response.context['form'])


class SectorUpdateViewPostNotAuthenticatedTestCase(BaseTest):

    def setUp(self):
        self.sector = mommy.make('sectors.Sector', name='Test')
        self.response = self.client.get(resolve_url('sectors:update', pk=self.sector.pk))

    def test_post(self):
        self.assertEqual(self.response.status_code, 302)

    def test_url(self):
        self.assertEqual(self.response.url, '/login/?next=/setores/{}/editar/'.format(self.sector.pk))


class SectorDeleteViewTestCase(BaseTest):

    def setUp(self):
        self.login()
        sector = mommy.make('sectors.Sector', name='Test')
        self.response = self.client.delete(resolve_url('sectors:delete', pk=sector.pk))

    def test_objects_not_exists(self):
        self.assertFalse(Sector.objects.exists())
