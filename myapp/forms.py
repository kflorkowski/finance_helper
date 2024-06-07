from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    birth_date = forms.DateField(input_formats=['%d/%m/%Y', '%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'gender', 'birth_date']

    def save(self, user=None, commit=True):
        person = super().save(commit=False)
        if user:
            person.user = user
        if commit:
            person.save()
        return person
