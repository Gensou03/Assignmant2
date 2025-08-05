
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.__products.append(product)
        print(f"Added {name} with quantity {quantity} to the store.")

    def show_products(self):
        if not self.__products:
            print("No products in the store.")
        else:
            print("Products in the store:")
            for product in self.__products:
                print(f"- {product.name}: {product.quantity} units")

my_store = Store()
my_store.add_product("Computer", 10)
my_store.add_product("Notebook", 20)
my_store.show_products()
