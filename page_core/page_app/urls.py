from django.urls import path
from page_app import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
]