from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
# pyrefly: ignore [missing-import]  
from django.contrib.auth.decorators import login_required
from products.models import Product, Cart, Order
from posts.models import Post

User = get_user_model()


# Create your views here.
#def accounts(request):
    #return render(request, "landingpages/linkedin.html")
def home(request):
    return render(request, "accounts/index.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect("signup")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        auth_login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("dashboard")

    return render(request, "accounts/signup.html")
        
def login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged in successfully.")

            next_url = request.GET.get("next")
            return redirect(next_url or "dashboard")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "accounts/login.html")
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")

@login_required
def dashboard(request):
    products_list = Product.objects.all()
    orders_list = Order.objects.filter(user=request.user)
    cart_items = Cart.objects.filter(user=request.user)
    posts_list = Post.objects.all()
    return render(request, "accounts/dashboard.html", {
        "products": products_list,
        "recent_products": products_list[:3],
        "total_products": products_list.count(),
        "orders": orders_list,
        "recent_orders": orders_list[:3],
        "orders_count": orders_list.count(),
        "cart_items": cart_items,
        "cart_count": cart_items.count(),
        "total_posts": posts_list.count(),
        "username": request.user.username,
    })


def add(request):
    if request.method == "POST":
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))
        c = a + b
        return render(request, "accounts/add.html", {"a":a,"b":b,"c": c}) 
    return render(request,"accounts/add.html")

def subtract(request):
    if request.method == "POST":
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))
        c   = a - b
        return render(request, "accounts/subtract.html", {"a":a,"b":b,"c": c}) 
    return render(request,"accounts/subtract.html")

def power(request):
    if request.method == "POST":
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))
        c   = a**b
        return render(request, "accounts/power.html", {"a":a,"b":b,"c": c}) 
    return render(request,"accounts/power.html")

def sqrt(request):
    if request.method == "POST":
        a = int(request.POST.get("a"))
        
        c   =float( a**0.5)
        return render(request, "accounts/sqrt.html", {"a":a,"c": c}) 
    return render(request,"accounts/sqrt.html")

def div(request):
    if request.method == "POST":
        a = int(request.POST.get("a"))
        b = int(request.POST.get("b"))
        c   = a//b
        return render(request, "accounts/div.html", {"a":a,"b":b,"c": c}) 
    return render(request,"accounts/div.html")


