from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Supplier, Yard


@login_required(login_url='login')
def dashboard(request):
    total_supplier = Supplier.objects.count()
    total_yard = Yard.objects.count()
    context = {
        'Supplier': total_supplier,
        'Yard': total_yard,
    }
    return render(request, 'dashboard.html', context)
