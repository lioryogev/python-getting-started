from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def signin(request):
	print("You've successfully signed in!")
	# return JsonResponse({'foo':'bar'})
	return render(request, 'signin.html', {'headers': request.META})

def signout(request):
	print("You've successfully signed out!")
	return render(request, 'signout.html', {'headers': request.META})

def verifyToken(request):
	print("headers:")
	print(request.META)
	return JsonResponse({}) #'headers': request.META})