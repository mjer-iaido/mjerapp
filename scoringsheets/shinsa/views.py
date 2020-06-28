from django.shortcuts import render, redirect
#from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views import generic
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.db.models import F
from django.db.models import Q

from .models import Events, Grade, Testee, Scoringsheet, Dojos, Country
from .forms import ScoringsheetForm

#weasyprint --start--
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile

# Create your views here.

def index(request):
    return render(request, 'shinsa/index.html', {})

#weasyprint --start--
def exportpdf_shinsa(request):
    from django.template.loader import get_template
    html_template = get_template('shinsa/scoringsheet_list.html')
    html_str = html_template.render({
#                    'Scoringsheet': Scoringsheet,
                },request)  # ここでrequestを渡してあげないと、Template側で必要な変数やプリセットなどが取得できずエラーになる場合がある

    pdf_file = HTML(request.GET.get('path')).write_pdf(
        stylesheets=[
            CSS(string='body { font-family: serif !important }'),
        ],
    )
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="shinsa_scoringsheet.pdf"'
    return response
#weasyprint --end--
class CountryListView(ListView):
    model = Country

class DojosListView(ListView):
    model = Dojos

    def get_queryset(self):
        countryparam = self.request.GET.get('country')
        object_list = Dojos.objects.filter(
                        Q(country__id=countryparam))
        return object_list

class EventsListView(ListView):
    model = Events

class EventsDetailView(DetailView):
    model = Events

class TesteeListView(ListView):
    model = Testee

    def get_queryset(self):
        dojoparam = self.request.GET.get('dojo')
        object_list = Testee.objects.filter(
                        Q(dojo__id=dojoparam))
        return object_list

class TesteeDetailView(DetailView):
    model = Testee

class TesteeUpdateView(UpdateView):
    model = Testee
    fields = [
        "grade",
        "dojo"
        ]
    success_url = reverse_lazy("scoringsheet")

class TesteeCreateView(CreateView):
    model = Testee
    fields = [
        "testee_name",
        "grade",
        "dojo"
        ]
    def get_success_url(self):
        return "".join([reverse('testee'),'?', urlencode(dict(dojo=self.request.GET.get('dojo')))])

class ScoringsheetListView(ListView):
    model = Scoringsheet
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["judge"] = 0
#        return context

    def get_queryset(self):
        eventparam = self.request.GET.get('event')
        object_list = Scoringsheet.objects.filter(
                        Q(events__id=eventparam))
        return object_list


class ScoringsheetCreateView(CreateView):
    model = Scoringsheet
    template_name = 'shinsa/scoringsheet_form.html'
    fields = [
        "testee",
        "score1",
        "score2",
        "score3",
        "score4",
        "score5",
        "written_points",
        "events"
        ]
    success_url = reverse_lazy("scoringsheet_form")

class ScoringsheetDetailView(DetailView):
    model = Scoringsheet
    template_name = 'shinsa/scoringsheet_detail.html'

class ScoringsheetUpdateView(UpdateView):
    model = Scoringsheet
    fields = [
        "score1",
        "score2",
        "score3",
        "score4",
        "score5",
        "written_points",
        ]
    def get_success_url(self):
        return "".join([reverse('scoringsheet'),'?', urlencode(dict(event=self.request.GET.get('event')))])
