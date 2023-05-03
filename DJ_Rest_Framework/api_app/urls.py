from django.urls import path
from . import views

urlpatterns = [
    # path para primer getProducts#
    path('products/',views.getProducts, name='products'),


]