from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
	print(request,11111111)

	return HttpResponse('asd')
