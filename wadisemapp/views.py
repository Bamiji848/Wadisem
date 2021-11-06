from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.conf import settings
from wadisem.settings import EMAIL_HOST_USER
from django.contrib import messages
from .forms import *
from django.http import Http404, HttpResponse, HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request, 'wadisemapp/index.html')


def about(request):
    return render(request, 'wadisemapp/about.html')


def education(request):
    return render(request, 'wadisemapp/education.html')


def finance(request):
    return render(request, 'wadisemapp/finance.html')


def business(request):
    return render(request, 'wadisemapp/business.html')


def blog(request):
    object_list = Blog.objects.all()
    paginator = Paginator(object_list, 6)  # 6 posts in each page
    page = request.GET.get('page')
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        blog = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        blog = paginator.page(paginator.num_pages)

    return render(request, 'wadisemapp/blog.html', {blog: 'blog'})


def blog_single(request, id):
    post = get_object_or_404(Blog, id=id)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'blog_key': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'wadisemapp/blog-single.html', context)


def contact(request, category_slug=None):
    contact = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_email = form.cleaned_data['email']
                sender_subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                email_msg = EmailMessage(subject=f"{sender_name}" 'from wadisem contact page' f"{sender_subject}", body=message, from_email='helpdesk@powercoolsystemsltd.com',
                                         to=['helpdesk@powercoolsystemsltd.com'], headers={'Reply-To': sender_email})
                email_msg.send()
                form = ContactForm()
    else:
        form = ContactForm()

    context = {
        form: 'form',
        contact: 'contact'
    }
    return render(request, 'wadisemapp/contact.html', context)
