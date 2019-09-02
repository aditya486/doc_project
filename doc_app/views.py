from django.shortcuts import render
from django.core import serializers
from django.views.generic import View
from django.http import HttpResponse
from doc_app.models import Book


class ListCBV(View):
    def get(self, id, request, *args, **kwargs):
        emp = Book.objects.get(id=id)
        emp_data = serializers.serialize('json', emp, use_natural_keys=True)
        return HttpResponse(emp_data, content_type='application/json')


# Create your views here.
def practice(request):
    return render(request, 'index.html')


def pract(request):
    return render(request, 'index.html')


def practadi(request):
    return render(request, 'index.html')


def practaditya(request):
    return render(request, 'index.html')


def aditya(request):
    return render(request, 'index.html')
