from django.forms import ModelForm
from django import forms
from .models import Person, Book


class PracticeForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birthdate']


class ForeignForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name']


class WidgetForm(forms.Form):
    eq_type = forms.ModelChoiceField(empty_label="select",
                                     widget=forms.Select, queryset=Person.objects.filter())
    name = forms.ModelChoiceField(empty_label="select",
                                  widget=forms.Select, queryset=Book.objects.all())

    def __init__(self, *args, **kwargs):
        y = kwargs.pop('person_obj')
        super(WidgetForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['name'].queryset = Book.objects.filter(author=y)
