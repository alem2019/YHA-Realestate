from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import min_price_choices, max_price_choices, bedroom_choices, boroughs_choices


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'min_price_choices': min_price_choices,
        'max_price_choices': max_price_choices,
        'bedroom_choices': bedroom_choices,
        'boroughs_choices': boroughs_choices

    }
    return render(request, 'core/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'core/about.html', context)
