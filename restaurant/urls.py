from django.urls import path
from . import views
"""
URL configuration for littlelemon project.

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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# from .views import UserViewSet

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'tables', views.BookingViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('admin/', admin.site.urls),
#     path('restaurant/menu/', include('restaurant.urls')),
#     path('restaurant/booking/', include(router.urls)),

# ]


urlpatterns = [
    path('index/', views.index, name='home'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingViewSet.as_view(['GET', 'POST'])),
    path('restaurant/booking/tables/',
         views.TableListView.as_view(), name='table-list'),
    path('api-token-auth/', obtain_auth_token)


]
