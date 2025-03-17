from django import forms
from .models import DataBlock

class CaseDataBlockForm(forms.ModelForm):
    class Meta:
        model = DataBlock
        fields = ['key', 'case', 'data_type', 'data']
