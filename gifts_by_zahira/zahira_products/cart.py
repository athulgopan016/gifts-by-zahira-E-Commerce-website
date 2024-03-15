from decimal import Decimal
from django.conf import settings
from zahira_products.models import Product
from django.shortcuts import get_object_or_404

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product_id, quantity=1):
        product_id = int(product_id)
        try:
            product = Product.objects.get(id=product_id)
            if product_id not in self.cart:
                self.cart[product_id] = {
                    'quantity': 0,
                    'price': str(product.price),
                    'name': product.name,  # Added product name
                    'image_url': product.image.url  # Added product image URL
                }

            self.cart[product_id]['quantity'] += int(quantity)
            self.save()
        except Product.DoesNotExist:
            return

    def save(self):
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.cart = {}
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
            cart[str(product.id)]['name'] = product.name  # Added product name
            cart[str(product.id)]['image_url'] = product.image.url  # Added product image URL

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def process_order(self, address):
        # Retrieve product details from the database based on cart items
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        # Your order processing logic here (e.g., creating an order in the database)

        # For demonstration purposes, let's print the order details
        print("Order Details:")
        for product in products:
            quantity = self.cart[str(product.id)]['quantity']
            print(f"{product.name} - Quantity: {quantity}")

        # Clear the cart after processing the order
        self.clear()

        # Return True if the order was successfully processed
        return True
