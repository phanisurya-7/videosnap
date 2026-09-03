
from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products, name="products"),
    path("cart/", views.cart, name="cart"),
    path("order/", views.order, name="order"),
    path("checkout/", views.checkout, name="checkout"),
    path("chatbot/", views.chatbot, name="chatbot"),
]