from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    roll=serializers.IntegerField()
    city=serializers.CharField()

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
