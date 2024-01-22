class Product:
    def __init__(self, id, name, price, stock_quantity, description, images):
        self.id = id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.description = description
        self.images = images

    def __str__(self):
        return f"Product {self.id}: {self.name} ({self.price}€)"

    def update_stock(self, quantity):
        self.stock_quantity -= quantity

    def is_in_stock(self, quantity):
        return self.stock_quantity >= quantity

class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.total_price = 0.0

    def add_item(self, product, quantity):
        if product.is_in_stock(quantity):
            self.items[product.id] = self.items.get(product.id, 0) + quantity
            self.total_price += product.price * quantity
            product.update_stock(quantity)
        else:
            print(f"Not enough stock available for {product.name}")

    def remove_item(self, product, quantity):
        if product.id in self.items:
            self.items[product.id] = max(0, self.items[product.id] - quantity)
            self.total_price -= product.price * quantity
            product.update_stock(-quantity)
        else:
            print(f"{product.name} is not in your cart")

    def empty_cart(self):
        self.items = {}
        self.total_price = 0.0

    def checkout(self):
        # Create an order instance and update stock levels
        # Clear the cart
        pass

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password  # hash the password before storing
        self.email = email
        self.order_history = []

    def __str__(self):
        return f"User: {self.username} ({self.email})"

    def login(self, password):
        # compare hashed password with the stored hash
        pass

    def register(self):
        # store user data in a secure way
        pass

    def add_order(self, order):
        self.order_history.append(order)
product1 = Product(1, "T-Shirt", 19.99, 10, "Comfortable cotton T-Shirt", ["image1.jpg", "image2.jpg"])
product2 = Product(2, "Jeans", 39.99, 5, "Durable denim jeans", ["image3.jpg", "image4.jpg"])

cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2, 1)

print(f"Cart Contents: {cart.items}")
print(f"Total Price: {cart.total_price}€")

cart.remove_item(product1, 1)
print(f"Cart Contents: {cart.items}")
print(f"Total Price: {cart.total_price}€")



