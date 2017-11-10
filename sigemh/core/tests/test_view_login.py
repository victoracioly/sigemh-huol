from model_mommy import mommy
from django.shortcuts import resolve_url
from sigemh.core.tests.mixins import BaseTest


class LoginGetTestCase(BaseTest):

    def setUp(self):
        self.response = self.client.get(resolve_url('login'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'login.html')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_html(self):
        contents = (
            ('<form', 1),
            ('<input', 3),
            ('type="text"', 1),
            ('type="password"', 1),
            ('type="submit"', 1)
        )
        for text, count in contents:
            with self.subTest():
                self.assertContains(self.response, text, count)


class LoginPostTestCase(BaseTest):

    def setUp(self):
        self.create_user()
        data = {
            'username': self.user.username,
            'password': '12345678'
        }
        self.response = self.client.post(resolve_url('login'), data=data)

    def test_redirect(self):
        self.assertEqual(302, self.response.status_code)
