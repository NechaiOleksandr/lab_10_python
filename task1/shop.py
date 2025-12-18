class Shop:
    def __init__(self, shopName, storeType):
        self.shopName = shopName
        self.storeType = storeType
        self.numberOfUnits = 0

    def describe_shop(self):
        print(f"\nМагазин: '{self.shopName}'")
        print(f"Тип: {self.storeType}")
        print(f"Кількість видів товару: {self.numberOfUnits}")

    def open_shop(self):
        print(f"Магазин '{self.shopName}' відкрито")

    def set_number_of_units(self, number):
        self.numberOfUnits = number
        print(f"Кількість видів товару встановлено: {self.numberOfUnits}")

    def increment_number_of_units(self, increment):
        self.numberOfUnits += increment
        print(f"Кількість видів товару збільшено на {increment}. Тепер: {self.numberOfUnits}")

class Discount(Shop):
    def __init__(self, shopName, storeType, discountProducts):
        super().__init__(shopName, storeType)
        self.discountProducts = discountProducts

    def get_discounts_products(self):
        print("\nТовари зі знижкою:")
        for product in self.discountProducts:
            print(f"{product}")
