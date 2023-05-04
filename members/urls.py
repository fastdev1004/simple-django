from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('members/', views.all_members, name="all_members"),
    path('members/details/<slug:slug>', views.details, name='details')
]