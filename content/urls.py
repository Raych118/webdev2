from django.urls import path
from .views import home, products, order, help, addQuery, panel, fetchEnquiry, pull, about

urlpatterns = [
    path('admin/', panel, name='admin'),
    path('', home, name='home'),
    path('products', products, name='products'),
    path('order', order, name='order'),
    path('help', help, name='help'),
    path('addQuery', addQuery, name='query'),
    path('fetch', fetchEnquiry, name='fetch'),
    path('pull', pull, name='pull'),
    path('about', about, name='about'),
]

