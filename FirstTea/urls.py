"""
URL configuration for FirstTea project.

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
from users.views import login_up, registration, log_out
from catalog.views import home_page, product_detail, about
from states.views import state, state_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_up, name='login'),
    path('logout/', log_out, name='log_out'),
    path('', home_page, name='home'),
    path('register/', registration, name='register'),
    path('showcase/', product_detail, name='showcase'),
    path('about/', about, name='about'),
    path('states/', state, name='state'),
    path('states/<int:id>/', state_detail, name='state_detail'),
    path('cart_view/', include('cart.urls'), name="cart_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
