from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Barataa, Qabxii, Hafittoo

@login_required
def dashboard(request):
    # Barataa maatii kanaan walqabatu qofa fida
    barattoota = Barataa.objects.filter(maqaa_maatii=request.user)
    
    context = {
        'barattoota': barattoota,
    }
    return render(request, 'hordoffii/dashboard.html', context)