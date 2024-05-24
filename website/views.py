from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WhoWeAre
from .models import QuickFacts
from .models import ServiceIntro
from .models import About
from .models import Services
from .models import Logos
from .models import ProductsTopImage
from .models import KeyProducts


def home(request):
    logos = Logos.objects.all()
    whoweare = WhoWeAre.objects.all()
    quickfacts = QuickFacts.objects.all()
    serviceintro = ServiceIntro.objects.all()
    return render(request, 'index.html', {'whoweare': whoweare, 'quickfacts': quickfacts, 'serviceintro': serviceintro, 'logos':logos})

def about(request):
    about = About.objects.all()
    quickfacts = QuickFacts.objects.all()
    serviceintro = ServiceIntro.objects.all()
    return render(request, 'about.html', {'about': about, 'quickfacts': quickfacts, 'serviceintro': serviceintro})

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', {'services': services})

def services_detail(request,id):
    services = Services.objects.all()
    serves = get_object_or_404(Services,pk=id)
    return render(request, 'services_detail.html', {"serves" : serves, 'services': services})

def products(request):
    pro = ProductsTopImage.objects.all()
    products = KeyProducts.objects.all()
    return render(request, 'products.html', {"pro" : pro, 'products': products})

def contacts(request):
    return render(request, 'contacts.html', {})

def gratuip(request):
    return render(request, 'gratuip.html', {})

def product_image(request):
    pro = ProductsTopImage.objects.all()
    return render(request, 'products.html', {"pro" : pro})

