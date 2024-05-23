from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WhoWeAre
from .models import QuickFacts
from .models import ServiceIntro
from .models import About


def home(request):
    whoweare = WhoWeAre.objects.all()
    quickfacts = QuickFacts.objects.all()
    serviceintro = ServiceIntro.objects.all()
    return render(request, 'index.html', {'whoweare': whoweare, 'quickfacts': quickfacts, 'serviceintro': serviceintro})

def about(request):
    about = About.objects.all()
    quickfacts = QuickFacts.objects.all()
    serviceintro = ServiceIntro.objects.all()
    return render(request, 'about.html', {'about': about, 'quickfacts': quickfacts, 'serviceintro': serviceintro})

def services(request):
    return render(request, 'services.html', {})

def products(request):
    return render(request, 'products.html', {})

def contacts(request):
    return render(request, 'contacts.html', {})

def gratuip(request):
    return render(request, 'gratuip.html', {})