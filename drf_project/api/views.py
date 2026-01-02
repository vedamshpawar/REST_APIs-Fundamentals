from django.shortcuts import render
from django.http import JsonResponse


def api_view(request):
    students = {
        'name':'rathan reddy',
        'age' : 24,
        'location' : 'hyd'
    }
    return JsonResponse(students)