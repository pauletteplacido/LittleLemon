from django.contrib import admin
from .models import MenuItem, Booking, SingleMenuItem

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Booking)
admin.site.register(SingleMenuItem)