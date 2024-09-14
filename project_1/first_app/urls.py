from django.urls import path
# from . import views
from . import views
urlpatterns = [

    path('courses/',views.courses),
    path("about/", views.about),
    path('',views.Home),
    
   
]   
