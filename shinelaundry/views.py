from django.shortcuts import render,redirect
from django.template.response  import TemplateResponse
from shinelaundry.models import slider


obj = slider.objects.all()
context = {
	'obj':obj
}

# Create your views here.
def index(request):
	return TemplateResponse (request, 'index.html', context)

def demo(request):
	return TemplateResponse (request, 'demo.html', context)

def contact(request):
	return TemplateResponse (request, 'contact.html', context)