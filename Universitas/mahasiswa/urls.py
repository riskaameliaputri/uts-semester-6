from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MahasiswaViewSet

router = DefaultRouter()
router.register(r'Mahasiswa', MahasiswaViewSet)

urlpatterns = router.urls
