<<<<<<< HEAD
from rest_framework import routers
from users.views import UserViewSet

router = routers.DefaultRouter()
=======
from api.router import router
from users.viewsets.user_viewset import UserViewSet

>>>>>>> github/main
router.register(r'users', UserViewSet)
