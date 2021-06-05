from django.urls import path,include
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('donate', views.donate, name='donate'),
   path('accounts/', include('allauth.urls')),
   path('logout/', views.logout, name='logout'),
   path('success', views.success, name='success'),
   path('transaction', views.transaction, name='transaction'),
]