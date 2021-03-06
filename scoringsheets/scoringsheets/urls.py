"""scoringsheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

#country
from shinsa.views import CountryListView

#Dojos
from shinsa.views import DojosListView

# evemts --start--
from shinsa.views import EventsListView
from shinsa.views import EventsDetailView

# testee --start--
from shinsa.views import TesteeListView
from shinsa.views import TesteeCreateView
from shinsa.views import TesteeDetailView
from shinsa.views import TesteeUpdateView
##from shinsa.views import TesteeScoringsheetCreateFormsetView
#from shinsa.views import TesteeScoringsheetUpdateFormsetView

# scoringsheet
from shinsa import views
from shinsa.views import ScoringsheetListView
from shinsa.views import ScoringsheetCreateView
from shinsa.views import ScoringsheetDetailView
from shinsa.views import Scoringsheet5UpdateView
from shinsa.views import Scoringsheet4UpdateView
from shinsa.views import Scoringsheet3UpdateView

# embuscoringsheet
from shinsa import views
from shinsa.views import EmbuscoringsheetListView
from shinsa.views import EmbuscoringsheetCreateView
from shinsa.views import Embuscoringsheet5UpdateView
from shinsa.views import Embuscoringsheet4UpdateView
from shinsa.views import Embuscoringsheet3UpdateView


## from shinsa.views import ScoringsheetCreateFormsetView

urlpatterns = [
    path('', views.index, name="index.html"),
# weasyprint
    path('exportpdf/shinsa/', views.exportpdf_shinsa, name='exportpdf_shinsa'),

# Country
    path('country', CountryListView.as_view(), name="country"),

# Dojos
    path('dojos', DojosListView.as_view(), name="dojos"),

# Testee
    path('create_testee/<str:dojo_number>', TesteeCreateView.as_view(), name="create_testee"),
    path('testee', TesteeListView.as_view(), name="testee"),
    path('testee/<int:pk>', TesteeDetailView.as_view(), name="testee_detail"),
    path('testee_update/<int:pk>', TesteeUpdateView.as_view(), name="testee_update"),
#    path('<int:pk>/update', TesteeUpdateView.as_view(), name="scoringsheet_update"),
#    path('formset_testee', TesteeScoringsheetCreateFormsetView.as_view(), name="formset_testee"),
#    path('formset_testee', TesteeScoringsheetUpdateFormsetView.as_view(), name="formset_testee"),

# Events
    path('events', EventsListView.as_view(), name="events"),
    path('events/<int:pk>', EventsDetailView.as_view(), name="events_detail"),

# Scoringsheet
    path('scoringsheet', ScoringsheetListView.as_view(), name="scoringsheet"),
    path('create_scoringsheet', ScoringsheetCreateView.as_view(), name="create_scoringsheet"),
    path('scoringsheet_form', ScoringsheetCreateView.as_view(), name="scoringsheet_form"),
    path('scoringsheet_detail/<int:pk>', ScoringsheetDetailView.as_view(), name="scoringsheet_detail"),
#    path('scoringseet_update/<int:pk>', ScoringsheetUpdateView.as_view(), name="scoringsheet_update"),
    path('scoringseet5_update/<str:marker1>/<str:marker2>/<str:marker3>/<str:marker4>/<str:marker5>/<int:pk>', Scoringsheet5UpdateView.as_view(), name="scoringsheet5_update"),
    path('scoringseet4_update/<str:marker1>/<str:marker2>/<str:marker3>/<str:marker4>/<int:pk>', Scoringsheet4UpdateView.as_view(), name="scoringsheet4_update"),
    path('scoringseet3_update/<str:marker1>/<str:marker2>/<str:marker3>/<int:pk>', Scoringsheet3UpdateView.as_view(), name="scoringsheet3_update"),
#    path('form_scoringsheet', ScoringsheetCreateFormsetView.as_view(), name="form_scoringsheet"),

# Enmu Scoringsheet
    path('embuscoringsheet', EmbuscoringsheetListView.as_view(), name="embuscoringsheet"),
    path('embuscoringsheet_form', EmbuscoringsheetCreateView.as_view(), name="embuscoringsheet_form"),
    path('create_embuscoringsheet', EmbuscoringsheetCreateView.as_view(), name="create_embuscoringsheet"),
    path('embuscoringseet5_update/<str:marker1>/<str:marker2>/<str:marker3>/<str:marker4>/<str:marker5>/<int:pk>', Embuscoringsheet5UpdateView.as_view(), name="embuscoringsheet5_update"),
    path('embuscoringseet4_update/<str:marker1>/<str:marker2>/<str:marker3>/<str:marker4>/<int:pk>', Embuscoringsheet4UpdateView.as_view(), name="embuscoringsheet4_update"),
    path('embuscoringseet3_update/<str:marker1>/<str:marker2>/<str:marker3>/<int:pk>', Embuscoringsheet3UpdateView.as_view(), name="embuscoringsheet3_update"),
#    path('embuscoringseet_update/<int:pk>', EmbuscoringsheetUpdateView.as_view(), name="embuscoringsheet_update"),

# Admin
    path('admin/', admin.site.urls),

# login logout
    path('login', LoginView.as_view(template_name = 'login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name = 'logout.html'), name="logout"),
]
