from django.db import models


class PersonManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=first_name, last_name=last_name)


class Person(models.Model):
    # objects = PersonManager()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100)

    class Meta:
        unique_together = (('first_name', 'last_name'),)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    # objects = GraphManager()

    # def __str__(self):
    #     return self.name


class hurricane(models.Model):
    damages = models.CharField(max_length=150)
    rainfall = models.CharField(max_length=100)
    Description = models.TextField(max_length=None)
