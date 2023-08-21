from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),

    path('menu-items/', views.MenuView.as_view(), name='menu'),
    path('menu-items/<int:pk>', views.MenuItemView.as_view(), name='menu-item'),
    
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('bookings/', include(router.urls)),
]