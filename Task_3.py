from pprint import pprint
#Product Store

#Write a class Product that has three attributes:

#type
#name
#price
#Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

#Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

#Also, the ProductStore class must have the following methods:

#add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
#set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
#sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
#get_income() - returns amount of many earned by ProductStore instance.
#get_all_products() - returns information about all available products in the store.
#get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:
    def __init__(self, product_type, name, price):
        self.product_type = product_type
        self.name = name
        self.price = price

class ProductStore(Product):
    def __init__(self):
        self.products = {}
        self.income = 0
    def add(self, product, amount):
        final_price = product.price * 1.3
        if amount <= 0:
            raise ValueError("Amount <= 0")

        if product.name in self.products:
            self.products[product.name]['amount'] += amount

        else:
            self.products[product.name] = {
                'product': product,
                'amount': amount,
                'price': final_price,
                'discount': 0
            }
    def set_discount(self, identifier, percent, identifier_type = 'name'):
        if not (0 <= percent <= 100):
            raise ValueError("Discount percent must be between 0 and 100.")
        product_found = False
        for product_name, product_info in self.products.items():
            product = product_info['product']
            if identifier_type == 'name' and product_name == identifier:
                product_info['discount'] = percent
                product_info['price'] = product_info['price'] * (1 - percent / 100)
                product_found = True

            elif identifier_type == 'type' and product.product_name == identifier:
                product_info['discount'] = percent
                product_info['price'] = product_info['price'] * (1 - percent / 100)
                product_found = True
        if not product_found:
            raise ValueError("Product not found")
            
    def sell_product(self, product_name, amount):
        if product_name in self.products:
            if self.products[product_name]['amount'] >= amount:
                self.products[product_name]['amount'] -= amount
                self.income += self.products[product_name]['price'] * amount
            else:
                raise ValueError("Not enough product in shop")
        else:
            raise ValueError("Not found product in shop")


    def get_income(self):
        print (f'All income = {self.income}')

    def get_all_products(self):
        for k, v in self.products.items():
            print(f"Product {k}  amount = {self.products[k]['amount']}, price is {self.products[k]['price']:.2f}, and Discount: {v['discount']}%")

    def get_product_info(self, product_name):
        tuple_list = ()
        if product_name in self.products:
            tuple_list = (product_name, self.products[product_name]['amount'])
        else:
            raise ValueError ("Product not found")
        return tuple_list
        



p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)
s.get_all_products()

assert s.get_product_info('Ramen') == ('Ramen', 290)

s.add(p2, 300)
assert s.get_product_info('Ramen') == ('Ramen', 590)