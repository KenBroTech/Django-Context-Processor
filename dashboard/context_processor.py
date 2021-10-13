from .models import Product


def product_context(request):
    food_total = Product.objects.filter(category='Food').count()
    stationary_total = Product.objects.filter(category='Stationary').count()
    electronics_total = Product.objects.filter(category='Electronics').count()
    context = {
        'food_total': food_total,
        'stationary_total': stationary_total,
        'electronics_total': electronics_total,
    }

    return context
