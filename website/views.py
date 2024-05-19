from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WhoWeAre
from .models import QuickFacts
from .models import ServiceIntro


def home(request):
    whoweare = WhoWeAre.objects.all()
    quickfacts = QuickFacts.objects.all()
    serviceintro = ServiceIntro.objects.all()
    return render(request, 'index.html', {'whoweare': whoweare, 'quickfacts': quickfacts, 'serviceintro': serviceintro})