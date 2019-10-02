from django.forms import ModelForm
from django import forms
from .models import Person, Book


# class PracticeForm(ModelForm):
#     class Meta:
#         model = Person
#         fields = ['first_name', 'last_name', 'birthdate']
#
#
# class ForeignForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name']

#


class WidgetForm(forms.Form):
    quantity = forms.IntegerField(min_value=0, max_value=9999)
    name = forms.ModelChoiceField(empty_label="select",
                                  widget=forms.Select, queryset=Book.objects.all())

    def __init__(self, *args, **kwargs):
        y = kwargs.pop('person_obj')
        super(WidgetForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['name'].queryset = Book.objects.filter(author=y)
        # self.fields['eq_type'].queryset = Person.objects.filter().first()
        self.fields['quantity'].required = False

    def clean(self):
        print(self.cleaned_data)
        # print(self.errors.pop('name'))
        print(self.non_field_errors())
