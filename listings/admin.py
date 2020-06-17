from django.contrib import admin
from .models import Listing

# Register your models here.

# define which field will show in your dash board
class ListingAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title') # if u click id/title you will get the information
    list_filter = ('realtor',) #must do .. will fyler by one name
    list_editable = ('is_published',) # for editing (only for boolean value)
    search_fields = ('title', 'price', 'list_date', 'realtor') # will appear a search key in top and serarch by these items
    list_per_page = 20 # per page 20 item will show
admin.site.register(Listing,ListingAdmin)
