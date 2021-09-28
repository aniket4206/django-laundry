from django.urls import path,include
from shinelaundry import views

urlpatterns = [
  
    path('', views.index, name='shinelaundry'),
    path('demo/', views.demo, name="demo"),
    path("contact/", views.contact, name="contact"),

    # path("login/", views.login_request, name="login"),
    # path("logout/", views.logout_request, name= "logout"),
]
