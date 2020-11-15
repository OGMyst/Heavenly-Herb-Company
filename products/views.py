from django.shortcuts import render
from django.db.models.functions import Lower


from .models import Product, Category
# Create your views here.


def products(request):
    """ A view to return the index page """

    products = Product.objects.all()
    categories = Category.objects.all()
    current_category = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            split_category = request.GET['category'].split(',')
            products = products.filter(category__name__in=split_category)
            current_category = Category.objects.filter(name__in=split_category)

        if 'sort' in request.GET:
            sort = request.GET['sort']
            sort_list = sort.split('_')
            sortkey = sort_list[0]

            if sort_list[1] == 'desc':
                sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category,
        'current_sorting': current_sorting,
        }

    return render(request, 'products/products.html', context)
