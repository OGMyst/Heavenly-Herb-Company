from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        Allows use of signals in checkout
        """
        import checkout.signals
