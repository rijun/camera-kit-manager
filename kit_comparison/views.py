from django.shortcuts import render
from django.views import generic

from .models import Lens, Kit


def index(request):
    available_kits = Kit.objects.all()
    kit_list = [{
        'id': x.id,
        'lenses': "\n".join([str(e) for e in x.lenses.all()]),
        'focal_lengths': "\n".join([e.focal_length for e in x.lenses.all()]),
        'total_weight': x.get_total_weight()
    } for x in available_kits]

    context = {
        'kit_list': kit_list
    }
    return render(request, 'kit_comparison/index.html', context)


class KitCreateView(generic.edit.CreateView):
    model = Kit
    fields = ['lenses']


class KitUpdateView(generic.UpdateView):
    model = Kit
    fields = ['lenses']


class KitDetailView(generic.DetailView):
    model = Kit

    def get_context_data(self, **kwargs):
        _context = super().get_context_data(**kwargs)
        _context['total_weight'] = self.object.get_total_weight()
        return _context


class LensListView(generic.ListView):
    model = Lens


class LensDetailView(generic.DetailView):
    model = Lens
