from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from django.contrib import admin

<<<<<<< HEAD
from users.models import CustomUser

=======
>>>>>>> github/main

@admin.register(CustomUser)
class UsersAdmin(UserAdmin):
    pass
<<<<<<< HEAD
=======


>>>>>>> github/main
