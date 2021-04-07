from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='shophome'),
    path('about',views.about,name='shopabout'),
    path('contact',views.contact,name='shopcontact'),
    path('products/<int:myid>',views.products,name='shopproducts')
]