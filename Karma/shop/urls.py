from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.login,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('update_order/',views.updateOrder,name="update_order"),
    path('cart',views.cart,name="cart"),
    path('home',views.home,name="home"),
    path('search',views.search,name="search"),
    path('checkout',views.checkout,name="checkout")
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)