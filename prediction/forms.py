from django import forms
from django.forms import ModelForm
from .models import Insurance

class InsuranceForm(ModelForm):
    Gender = forms.ChoiceField(widget=forms.RadioSelect, choices=Insurance.GENDER)
    Age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Driving_License = forms.ChoiceField(widget=forms.RadioSelect, choices=Insurance.DRIVING_LICENSE)
    Region_Code = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Previously_Insured = forms.ChoiceField(widget=forms.RadioSelect, choices=Insurance.PREVIOUSLY_INSURED)
    Vehicle_Age = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=Insurance.VEHICLE_AGE)
    Vehicle_Damage = forms.ChoiceField(widget=forms.RadioSelect, choices=Insurance.VEHICLE_DAMAGE)
    Annual_Premium = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Policy_Sales_Channel = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Vintage = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Insurance
        fields = ['Gender','Age','Driving_License','Region_Code','Previously_Insured','Vehicle_Age','Vehicle_Damage','Annual_Premium','Policy_Sales_Channel','Vintage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Gender'].widget.attrs.update({'class': 'radio-margin'})
        self.fields['Driving_License'].widget.attrs.update({'class': 'radio-margin'})
        self.fields['Previously_Insured'].widget.attrs.update({'class': 'radio-margin'})
        self.fields['Vehicle_Damage'].widget.attrs.update({'class': 'radio-margin'})