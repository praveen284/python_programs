class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_saved = price - deal_price # derived attribute
    
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal_Price: {}".format(self.deal_price))
        print("Ratings: {}".format(self.ratings))
        print("You_Saved: {}".format(self.you_saved))
        
    def get_deal_price(self):
        return self.deal_price

class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months
        
    def display_product_details(self):
        super().display_product_details()
        print("warranty_in_months: {} months".format(self.warranty_in_months))
       
class GroceryItem(Product):
    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date
        
    def display_product_details(self):
        super().display_product_details()
        print("expiry_date: {} ".format(self.expiry_date))
     
class Laptop(ElectronicItem):
    def __init__(self, name, price, deal_price, ratings, 
    warranty_in_months, ram, storage):
        super().__init__(name, price, deal_price, ratings, warranty_in_months)
        self.ram = ram
        self.storage = storage
    
    def display_product_details(self):
        super().display_product_details()
        print("Ram: {}".format(self.ram))
        print("Storage: {}".format(self.storage))
        

class Order():
    delivery_charges = {
        "Normal" : 0, 
        "Prime" : 100
    }
    def __init__(self, delivery_method, delivery_address):
        self.items_in_cart = []
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address
        
    def add_item(self, product, quantity):
        item = (product, quantity)
        self.items_in_cart.append(item)
        
    def display_order_details(self):
        print("Delivery Method: {}".format(self.delivery_method))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Products")
        print("...................................")
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print("")
        total_bill = self.get_total_bill()
        print("Total Bill: {}".format(total_bill))
        
    def get_total_bill(self):
        total_bill = 0
        for product,quantity in self.items_in_cart:
            total_bill += product.get_deal_price() *quantity
            
        order_delivery_charges = Order.delivery_charges[self.delivery_method]
        total_bill += order_delivery_charges
        return total_bill
    @classmethod
    def update_delivery_chares(cls, delivery_method , charges):
        cls.delivery_charges[delivery_method] = charges
        

            
            
tv = ElectronicItem("Tv",40000,25000,4.5,24)
tv.display_product_details()
print("\n")

milk = GroceryItem("milk", 40, 10, 4.5,"Jan 2022" )  
milk.display_product_details()
print("\n")

lenovo_lap = Laptop("Lenovo 123", 45000, 30000, 4.5, 24,"8GB","1TB")
lenovo_lap.display_product_details()
print("\n")

my_order = Order("Normal","Hydrabad")
my_order.add_item(tv,1)
my_order.add_item(milk,3)
my_order.add_item(lenovo_lap,1)
my_order.display_order_details()

Order.update_delivery_chares("Normal",50)
my_order.display_order_details()

