from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings


def bag_contents(request):
    """ Makes Bag data available across all files """
    bag_items = []
    total = 0
    product_count = 0
    delivery = 0
    sub_total = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        sub_total = quantity * product.price
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'sub_total': sub_total,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD_UK and total > 0:
        delivery = settings.STANDARD_DELIVERY_COST_UK
    else:
        delivery = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
