from django.urls import path
from .import views # importing all views from blog app

urlpatterns = [
    path('', views.post_list, name = 'post_list') # will change basic url view to a view called post_list
]

