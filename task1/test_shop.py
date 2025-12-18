import unittest
from shop import Shop, Discount


class TestShop(unittest.TestCase):
    def setUp(self):
        self.shop = Shop("Test-shop", "Supermarket")

    def test_initial_values(self):
        self.assertEqual(self.shop.shopName, "Test-shop")
        self.assertEqual(self.shop.storeType, "Supermarket")
        self.assertEqual(self.shop.numberOfUnits, 0)

    def test_set_number_of_units(self):
        self.shop.set_number_of_units(42)
        self.assertEqual(self.shop.numberOfUnits, 42)

    def test_increment_number_of_units(self):
        self.shop.set_number_of_units(10)
        self.shop.increment_number_of_units(5)
        self.assertEqual(self.shop.numberOfUnits, 15)


class TestDiscount(unittest.TestCase):
    def test_discount_initialization(self):
        products = ["Bread", "Milk"]
        discount_shop = Discount("Discount-shop", "Market", products)

        self.assertEqual(discount_shop.shopName, "Discount-shop")
        self.assertEqual(discount_shop.discountProducts, products)
        self.assertEqual(len(discount_shop.discountProducts), 2)


if __name__ == '__main__':
    unittest.main()