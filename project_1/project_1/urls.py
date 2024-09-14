from django.contrib import admin
from django.urls import path, include
# from . import views
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('',views.home),
    # path('contact/',views.contact)
    path('',views.Home),
    path("first_app/", include("first_app.urls")),
    path('contact/',views.contact)
   
   
]
