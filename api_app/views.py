from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse



def getListOfTasks(request):
    
    response = JsonResponse(json)
    return response