from django.urls import path
from . import views   #imports views.py

urlpatterns = [
  path("", views.home, name='home'),    #renders home.html
  path("about/", views.about, name='about'), 
  path("login/", views.login_view, name='login'), 
  path("library/", views.library, name='library'), 
  path("patient/", views.patient, name='patient'), 
  path("appointment/", views.appointment, name='appointment'), 
  path('api/book-appointment/', views.book_appointment, name='book_appointment'),
  
  
 
]