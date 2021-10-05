from django.shortcuts import render,redirect
from django.template.response  import TemplateResponse
from shinelaundry.models import slider,image,faq,services_info,index_image,personal_info,whychooseus,socialmediaaccount
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# obj = slider.objects.all()
# context = {
# 	'obj':obj
# }
# Create your views here.
def index(request):
	if request.method == "POST":
		to = request.POST.get('toemail')
		# content = request.POST.get('content')
		html_content = render_to_string("email_template.html")
		text_content = strip_tags(html_content)

		email = EmailMultiAlternatives(
			#subject
			"testing",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			#rec list
			[to]
		)
		email.attach_alternative(html_content,"text/html")
		email.send()



	obj1 = services_info.objects.all()
	obj = slider.objects.all()
	obj3 = index_image.objects.all()
	obj4 = personal_info.objects.all()
	obj5 = whychooseus.objects.all()
	obj6 = socialmediaaccount.objects.all()
	context = {
		'obj':obj,
		'obj1':obj1,
		'obj3':obj3,
		'obj4':obj4,
		'obj5':obj5,
		'obj6':obj6
	}
	return TemplateResponse (request, 'index.html', context)



def about(request):
	obj4 = personal_info.objects.all()
	obj6 = socialmediaaccount.objects.all()
	context = {
		'obj4':obj4,
		'obj6':obj6
	}
	return TemplateResponse (request, 'about.html',context)

def contact(request):
	obj4 = personal_info.objects.all()
	obj6 = socialmediaaccount.objects.all()
	context = {
		'obj4':obj4,
		'obj6':obj6
	}
	return TemplateResponse (request, 'contact.html', context)

def vision(request):
	obj4 = personal_info.objects.all()
	obj6 = socialmediaaccount.objects.all()
	context = {
		'obj4':obj4,
		'obj6':obj6
	}
	return TemplateResponse (request, 'vision.html', context)

def services(request):
	obj1 = services_info.objects.all()
	obj4 = personal_info.objects.all()
	obj6 = socialmediaaccount.objects.all()
	context1 = {
		'obj1':obj1,
		'obj4':obj4,
		'obj6':obj6
	}
	return TemplateResponse (request, 'services.html',context1)

def portfolio(request):
	obj2 = image.objects.all()
	obj4 = personal_info.objects.all()
	obj6 = socialmediaaccount.objects.all()
	context = {
		'obj2':obj2,
		'obj4':obj4,
		'obj6':obj6
	}
	return TemplateResponse (request, 'portfolio.html', context)

def faq1(request):
	obj = faq.objects.all()
	obj4 = personal_info.objects.all()
	obj6 = socialmediaaccount.objects.all()
	context = {
		'obj':obj,
		'obj4':obj4,
		'obj6':obj6
	}
	return TemplateResponse (request, 'faq.html', context)

# def sendanemail(request):
# 	if request.method == "POST":
# 		to = request.POST.get('toemail')
# 		# content = request.POST.get('content')
# 		html_content = render_to_string("email_template.html")
# 		text_content = strip_tags(html_content)

# 		email = EmailMultiAlternatives(
# 			#subject
# 			"testing",
# 			#content
# 			text_content,
# 			#from email
# 			settings.EMAIL_HOST_USER,
# 			#rec list
# 			[to]
# 		)
# 		email.attach_alternative(html_content,"text/html")
# 		email.send()
# 		return render(
# 			request,
# 			'index.html',
# 			{
# 				'title':'send an email'
# 			}
# 		)

