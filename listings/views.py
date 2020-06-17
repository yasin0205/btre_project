from django.shortcuts import render , get_object_or_404
from .models import Listing #calling database
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.

def index (request):
    listings = Listing.objects.order_by('-list_date') # will show the post serially by date
    #pagination
    paginator = Paginator(listings,3)
    page = request.GET.get('page') # page in bracket will use in templates as '?page'
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context )

def listing (request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id) # will fetch from Listing bd ...if key is not exists 404 error will show
    context = {'listing': listing}
    return render(request, 'listings/listing.html',context)

def search (request):
    context = {'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices}
    return render(request, 'listings/search.html', context)