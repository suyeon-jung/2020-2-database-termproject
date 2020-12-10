from django.contrib import admin
from .models import *

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Olympic)
admin.site.register(Game)
admin.site.register(Athlete)
admin.site.register(Sport)
admin.site.register(Participate)

# Register your models here.
