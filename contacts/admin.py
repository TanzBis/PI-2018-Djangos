from django.contrib import admin
from contacts.models import Contact
from contacts.models import Address


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class ContactAdmin(admin.ModelAdmin):
    pass
