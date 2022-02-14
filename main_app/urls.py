from django.urls import path
from . import views

urlpatterns = [
    #we gon define all of our app-level urls
    #we needa add an import statement to link our files

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
]


