import imp
from numbers import Real
import re
from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import states_choices, price_choices, bedroom_choices
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'states_choices': states_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('name')
    mvp_realtors = Realtor.objects.order_by('name').filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
