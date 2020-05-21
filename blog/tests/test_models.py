import pytest



@pytest.mark.django_db
def test_blog_model(setup_post_model):
    assert setup_post_model.__str__() == "post sample model"


@pytest.mark.django_db
def test_comment_model(setup_comment_model):
    assert setup_comment_model.__str__() == "comment sample model"






