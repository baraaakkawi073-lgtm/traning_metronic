from django.urls import path
from .views import index, products, books
from . import views

urlpatterns = [
    path("", index, name="index"),
    path("products/", products, name="products"),
    path("books/", books, name="books"),

    # ✅ مسارات CRUD للمنتجات
    path("products/create/", views.create_product, name="create_product"),
    path("products/<int:pk>/edit/", views.edit_product, name="edit_product"),
    path("products/<int:pk>/delete/", views.delete_product, name="delete_product"),
]

