from django.views import generic

from .models import Lens, Kit

class IndexView(generic.ListView):
    model = Kit
    template_name = 'kit_comparison/index.html'

class KitDetailView(generic.DetailView):
    model = Kit

    def get_context_data(self, **kwargs):
        _context = super().get_context_data(**kwargs)
        _context['total_weight'] = self.object.get_total_weight()
        _context['focal_range_plot'] = self.object.get_focal_range_plot()
        return _context

class LensDetailView(generic.DetailView):
    model = Lens
