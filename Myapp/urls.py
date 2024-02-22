from django.urls import path
from Myapp import views

urlpatterns = [

    path('welcome/', views.karibu),
    path('', views.home, name='my_home'),
    path('services/', views.services, name='our_services'),
    path('aboutus/', views.aboutus, name='my_aboutus'),
    path('gallery/', views.gallery, name='my_gallery'),
    path('contactus/', views.contactus, name='my_contactus')


]


