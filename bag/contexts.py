from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings


def bag_contents(request):

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

    if total < settings.FREE_DELIVERY_THRESHOLD_UK:
        delivery = settings.STANDARD_DELIVERY_COST_UK
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD_UK - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        # 'free_delivery_delta': free_delivery_delta,
        # 'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context