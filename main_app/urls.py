from django.urls import path
from . import views

# This HAS TO BE CALLED urlpatterns
# needs to be a list as well
# django wants it that way
urlpatterns = [
    # this path goes to localhost/ home path
    # inside of django leading / is not a thing at all 
    # never add leading /
    path('', views.index, name='index'),
    path('cats/', views.cat_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cat_show, name='cats_show'),
    path('cats/create/', views.CatCreate.as_view(), name='cat_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('user/<username>/', views.profile, name='profile')
]