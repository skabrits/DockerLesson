from django.shortcuts import render
import json
from django.http import HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    text = "Hello"
    return HttpResponse(json.dumps(text))

@csrf_exempt
def registr(request):
    result = {"status": 400}
    if request.method == "POST":
        parameters = request.POST
        login = parameters.get("login")
        password = parameters.get("password")
        print("login " + str(login) + " password " + str(password))
        result = {"ID": random.randint(100000000,1000000000), "status": 200}
    return HttpResponse(json.dumps(result))