from model_mommy import mommy
from django.test import TestCase
from django.shortcuts import resolve_url


class BaseTest(TestCase):

    def login(self):
        self.create_user()
        data = {
            'username': self.user.username,
            'password': '12345678'
        }
        self.client.post(resolve_url('login'), data=data)
        self.user

    def create_user(self):
        self.user = mommy.make('auth.User', username='username')
        self.user.set_password('12345678')
        self.user.save()
