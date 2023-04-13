from django.urls import path
from . import views

urlpatterns = [
    path('api/items', views.ItemsList.as_view(), name='items_list'),
    path('api/items/<int:pk>', views.ItemsDetail.as_view(), name='items_detail'),
]