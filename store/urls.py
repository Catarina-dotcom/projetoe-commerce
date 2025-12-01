from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('produto/<slug:slug>/', views.product_detail, name='product_detail'),
    path('carrinho/adicionar/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('carrinho/remover/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('carrinho/atualizar/<int:product_id>/', views.update_cart, name='update_cart'),
    path('informacoes/', views.informacoes, name='informacoes'),
    path('carrinho/', views.view_cart, name='view_cart'),
   
]