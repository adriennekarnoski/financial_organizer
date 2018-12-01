"""Test funtions for app.py."""
import pytest


@pytest.fixture
def app_fixture():
    from app import Vendor
    v = Vendor('Test')
    return v


def test_add_delivery_day(app_fixture):
    """Test the add_delivery_day method."""
    app_fixture.add_delivery_day('Monday')
    assert app_fixture.delivery_day == 'Monday'
