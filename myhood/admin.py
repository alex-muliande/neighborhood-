from django.contrib import admin
from .models import Profile,Neighbourhood,Businesses,User

# Register your models here.
admin.site.register(Profile)
admin.site.register(Businesses)
admin.site.register(Neighbourhood)
