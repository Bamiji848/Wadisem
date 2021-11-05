from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'wadisemapp/index.html')

def about(request):
    return render(request,'wadisemapp/about.html')

def services(request):
    return render(request,'wadisemapp/services.html')

def blog(request):
    return render(request,'wadisemapp/blog.html')

def contact(request):
    return render(request,'wadisemapp/contact.html')