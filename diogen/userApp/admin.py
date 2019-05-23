from django.contrib import admin
from userApp.models import *
# Register your models here.

#admin.site.register(Person, PersonModelAdmin)
admin.site.register(PersonProfile)

admin.site.register(EventProfile)
admin.site.register(Participation)
# admin.site.register(MusicianProfile)
# admin.site.register(CompanyProfile)