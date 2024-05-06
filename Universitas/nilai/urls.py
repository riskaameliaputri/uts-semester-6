from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import NilaiViewSet

router = DefaultRouter()
router.register(r'nilai', NilaiViewSet)

urlpatterns = router.urls
