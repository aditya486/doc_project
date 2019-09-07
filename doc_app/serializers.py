from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    birthdate = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.save()
        return instance
