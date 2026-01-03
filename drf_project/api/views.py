from django.shortcuts import render
from django.http import JsonResponse
from students.models import Students


def api_view(request):
    students = Students.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)