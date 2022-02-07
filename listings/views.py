from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from listings.choices import min_price_choices, max_price_choices, bedroom_choices, boroughs_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
        'title': 'Listings'
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__gte=bedrooms)

    # Min price
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        if min_price:
            price = min_price
            queryset_list = queryset_list.filter(price__gte=price)

      # Max price
    if 'max_price' in request.GET:
        max_price = request.GET['max_price']
        if max_price:
            price = max_price
            queryset_list = queryset_list.filter(price__lte=price)

        # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
     # borough
    if 'borough' in request.GET:
        borough = request.GET['borough']
        if borough:
            queryset_list = queryset_list.filter(borough__iexact=borough)

    context = {

        'min_price_choices': min_price_choices,
        'max_price_choices': max_price_choices,
        'bedroom_choices': bedroom_choices,
        'boroughs_choices': boroughs_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
