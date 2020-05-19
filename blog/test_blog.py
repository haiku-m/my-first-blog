import pytest
from django.urls import reverse
from django.test import TestCase
from . import views
from bs4 import BeautifulSoup
import requests
from .models import Post, Comment


def test_blog_index(client):

    """display check"""
    response = client.get(reverse('post_detail'))
    assert response.status_code == 200
