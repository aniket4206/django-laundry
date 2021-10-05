from django.urls import path,include
from shinelaundry import views


urlpatterns = [
  
    path('', views.index, name='shinelaundry'),
    path("contact/", views.contact, name="contact"),
    path('faq/', views.faq1, name="faq_page"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('vision/', views.vision, name="vision"),
    path('services/', views.services, name="services"),
    path('portfolio/', views.portfolio, name="gallery")


    # path("login/", views.login_request, name="login"),
    # path("logout/", views.logout_request, name= "logout"),
]
