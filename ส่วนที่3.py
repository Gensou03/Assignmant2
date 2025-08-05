
# ส่วนที่ 3: ระบบร้านค้าออนไลน์
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Customer:
    def __init__(self, name="Anonymous", email="customer@example.com"):
        self.name = name 
        self.email = email  
        self.__cart = []  

    def add_to_cart(self, name, quantity):
        product = Product(name, quantity)
        self.__cart.append(product)
        print(f"{self.name} added {name} with quantity {quantity} to cart.")

    def remove_from_cart(self, name):
        for product in self.__cart:
            if product.name.lower() == name.lower():
                self.__cart.remove(product)
                print(f"{self.name} removed {name} from cart.")
                return
        print(f"Product {name} not found in {self.name}'s cart.")

    def update_cart_quantity(self, name, quantity):
        for product in self.__cart:
            if product.name.lower() == name.lower():
                product.quantity = quantity
                print(f"{self.name} updated {name} to quantity {quantity} in cart.")
                return
        print(f"Product {name} not found in {self.name}'s cart.")

    def show_cart(self):
        if not self.__cart:
            print(f"No products in {self.name}'s cart.")
        else:
            print(f"{self.name}'s cart (Email: {self.email}):")
            for product in self.__cart:
                print(f"- {product.name}: {product.quantity} units")

def manage_customer_cart():
    customer_name = input("Enter customer name: ")
    customer_email = input("Enter customer email: ")
    customer = Customer(customer_name, customer_email)

    while True:
        print(f"\n=== {customer_name}'s Cart Management ===")
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. Update product quantity")
        print("4. Show cart")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter product name: ")
            try:
                quantity = int(input("Enter product quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative. Please try again.")
                    continue
                customer.add_to_cart(name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")

        elif choice == '2':
            name = input("Enter product name to remove: ")
            customer.remove_from_cart(name)

        elif choice == '3':
            name = input("Enter product name to update: ")
            try:
                quantity = int(input("Enter new quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative. Please try again.")
                    continue
                customer.update_cart_quantity(name, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")

        elif choice == '4':
            customer.show_cart()

        elif choice == '5':
            print(f"Exiting {customer_name}'s Cart Management.")
            break

        else:
            print("Invalid choice. Please select 1-5.")

manage_customer_cart()

