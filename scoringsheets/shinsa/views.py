from django.shortcuts import render, redirect
#from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
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

from .models import Events, Grade, Testee, Scoringsheet, Dojos, Country, Status, Embuscoringsheet
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

class CountryListView(LoginRequiredMixin, ListView):
    model = Country
    login_url = '/login/'

class DojosListView(LoginRequiredMixin, ListView):
    model = Dojos
    login_url = '/login/'

    def get_queryset(self):
        countryparam = self.request.GET.get('country')
        object_list = Dojos.objects.filter(
                        Q(country__id=countryparam))
        return object_list

class EventsListView(LoginRequiredMixin, ListView):
    model = Events
    login_url = '/login/'

class EventsDetailView(LoginRequiredMixin, DetailView):
    model = Events
    login_url = '/login/'

class TesteeListView(LoginRequiredMixin, ListView):
    model = Testee

    def get_queryset(self):
        dojoparam = self.request.GET.get('dojo')
        object_list = Testee.objects.filter(
                        Q(dojo__id=dojoparam))
        return object_list

    login_url = '/login/'

class TesteeDetailView(DetailView):
    model = Testee

class TesteeUpdateView(LoginRequiredMixin, UpdateView):
    model = Testee
    fields = [
        "status",
        "dojo",
        "first_grade",
        "second_grade",
        "third_grade",
        "fourth_grade",
        "fifth_grade",
        "sixth_grade",
        "renshi",
        "seventh_grade",
        "kyoshi"
        ]
#    success_url = reverse_lazy("scoringsheet")
    def get_success_url(self):
        return "".join([reverse('testee'),'?', urlencode(dict(dojo=self.request.GET.get('dojo')))])

    login_url = '/login/'

class TesteeCreateView(LoginRequiredMixin, CreateView):
    model = Testee
    fields = [
        "membership_number",
        "testee_name",
        "testee_name_eng",
        "status",
        "dojo"
        ]
    def get_success_url(self):
        return "".join([reverse('testee'),'?', urlencode(dict(dojo=self.request.GET.get('dojo')))])

    login_url = '/login/'

    def get_initial(self):
        initial = super().get_initial()
        initial["dojo"] = self.request.GET.get('dojo')
        initial["membership_number"] = self.kwargs.get('dojo_number')
        return initial

#    def get_initial(self):
#        initialDojoNumber = super().get_initial()
#        initialDojoNumber["membership_number"] = self.kwargs.get('dojo_number')
#        return initialDojoNumber

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


class ScoringsheetCreateView(LoginRequiredMixin, CreateView):
    model = Scoringsheet
    template_name = 'shinsa/scoringsheet_form.html'
    fields = [
        "testee",
        "grade",
#        "score1",
#        "score2",
#        "score3",
#        "score4",
#        "score5",
#        "written_points",
        "events"
        ]
    success_url = reverse_lazy("scoringsheet_form")

    login_url = '/login/'

    def get_initial(self):
        initial = super().get_initial()
        initial["events"] = self.request.GET.get('event')
        return initial

class ScoringsheetDetailView(DetailView):
    model = Scoringsheet
    template_name = 'shinsa/scoringsheet_detail.html'

class Scoringsheet5UpdateView(LoginRequiredMixin, UpdateView):
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

    login_url = '/login/'

    def get_form(self):
        form = super(Scoringsheet5UpdateView, self).get_form()
        form.fields['score1'].label = self.kwargs.get('marker1')
        form.fields['score2'].label = self.kwargs.get('marker2')
        form.fields['score3'].label = self.kwargs.get('marker3')
        form.fields['score4'].label = self.kwargs.get('marker4')
        form.fields['score5'].label = self.kwargs.get('marker5')
        return form

class Scoringsheet4UpdateView(LoginRequiredMixin, UpdateView):
    model = Scoringsheet
    fields = [
        "score1",
        "score2",
        "score3",
        "score4",
        "written_points",
        ]
    def get_success_url(self):
        return "".join([reverse('scoringsheet'),'?', urlencode(dict(event=self.request.GET.get('event')))])

    login_url = '/login/'

    def get_form(self):
        form = super(Scoringsheet4UpdateView, self).get_form()
        form.fields['score1'].label = self.kwargs.get('marker1')
        form.fields['score2'].label = self.kwargs.get('marker2')
        form.fields['score3'].label = self.kwargs.get('marker3')
        form.fields['score4'].label = self.kwargs.get('marker4')
        return form

class Scoringsheet3UpdateView(LoginRequiredMixin, UpdateView):
    model = Scoringsheet
    fields = [
        "score1",
        "score2",
        "score3",
        "written_points",
        ]
    def get_success_url(self):
        return "".join([reverse('scoringsheet'),'?', urlencode(dict(event=self.request.GET.get('event')))])

    login_url = '/login/'

    def get_form(self):
        form = super(Scoringsheet3UpdateView, self).get_form()
        form.fields['score1'].label = self.kwargs.get('marker1')
        form.fields['score2'].label = self.kwargs.get('marker2')
        form.fields['score3'].label = self.kwargs.get('marker3')
        return form

class EmbuscoringsheetListView(ListView):
    model = Embuscoringsheet
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["judge"] = 0
#        return context

    def get_queryset(self):
        eventparam = self.request.GET.get('event')
        object_list = Embuscoringsheet.objects.filter(
                        Q(events__id=eventparam))
        return object_list

class EmbuscoringsheetCreateView(LoginRequiredMixin, CreateView):
    model = Embuscoringsheet
    template_name = 'shinsa/embuscoringsheet_form.html'
    fields = [
        "testee",
        "grade",
        "events"
        ]
    success_url = reverse_lazy("embuscoringsheet_form")

    login_url = '/login/'

    def get_initial(self):
        initial = super().get_initial()
        initial["events"] = self.request.GET.get('event')
        return initial

class Embuscoringsheet5UpdateView(LoginRequiredMixin, UpdateView):
    model = Embuscoringsheet
    fields = [
        "score1",
        "score2",
        "score3",
        "score4",
        "score5",
        ]
    def get_success_url(self):
        return "".join([reverse('embuscoringsheet'),'?', urlencode(dict(event=self.request.GET.get('event')))])

    login_url = '/login/'

    def get_form(self):
        form = super(Embuscoringsheet5UpdateView, self).get_form()
        form.fields['score1'].label = self.kwargs.get('marker1')
        form.fields['score2'].label = self.kwargs.get('marker2')
        form.fields['score3'].label = self.kwargs.get('marker3')
        form.fields['score4'].label = self.kwargs.get('marker4')
        form.fields['score5'].label = self.kwargs.get('marker5')
        return form

class Embuscoringsheet4UpdateView(LoginRequiredMixin, UpdateView):
    model = Embuscoringsheet
    fields = [
        "score1",
        "score2",
        "score3",
        "score4",
        ]
    def get_success_url(self):
        return "".join([reverse('embuscoringsheet'),'?', urlencode(dict(event=self.request.GET.get('event')))])

    login_url = '/login/'

    def get_form(self):
        form = super(Embuscoringsheet4UpdateView, self).get_form()
        form.fields['score1'].label = self.kwargs.get('marker1')
        form.fields['score2'].label = self.kwargs.get('marker2')
        form.fields['score3'].label = self.kwargs.get('marker3')
        form.fields['score4'].label = self.kwargs.get('marker4')
        return form

class Embuscoringsheet3UpdateView(LoginRequiredMixin, UpdateView):
    model = Embuscoringsheet
    fields = [
        "score1",
        "score2",
        "score3",
        ]
    def get_success_url(self):
        return "".join([reverse('embuscoringsheet'),'?', urlencode(dict(event=self.request.GET.get('event')))])

    login_url = '/login/'

    def get_form(self):
        form = super(Embuscoringsheet3UpdateView, self).get_form()
        form.fields['score1'].label = self.kwargs.get('marker1')
        form.fields['score2'].label = self.kwargs.get('marker2')
        form.fields['score3'].label = self.kwargs.get('marker3')
        return form
