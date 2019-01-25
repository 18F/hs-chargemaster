import pytest
from django.contrib.auth.models import User, Group


@pytest.mark.django_db
def test_users():
    assert User.objects.count() == 0


@pytest.mark.django_db
def test_groups():
    assert Group.objects.count() == 0
