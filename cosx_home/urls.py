
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name="cosx-home"),
    path('products/', views.products, name="cosx-products"),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('products/<int:pk>/', views.productdetails, name='productdetails'),
    path('cart/', views.cart, name="cart"),
    path('cart/<int:pk>/', views.cart_add, name="cart_add"),
    path('checkout_fromcart/', views.checkout_fromcart, name="checkout_fromcart"),
    path('checkout/<int:pk>', views.checkout, name="checkout"),
    path('wallet/', views.wallet, name="wallet"),
    path('success/', views.success, name="success"),
    path('orders/', views.orders, name="orders"),
    path('orders/<int:pk>', views.order_details, name="orders_details"),

]

urlpatterns += staticfiles_urlpatterns()