from django.contrib import admin
from userApp.models import *
# Register your models here.


admin.site.register(PersonProfile)
admin.site.register(EventProfile)
admin.site.register(Participation)
admin.site.register(GroupProfile)   
admin.site.register(RequestEvent)
admin.site.register(AcceptedEvent)   
admin.site.register(AcceptedGroup)   