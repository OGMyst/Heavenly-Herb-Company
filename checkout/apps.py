from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Makes checkout available to other files
    under the name 'checkout'
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
