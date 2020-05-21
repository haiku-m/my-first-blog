import pytest
from django.urls import reverse
from django.test import TestCase
from . . import views
from . .views import post_list

@pytest.mark.django_db
def test_post_list(client):
    response = client.get(reverse('blog:post_list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_detail(client):
    response = client.get(reverse('blog:post_detail', kwargs=dict(pk=u'1')))
    assert response.status_code == 404
    
@pytest.mark.django_db
def test_post_new(client):
    response = client.get(reverse('blog:post_new'))
    assert response.status_code == 302

@pytest.mark.django_db
def test_post_edit(client):
    response = client.get(reverse('blog:post_edit', kwargs=dict(pk=u'1')))
    assert response.status_code == 302

def test_post_draft_list(client):
    response = client.get(reverse('blog:post_draft_list'))
    assert response.status_code == 302



