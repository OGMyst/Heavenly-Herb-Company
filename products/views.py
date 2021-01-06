from django.shortcuts import render, get_object_or_404


from .models import Product, Category
from .forms import ProductForm
# Create your views here.


def products(request):
    """ A view to return and filter products for the products page """

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


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
