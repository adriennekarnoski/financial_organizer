import io
import json
import os
import pickle


class Vendor(object):
    """Class for vendor object."""

    def __init__(self, name):
        self.name = name
        self.sales_day = None
        self.delivery_day = []
        self.products = []
        self.credit_policy = None

    def add_sales_day(self, weekday):
        """Add sales day to vendor object."""
        self.sales_day = weekday

    def add_delivery_day(self, weekday):
        """Add delivery day to vendor object."""
        self.delivery_day = weekday

    def add_products(self, product):
        """Add products to the vendor object."""
        if isinstance(product, list):
            for item in product:
                self.products.append(item)
        else:
            self.products.append(product)