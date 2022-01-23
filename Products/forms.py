from django import forms

from Products.models import Pass, Training, Diet


class PassForm(forms.ModelForm):
    duration = forms.IntegerField()
    cost = forms.DecimalField()

    class Meta:
        model = Pass
        fields = ('duration', 'cost')

class TrainingForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    file = forms.FileField()
    cost = forms.DecimalField()

    class Meta:
        model = Training
        fields = ('title', 'description', 'file', 'cost')

class DietForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    file = forms.FileField()
    cost = forms.DecimalField()

    class Meta:
        model = Diet
        fields = ('title', 'description', 'file', 'cost')