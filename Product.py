class Product:
    currency = 'USD'
    products_created = 0
    
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity
        Product.products_created += 1

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError
        if len(value.strip()) == 0:
            raise ValueError
        self._title = value.strip().capitalize()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if not self.is_valid_price(value):
            raise ValueError
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self._quantity = value

    @property
    def total_cost(self):
        return self._price * self._quantity

    @property
    def in_stock(self):
        return self._quantity > 0

    def _check_n(self,n):
        if not isinstance(n, int):
            raise TypeError
        if n <= 0 or n > self.quantity:
            raise ValueError
        
    def sell(self, n):
        self._check_n(n)
        if n > self.quantity:
            raise ValueError
        self._quantity -= n

    def restock(self,n):
        self._check_n(n)
        self._quantity += n

    @classmethod
    def from_dict(cls, data):
        title = data['title']
        price = data['price']
        quantity = data['quantity']
        return cls(title, price, quantity)

    @classmethod
    def from_string(cls, s):
        title, price, quantity = s.split(';')
        return cls(title, float(price), int(quantity))

    @classmethod
    def free_sample(cls, title):
        return cls(title, price = 0.01, quantity = 1)

    @staticmethod
    def is_valid_price(value):
        if isinstance(value, (int,float)) and value > 0:
            return True
        return False

    @staticmethod
    def apply_discount(price, percent):
        if not isinstance(price, (int, float)) or not isinstance(percent,(int, float)):
            raise TypeError
        if not 0<=percent<=100:
            raise ValueError
        return price*(1-(percent/100))

    def __repr__(self):
        return f'Product(title={self._title!r}, price={self._price!r}, quantity={self._quantity!r})'






    
