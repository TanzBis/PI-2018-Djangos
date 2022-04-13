from django.contrib import admin
<<<<<<< HEAD

from profiles.models import Profile, Contacts, Photos

admin.site.register(Profile)
=======
from profiles.models.profiles import Profile, Contacts, Photos


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
>>>>>>> github/main


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    pass
