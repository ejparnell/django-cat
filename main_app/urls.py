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
    path('user/<username>/', views.profile, name='profile'),
    path('cattoys/', views.cattoys_index, name='cattoys_index'),
    path('cattoys/<int:cattoy_id>/', views.cattoy_show, name='cattoys_show'),
    path('cattoys/create/', views.CatToyCreate.as_view(), name='cattoys_create'),
    path('cattoys/<int:pk>/update/', views.CatToyUpdate.as_view(), name='cattoys_update'),
    path('cattoys/<int:pk>/delete/', views.CatToyDelete.as_view(), name='cattoys_delete'),
]