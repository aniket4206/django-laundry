from django.contrib import admin
from django.urls import path,include
from shinelaundry import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('shinelaundry.urls')),
    path('', views.index, name='shinelaundry'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
]
