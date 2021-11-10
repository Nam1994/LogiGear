class Product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "Name is %s, Price is %s" % (self.name, self.price)
