from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import mail

# Create your views here.
def home(request):

    # mail.EmailMessage('subject', 'content', 'test@gmail.com', ['mic1028002@gmail.com']).send()

    print 1 + '1'  # will raise Exception

    return HttpResponse('<h1>Page was found</h1>')
