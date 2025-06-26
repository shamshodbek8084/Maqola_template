from django import forms
from .models import Maqola

class MaqolaForm(forms.ModelForm):
    class Meta:
        model = Maqola
        fields = [
            'talaba_fish', 'fakultet', 'fakultet_raqami', 'guruh_raqami',
            'number', 'title', 'format',
            'publication_type', 'journal_name', 'volume', 'issue',
            'published_date', 'pages',
            'bet_soni', 'mualliflar_soni', 'authors'
        ]
        widgets = {
            'published_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
