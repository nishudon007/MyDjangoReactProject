from django.db import models
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        # fields of the category that needs to be serialized
        fields = ('name', 'description')
