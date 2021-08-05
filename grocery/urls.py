from .views import GroceryDeleteView, GroceryDetailView,GroceryCreateView, GroceryListView, GroceryUpdateView
from django.urls import path

app_name = 'grocery'

urlpatterns = [
    path('',GroceryListView.as_view(),name='grocery-list'),
    path('grocery/<int:pk>/',GroceryDetailView.as_view(),name='grocery-detail'),
    path('grocery/add/',GroceryCreateView.as_view(),name='add-grocery'),
    path('grocery/update/<int:pk>/',GroceryUpdateView.as_view(),name='grocery-update'),
    path('grocery/delete/<int:pk>/',GroceryDeleteView.as_view(),name='grocery-delete'),
]
