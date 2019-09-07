from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, redirect
from django.core import serializers
from django.views.generic import View
from django.http import HttpResponse
from doc_app.models import Book, Person
from.forms import PracticeForm, ForeignForm


class ListCBV(View):
    def get(self, request, lool_id, *args, **kwargs):
        emp = Book.objects.all()
        emp_data = serializers.serialize('json', emp)
        return HttpResponse(emp_data, content_type='application/json')


# Create your views here.
def practice(request):
    if request.method == 'POST':
        form1 = PracticeForm(request.POST)
        form2 = ForeignForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            z = form1.save()
            u = Person.objects.filter(first_name=z.first_name).first()
            y = form2.save(commit=False)
            y.author = u
            y.save()
        return redirect('practice')
    else:
        form1 = PracticeForm()
        form2 = ForeignForm()
        return render(request, 'index.html', {'form1': form1, 'form2': form2})


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
