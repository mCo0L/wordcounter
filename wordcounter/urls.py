from django.urls import path
from wordcounter import views

urlpatterns = [
    path('', views.home, name='home'),
    path('count/', views.count, name='count'),
    path('abount/', views.about, name='about')
]
