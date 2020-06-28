from django import forms
from .models import Testee, Scoringsheet, Grade, Dojos, Events

#EVENTS_CHOICES = Events
# EVENTS_CHOICES = Events + [('','---------')]

#class EventSelectForm(forms.Form):
#    Event_name = forms.ChoiceField(label='Event', choices=EVENTS_CHOICES, required=False)
#
#    EventSelectFormSet = forms.formset_factory(EventSelectForm, extra=3)

class ScoringsheetForm(forms.ModelForm):
#    testee_name = forms.ModelChoiceField(
#        label = "受審者",
#        queryset = Testee.objects,
#        required = False
#    )
    class Meta:
        model = Scoringsheet
        fields = '__all__'
#        fields = [
#            "testee",
#            "score1",
#            "score2",
#            "score3",
#            "score4",
#            "score5",
#            "written_points"
#            ]

        field_order = ('scoringsheet_id')
