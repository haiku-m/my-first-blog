import pytest
from django.contrib.auth.models import User
from . .models import Post, Comment

@pytest.fixture()
def setup_post_model():
    post_data = Post(author=User.objects.create(username="test"),
                            title="post sample model", text="test")
    return post_data

@pytest.fixture()
def setup_comment_model():
    comment_data = Comment(post = Post.objects.create(author=User.objects.create(username="test"),
                    title="post sample model", text="test"), author="other",
                    text="comment sample model")
    return comment_data
