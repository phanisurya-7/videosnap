from products.chatbot import get_response
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from products.models import Product, Cart, Order


def products(request):
    products_list = Product.objects.all()
    return render(request, "products/products.html", {"products": products_list})

def cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product_obj = get_object_or_404(Product, id=product_id)
        Cart.objects.create(user=request.user, product=product_obj)
        return redirect("cart")
    
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, "products/cart.html", {"cart_items": cart_items})

def order(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "products/order.html", {"orders": orders})

def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        Order.objects.create(user=request.user, product=item.product)
    cart_items.delete()
    return render(request, "products/checkout.html")

def chatbot(request):

    response = ""

    if request.method == "POST":

        message = request.POST.get("message")

        response = get_response(message)

    return render(
        request,
        "products/chatbot.html",
        {
            "response": response
        }
    )