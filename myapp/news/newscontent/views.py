from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView

from .models import Newsimage, Newsinfo, Category

def home_view(request, newsinfo_id):
    return HttpResponse("You're looking at question %s." % newsinfo_id)
