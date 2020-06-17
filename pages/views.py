from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing # import listing db
from realtors.models import Realtor #import realtor db
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.

def index (request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] # only 3 post will show by date order and which is published/boolean is true
    context= {'listings': listings,
               'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices}
    return render ( request, 'pages/index.html', context) # index file is located in page directory

def about (request):
    realtors = Realtor.objects.order_by('-hire_date')
    #get MVP/ seller of the month
    mvp_realtors= Realtor.objects.all().filter(is_mvp=True)
    context = { 'realtors': realtors, 'mvp_realtors': mvp_realtors}
    return render ( request, 'pages/about.html', context)