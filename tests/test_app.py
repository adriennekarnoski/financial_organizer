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


def test_add_sales_day(app_fixture):
    """Test the add_sales_day method."""
    app_fixture.add_sales_day('Friday')
    assert app_fixture.sales_day == 'Friday'


def test_add_single_product(app_fixture):
    """Test adding a single product to vendor object."""
    app_fixture.add_products('Pepsi')
    assert len(app_fixture.products) == 1
    assert app_fixture.products[0] == 'Pepsi'


def test_adding_multiple_products(app_fixture):
    """Test adding a single product to vendor object."""
    app_fixture.add_products(['Pepsi', 'Coke', 'Sprite'])
    assert len(app_fixture.products) == 3
