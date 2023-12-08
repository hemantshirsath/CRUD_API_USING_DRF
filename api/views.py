from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def view_student(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            data={
                'msg':"Data saved successfully!"
            }
            return JsonResponse(data)
        return JsonResponse(serializer.errors)
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            data={'msg':'Data updated Successfully'}
            return JsonResponse(data)
        return JsonResponse(serializer.errors, safe=False)
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)


    