from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django import forms
from django.shortcuts import render, redirect
from django.core import serializers
from django.views.generic import View
from django.http import HttpResponse
from doc_app.models import Book, Person
from.forms import PracticeForm, ForeignForm, WidgetForm


class ListCBV(View):
    def get(self, request, lool_id, *args, **kwargs):
        emp = Book.objects.all()
        emp_data = serializers.serialize('json', emp)
        return HttpResponse(emp_data, content_type='application/json')


# Create your views here.
# def practice(request):
#     if request.method == 'POST':
#         form1 = PracticeForm(request.POST)
#         form2 = ForeignForm(request.POST)
#         if form1.is_valid() and form2.is_valid():
#             z = form1.save()
#             u = Person.objects.filter(first_name=z.first_name).first()
#             y = form2.save(commit=False)
#             y.author = u
#             y.save()
#         return redirect('practice')
#     else:
#         form1 = PracticeForm()
#         form2 = ForeignForm()
#         return render(request, 'index.html', {'form1': form1, 'form2': form2})


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
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PersonSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PersonSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WidgetView(View):
    def get(self, request, *args, **kwargs):
        person_obj = Person.objects.filter().first()
        form = WidgetForm(person_obj=person_obj)
        alloc = []
        if request.GET.get('eq_type') and request.GET.get('name'):
            alloc = Book.objects.filter(author=request.GET.get('eq_type'))
        elif request.GET.get('eq_type'):
            alloc = Book.objects.filter(author=request.GET.get('eq_type'))
        # print(alloc)
        return render(request, 'user_list.html', {'form': form, 'alloc': alloc})
