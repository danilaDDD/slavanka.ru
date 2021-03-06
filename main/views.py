from django.views.generic import TemplateView

from contacts.models import Office
from tours.models import ToursBanner, TourType, Tour
from events.models import Event
from base.views import SvkBaseView

# Create your views here.


class HomeView(SvkBaseView):
    template_name = 'index.html'
    title = 'Главная'

    def get_context_data(self, **kwards):
        context = super(HomeView, self).get_context_data(**kwards)

        context['baners'] = ToursBanner.get_hierarchy_all()
        context['tours'] = Tour.get_short_list()
        context['events'] = Event.get_short_list()

        return context
