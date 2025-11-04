from rest_framework import serializers
from . import models

class OutflowSerializer(serializers.ModelSerializer):


    class Meta:
     model = models.Outflows
     fields = '__all__'
