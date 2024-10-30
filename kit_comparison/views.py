from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Lens, Kit

def index(request):
    context = {
        'kits': Kit.objects.all(),
        'lenses': Lens.objects.all(),
    }
    return render(request, 'kit_comparison/index.html', context)

def kit_detail(request, kit_id):
    kit = get_object_or_404(Kit, pk=kit_id)
    return render(request, 'kit_comparison/kit_detail.html', {'kit': kit})

def lenses(request):
    return HttpResponse("Hello, world. You're at the lenses list view.")

def lens_detail(request, lens_id):
    lens = get_object_or_404(Lens, pk=lens_id)
    return render(request, 'kit_comparison/lens_detail.html', {'lens': lens})
