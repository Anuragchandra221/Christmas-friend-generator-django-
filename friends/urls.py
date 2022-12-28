from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('random/', views.random),
    path('reset/', views.reset),
    path('search/<str:val>', views.search),
    path('count/', views.count),
    path('feedback/', views.feedback),
]