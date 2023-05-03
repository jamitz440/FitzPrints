from django import forms
from .models import Product, Filament


class UploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UpdateForm(forms.ModelForm):
    filament_used = forms.ModelMultipleChoiceField(queryset=Filament.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    class Meta:
        model = Product
        fields = {'name', 'description', 'price', 'profit', 'weight', 'filament_used'}