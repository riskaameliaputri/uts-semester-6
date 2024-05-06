from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MatakuliahViewSet

router = DefaultRouter()
router.register(r'matakuliah', MatakuliahViewSet)

urlpatterns = router.urls
