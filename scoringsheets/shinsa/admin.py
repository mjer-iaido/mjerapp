from django.contrib import admin
from shinsa.models import Events
from shinsa.models import Testee
from shinsa.models import Scoringsheet
from shinsa.models import Embuscoringsheet
from shinsa.models import Grade
from shinsa.models import Dojos
from shinsa.models import Country
from shinsa.models import Status

#from shinsa.models import Markers


# Register your models here.

admin.site.register(Events)
admin.site.register(Testee)
admin.site.register(Scoringsheet)
admin.site.register(Embuscoringsheet)
admin.site.register(Grade)
admin.site.register(Dojos)
admin.site.register(Country)
admin.site.register(Status)
#admin.site.register(Markers)
