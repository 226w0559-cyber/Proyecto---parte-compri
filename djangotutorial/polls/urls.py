from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vista1/", views.vista1, name="rafael_1"),
    path("vista2/", views.vista2, name="rafael_2"),
    path("vista3/", views.vista3, name="rafael_3"),
    path("vista4/", views.vista4, name="rafael_4"),
    path("vista5/", views.vista5, name="rafael_5"),
    path("vista6/", views.vista6, name="rafael_6"),
    path("vista7/", views.vista7, name="rafael_7"),
    path("vista8/", views.vista8, name="rafael_8"),
    path("vista9/", views.vista9, name="rafael_9"),
    path("vista10/", views.vista10, name="rafael_10"),
    
]