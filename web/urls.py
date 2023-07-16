from django.urls import path

from .views import AboutUs
from .views import HomeView
from .views import ProductView
from .views import ContactPageView
from .views import ProductDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductView.as_view(), name='products'),
    path('about-us/', AboutUs.as_view(), name='about-us'),
    path('contact-us/', ContactPageView.as_view(), name='contact-us'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'), # noqa
]
