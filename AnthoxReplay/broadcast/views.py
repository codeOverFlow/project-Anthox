from django.http import HttpResponse

from .models import *

# Create your views here.

def cast(request):
    message = "Working fine dude."
    return HttpResponse(message)

def listing(request):

    ep = ["<li>{}</li>".format(ep) for ep in pascal.episodes]
    return HttpResponse(ep)