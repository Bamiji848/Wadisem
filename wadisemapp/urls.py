from django.conf.urls import url
from . import views
from django.urls import path, include


app_name = 'wadisemapp'

urlpatterns = [
    path('about',views.about, name="about"),
    path('services',views.services, name="services"),
    path('blog',views.blog, name="blog"),
    path('contact',views.contact, name="contact"),
]