from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Event

# Create your views here.


class HomepageView(generic.ListView):
  model = Event
  template_name = "rbs_site/main.html"