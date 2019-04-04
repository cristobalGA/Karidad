# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

# Create your views here.
class index_view(TemplateView):
    template_name = 'index.html'

)