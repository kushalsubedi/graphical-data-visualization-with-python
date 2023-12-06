from django import forms

from .models import DataFile, ManualDatas


class MaualDatasForm(forms.ModelForm):
    class Meta:
        model = ManualDatas
        fields = ['name', 'description', 'heading1', 'heading2', 'datafield']


class DataFileForm(forms.ModelForm):
    class Meta:
        model = DataFile
        fields = ['name', 'description', 'file']
