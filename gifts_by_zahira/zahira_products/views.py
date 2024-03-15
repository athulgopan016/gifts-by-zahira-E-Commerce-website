from django.shortcuts import render, redirect, get_object_or_404
from .models import  Product, Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .cart import Cart
from . import views 
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

@login_required
def home(request):
    return render(request,"index.html")





def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def customer_profile(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def loginview(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('zahira_products:home')  # Make sure the name 'home' matches your URL pattern
        else:
            return render(request, "Registration/login.html", {"msg": "Invalid login"})
    else:
        return render(request, "Registration/login.html")

def sign_up(request):
    try:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # Save the user if the form is valid
                form.save()
                return redirect('login')
            else:
                # Return the form with errors if it's not valid
                return render(request, 'signup.html', {'form': form, 'msg': 'Invalid signup'})
        else:
            # Render the form for GET requests
            form = UserCreationForm()
            return render(request, 'signup.html', {'form': form})
    except Exception as e:
        print(e)
        # Handle other exceptions if needed
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def add_to_cart(request, product_id):
    try:
        product_id = int(product_id)
    except ValueError:
        return HttpResponseBadRequest("Invalid product ID")

    print("Product ID:", product_id)
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product)
    return redirect('zahira_products:product_list')
# Assuming your CartItem model has a 'product' field
def view_cart(request):
    cart = Cart(request)
    cart_items = cart.cart.values()
    

    total_price = cart.get_total_price()
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total_price': total_price})

@csrf_protect
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
   
    cart = Cart(request)
    cart.remove(product)
    return redirect('zahira_products:view_cart')


def place_order(request):
    if request.method == 'POST':
        cart = Cart(request)
        address = request.POST.get('address', '')
        
        order_success = cart.process_order(address)

        if order_success:
            messages.success(request, 'Order placed successfully!')
            return redirect('zahira_products:product_list')
        else:
            messages.error(request, 'Failed to place the order. Please try again.')

        return render(request, 'customers.html')