from django.urls import path
from nilai import views

urlpatterns = [
    path('nilai/', views.Nilai_list),
]