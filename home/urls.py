"""
URL configuration for finalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.urls import path
# from.import views

# urlpatterns = [
#     path('', views.index,name="index"),
#     path('signup', views.signup,name="signup"), 
#     path('login', views.loginn,name="login"),
# ]

# from django.urls import path
# from .views import CustomLoginView
# from.import views

# app_name = 'accounts'

# urlpatterns = [

  
#     path('login/', CustomLoginView.as_view(), name='login'),
# ]

# app_name = 'finalproject'
# from django.urls import path
# from .views import login_view
# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('index/', login_view, name='index'),
#     path('login/', views.login_view, name='login'),
#     # Define other URL patterns as needed
# ]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.signin, name='signin'),
    path('index_view', views.index_view, name='index_view'),
    path('gallery_view/', views.gallery_view, name='gallery_view'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('success_view/', views.success_view, name='success_view'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:cart_item_id>/', views.update_quantity, name='update_quantity'),
    path('cart/', views.cart_view, name='cart_view'),
]