from abc import ABC, abstractmethod


class PaymentProvider(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def describe(self):
        return type(self).__name__


class CardProvider(PaymentProvider):
    def pay(self, amount):
        return f'Card: paid {amount}'

    def refund(self, amount):
        return f'Card: refunded {amount}'


class PaypalProvider(PaymentProvider):
    def pay(self, amount):
        return f'Paypal: paid {amount}'

    def refund(self, amount):
        return f'Paypal: refunded {amount}'


class BrokenProvider(PaymentProvider):
    def pay(self, amount):
        return f'BrokenProvider: paid {amount}'


def checkout(provider, amount):
    return provider.pay(amount)

card = CardProvider()
paypal = PaypalProvider()

print(card.describe())        # CardProvider
print(paypal.describe())      # PaypalProvider
print(checkout(card, 100))    # Card: paid 100
print(checkout(paypal, 50))   # Paypal: paid 50
print(card.refund(30))        # Card: refunded 30
print(paypal.refund(20))      # Paypal: refunded 20

PaymentProvider()             # TypeError
BrokenProvider()              # TypeError