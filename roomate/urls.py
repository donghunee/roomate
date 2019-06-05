"""roomate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from main import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('signup/',views.signup,name="signup"),
    path('',views.index,name="index"),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('activate/<uid64>&<token>',views.activate,name="activate"),
    path('first/',views.first,name="first"),
    path('two/',views.two,name="two"),
    path('three/',views.three,name="three"),
    path('four/',views.four,name="four"),

    path('fin/',views.fin,name="fin"),
    path('show_matching/',views.show_matching,name="show_matching"),
    path('email/',views.ema,name="email"),
]
