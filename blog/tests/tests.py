from django.urls import reverse, resolve
from django.test import TestCase
from .views import post_list

class TestsView(TestCase):
    def test_post_list_view_status_code(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_post_list_url_resolves_post_list_view(self):
        view = resolve('/')
        self.assertEquals(view.func, post_list)

#test 詳細　$ python manage.py test --verbosity 0　～　3　で表示