from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Virus)
admin.site.register(Location)
admin.site.register(Case)
admin.site.register(Visit)