from django.contrib import admin
# from django.contrib.auth import get_user_model
from .models import MenuItem, Booking
# User = get_user_model()

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Booking)
# admin.site.register(CustomUserAdmin)
