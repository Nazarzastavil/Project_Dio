from django.contrib import admin
from userApp.models import Person
# Register your models here.
'''
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "updated", "timestamp"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post
 '''
#admin.site.register(Person, PersonModelAdmin)
admin.site.register(Person)