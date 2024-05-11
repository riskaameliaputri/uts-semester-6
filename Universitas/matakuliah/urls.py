from django.urls import path
from matakuliah import views

urlpatterns =[
    path('matakuliah/', views.Matakuliah_list),
]