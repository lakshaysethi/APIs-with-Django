from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse



def getListOfTasks(request): #only handeling GET requests 
    json = {}# python
    json['task'] = 'make api'# python
    json['task2'] ='learn fetch ' # python
    #2 ask db for specific stuff 
    response = JsonResponse(json) # python to javascript because browser only speaks JS
    return response

    #1 POST request
# 1 seperate your backend and frontend - 
# 2 if backend stops for a while - we stil have front end working 
# 3 devide the backend  parts  - api 
