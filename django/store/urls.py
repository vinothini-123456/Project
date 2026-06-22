"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('productdetail/<int:id>',views.productdetail,name='productdetail'),
    path('products',views.product_items,name='products'),
    path('login',views.loginpage,name='login'),
    path('signup',views.signuppage,name='signup'),
    path('logout',views.logout_page,name='logout'),
    path('verify/<int:id>/',views.verify,name='verify'),
    path('buy/<int:id>/', views.buy_product, name='buy_product'),
    path('order-success/', views.order_success, name='order_success'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
