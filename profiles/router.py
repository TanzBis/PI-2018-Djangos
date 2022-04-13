<<<<<<< HEAD
from rest_framework import routers

from profiles.views import ProfilesViewSet, ProfileStatusViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfilesViewSet)
router.register(r'profile/status', ProfileStatusViewSet)
=======
from api.router import router
from profiles.viewsets.profile_viewset import ProfileViewSet

router.register(r'profile', ProfileViewSet)

>>>>>>> github/main
