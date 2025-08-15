from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def index(request):
    return render(request, "index.html")

def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def books(request):
    return render(request, "books.html")

# ✅ إنشاء منتج
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()
    return render(request, "products_form.html", {"form": form, "title": "Add Product"})

# ✅ تعديل منتج
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm(instance=product)
    return render(request, "products_form.html", {"form": form, "title": "Edit Product"})

# ✅ حذف منتج
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("products")
    return render(request, "products_confirm_delete.html", {"product": product})
