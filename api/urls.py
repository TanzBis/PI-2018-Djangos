from django.contrib import admin
from django.urls import path, include

<<<<<<< HEAD
from follows.router import router as follows_router
from users.router import router as users_router
from profiles.router import router as profiles_router
=======
from addresses.router import router as address
from profiles.viewsets.profile_viewset import ProfileViewSet
from users.router import router as user
from follows.router import router as follows
from profiles.router import router as profiles

>>>>>>> github/main
urlpatterns = [
    path('', include(address.urls)),
    path('', include(user.urls)),
    path('', include(follows.urls)),
    path('', include(profiles.urls)),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
<<<<<<< HEAD
    path('', include(users_router.urls)),
    path('', include(follows_router.urls)),
    path('', include(profiles_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
=======
>>>>>>> github/main
]
