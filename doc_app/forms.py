from django.forms import ModelForm
from .models import Person, Book


class PracticeForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birthdate']


class ForeignForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name']
