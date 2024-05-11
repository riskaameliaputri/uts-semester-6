from django.urls import path
from mahasiswa import views

urlpatterns =[
    path('mahasiswa/', views.Mahasiswa_list),
]