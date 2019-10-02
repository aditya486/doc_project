from django.db.models import F
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
from datetime import datetime
from.forms import WidgetForm


# class ListCBV(View):
#     def get(self, request, lool_id, *args, **kwargs):
#         emp = Book.objects.all()
#         emp_data = serializers.serialize('json', emp)
#         return HttpResponse(emp_data, content_type='application/json')
#
#
# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         person = Person.objects.all()
#         serializer = PersonSerializer(person, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Person.objects.get(pk=pk)
#     except Person.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = PersonSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = PersonSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
class WidgetView(View):
    def get(self, request, *args, **kwargs):
        person_obj = Person.objects.filter().first()
        form = WidgetForm(request.GET, person_obj=person_obj)
        alloc = []
        if request.GET.get('eq_type') and request.GET.get('name'):
            alloc = Book.objects.filter(author=request.GET.get('eq_type'))
        elif request.GET.get('eq_type'):
            alloc = Book.objects.filter(author=request.GET.get('eq_type'))
        return render(request, 'user_list.html', {'form': form, 'alloc': alloc})


# class TestF_String(View):
#     def get(self, request, *args, **kwargs):
#         a = datetime(2019, 9, 1, 6, 0, 0, 0)
#         a = datetime(2019, 9, 1, 12, 0, 0, 0)
#         person_obj = Person.objects.filter(end_time=F('start_time'))
#         for x in person_obj:
#             b = x.start_time
#             c = b.strftime("%Y-%m-%d %H:%M")
#             d = datetime.strptime(c, "%Y-%m-%d %H:%M")
#             # print(type(b.strftime("%Y-%m-%d %H:%M")))
#             # print(datetime.strptime(c, "%Y-%m-%d %H:%M"))
#             if a == d:
#                 print('Yes')
#             else:
#                 print('No')
