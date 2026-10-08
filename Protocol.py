from typing import Protocol


class Payable(Protocol):
    def pay(self, amount):
        ...


class CryptoProvider:
    def pay(self, amount):
        return f'Crypto: paid {amount}'


def checkout_proto(p: Payable, amount):
    return p.pay(amount)

crypto = CryptoProvider()
print(checkout_proto(crypto, 7))     # Crypto: paid 7
print(checkout_proto(5, 100))        # AttributeError