from django.urls import path, include
from . import views

urlpatterns = [
    #path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('signout/', views.signout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add, name='add'),
    path('subtract/', views.subtract, name='subtract'),
    path('power/', views.power, name='power'),
    path('sqrt/', views.sqrt, name='sqrt'),
    path('div/', views.div, name='div'),
]