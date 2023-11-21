from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='view_products'),
    path('add', views.create_product, name='create_product'),
    # Create a URL pattern that captures an integer parameter product_id from the URL
    path('update/<int:product_id>', views.update_product, name='update_product'),
    # Create a URL pattern that captures an integer parameter product_id from the URL
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),

]
