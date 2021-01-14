from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Product, Category
from .forms import ProductForm
# Create your views here.


def products(request):
    """ A view to return and filter products for the products page """
    all_products = Product.objects.all()
    categories = Category.objects.all()
    current_category = None
    sort = None
    direction = None
    page_number = 1
    start_point = 0
    end_point = start_point + 9

    if request.GET:
        if 'page' in request.GET:
            page_number = request.GET.get('page')
            start_point = (int(page_number) - 1)*9
            end_point = start_point + 9
            filtered_products = all_products
            split_filtered_products = all_products[start_point:end_point]

        if 'category' in request.GET:
            split_category = request.GET['category'].split(',')
            filtered_products = all_products.filter(category__name__in=split_category)
            split_filtered_products = all_products.filter(category__name__in=split_category)[start_point:end_point]
            current_category = Category.objects.get(name=request.GET['category'])

        if 'sort' in request.GET:
            sort = request.GET['sort']
            sort_list = sort.split('_')
            sortkey = sort_list[0]

            if sort_list[1] == 'desc':
                sortkey = f'-{sortkey}'

            filtered_products = all_products.order_by(sortkey)
            split_filtered_products = all_products.order_by(sortkey)[start_point:end_point]

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            filtered_products = all_products.filter(queries)
            split_filtered_products = all_products.filter(queries)[start_point:end_point]

    else:
        filtered_products = all_products
        split_filtered_products = all_products[start_point:end_point]

    paginator = Paginator(filtered_products, 9)
    page_obj = paginator.get_page(page_number)
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': split_filtered_products,
        'categories': categories,
        'current_category': current_category,
        'current_sorting': current_sorting,
        'page_obj': page_obj
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
