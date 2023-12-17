from rest_framework import serializers
import database

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = database.Task
        fields = '__all__'