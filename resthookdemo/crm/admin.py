from django.contrib import admin

from resthookdemo.crm.models import Contact, Deal


class ContactAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Contact._meta.fields]
admin.site.register(Contact, ContactAdmin)

class DealAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Deal._meta.fields]
admin.site.register(Deal, DealAdmin)