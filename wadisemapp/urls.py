from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'wadisemapp'

urlpatterns = [
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('<int:id>/', views.blog_single, name='blog_single'),
    path('contact', views.contact, name="contact"),
    path('education', views.education, name="education"),
    path('finance', views.finance, name="finance"),
    path('business', views.business, name="business"),
]
