from django.shortcuts import render
from discount_module.models import Discount

# Create your views here.
def discount_component_view(request):
    discounts = Discount.objects.filter(is_active=True)


    context = {
        'discounts': discounts,
    }
    return render(request, 'discount_component.html', context)