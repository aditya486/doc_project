from django.contrib import admin
from doc_app.models import Book, Person, PersonManager

# Register your models here.
admin.site.register(Book)
admin.site.register(Person)
# admin.site.register(PersonManager)
# admin.site.register(GraphManager)
