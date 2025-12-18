from shop import Shop, Discount

store = Shop("Rozetka", "Online Supermarket")
store.describe_shop()
store.open_shop()

store1 = Shop("Silpo", "Grocery")
store2 = Shop("Comfy", "Electronics")
store3 = Shop("Eva", "Beauty")
store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

print(f"Початкова кількість товарів у магазині: {store.numberOfUnits}")
store.numberOfUnits = 50
print(f"Змінена кількість товарів: {store.numberOfUnits}")

store.set_number_of_units(100)
store.increment_number_of_units(25)

productsList = ["iPhone 13", "Samsung TV", "PlayStation 5"]
storeDiscount = Discount("CyberFriday", "Electronics", productsList)
storeDiscount.get_discounts_products()
storeDiscount.describe_shop()

all_store = Shop("ATB", "Grocery")
all_store.open_shop()