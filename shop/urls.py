from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='Aboutus'),
    path('contact/',views.contact,name='Contactus'),
    path('trackeer/',views.trackeer,name='TrackingStatus'),
    path('search/',views.search,name='Searching'),
    path('products/<int:myid>',views.products,name='ProductView'),
    path('checkout/',views.checkout,name='Checkout')
]