from django import forms
from census.models import People

class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        ordering = ['id']
        fields = ['name', 'id_people', 'place', 'table', 'venc_id']
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'id_people': forms.TextInput(attrs={ 'class': 'form-control' }),
            'place': forms.TextInput(attrs={ 'class': 'form-control' }),
            'table': forms.TextInput(attrs={ 'class': 'form-control' }),
            'venc_id': forms.TextInput(attrs={ 'class': 'form-control' }),
      }