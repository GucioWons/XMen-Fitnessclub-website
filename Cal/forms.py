from django import forms

from Cal.models import Class


class ClassForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    max = forms.IntegerField()
    date = forms.DateTimeField()

    class Meta:
        model = Class
        fields = ('title', 'description', 'max', 'date')