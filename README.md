# Django-E-commerce-App

An advanced E-commerce web application built with Django. This application includes robust features such as user authentication, product listing, shopping cart, order management, and payment integration.

# Features
User Registration and Authentication

Comprehensive Product Management

Dynamic Shopping Cart

Order Management System

Payment Integration

# Installation
Prerequisites
Python 3.6+

Django 3+

Virtual Environment (recommended)

# Setup Instructions
Clone the Repository:

bash
git clone https://github.com/your_username/django-ecommerce-app.git
cd django-ecommerce-app
Create and Activate a Virtual Environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Required Packages:

bash
pip install -r requirements.txt
Run Migrations:

bash
python manage.py makemigrations
python manage.py migrate

# Project Structure

1. ecommerce_project/
Description: The main project directory containing settings and configuration files.

Key Files:

settings.py: Configuration settings for the Django project.

urls.py: URL routing configuration for the entire project.

2. accounts/
Description: Manages user authentication and registration.

Key Files:

models.py: Defines the CustomUser model, extending Django's AbstractUser.

forms.py: Contains the CustomUserCreationForm for user registration.

views.py: Handles views for user registration and login.

admin.py: Registers the CustomUser model with the admin site.

python
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
accounts/models.py
python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
accounts/forms.py
python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
3. products/
Description: Manages product listings and details.

Key Files:

models.py: Defines the Product model.

views.py: Handles views for listing and detailing products.

admin.py: Registers the Product model with the admin site.

python
from django.contrib import admin
from .models import Product

admin.site.register(Product)
products/models.py
python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
4. orders/
Description: Manages orders and shopping cart functionality.

Key Files:

models.py: Defines the Order and OrderItem models.

views.py: Handles views for managing the shopping cart and orders.

admin.py: Registers the Order and OrderItem models with the admin site.

python
from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
orders/models.py
python
from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
# Usage
User Registration
Navigate to /accounts/register/.

Complete the registration form and submit.

User Login
Navigate to /accounts/login/.

Enter your credentials and submit.

Product Listing
Navigate to /products/ to view all available products.

Click on a product to view its details.

Add to Cart
From the product detail page, click "Add to Cart".

View Cart
Navigate to /orders/view_cart/ to view items in your cart.

Checkout
Implement payment integration using a service like Stripe or PayPal.

Complete the checkout process.
