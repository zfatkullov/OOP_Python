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

PROVIDERS = {'card': CardProvider, 'paypal': PaypalProvider}
def create_provider(kind: str) -> PaymentProvider:
    if kind not in PROVIDERS:
        raise ValueError(f'Unknown provider {kind}. Available: {", ".join(PROVIDERS.keys())}')
    return PROVIDERS[kind]()

print(isinstance(create_provider("card"), CardProvider))
create_provider("bitcoin")
print(checkout(create_provider("paypal"), 100))