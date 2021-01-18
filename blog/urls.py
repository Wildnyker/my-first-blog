from django.urls import path
from .import views # importing all views from blog app

urlpatterns = [
    path('', views.post_list, name = 'post_list'), # will change basic url view to a view called post_list
    path('post/<int:pk>', views.post_detail, name='post_detail'), # than add view
    path('post/new/', views.post_new, name = 'post_new'), # than add view
    path('post/<int:pk>/edit', views.post_edit, name = 'post_edit')
]

# post/ means that the URL should begin with the word post followed by a /. So far so good.
# <int:pk> – this part is trickier. It means that Django expects an integer value and will transfer it to a view as a variable called pk.
# / – then we need a / again before finishing the URL.

#after adding path you need to create view