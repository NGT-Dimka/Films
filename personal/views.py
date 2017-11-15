from django.views.generic import DetailView
from films.models import Producer

# Create your views here.


class ProducerDetailView(DetailView):
    model = Producer
    template_name = 'producer_detail.html'

