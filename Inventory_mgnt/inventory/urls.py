from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register-user/', views.register_user, name='register'),
    path('inventory/', views.inventory_view, name='inventory'),
    path('add-product/<int:pk>', views.add_product, name='add_product'),
    path('add-product/', views.add_product, name='add_product'),
    path('products/<int:pk>', views.products, name='products'),
    path('products/', views.products, name='products'),
    path('add-inventory/', views.add_inventory, name='add_inventory'),
    path('update-inventory/<int:pk>', views.update_inventory, name='update_inventory'),
    path('delete-inventory/<int:pk>', views.delete_inventory, name='delete_inventory'),
    path('delete-product/<int:pk>', views.delete_product, name='delete_product'),
    path('delete-product/', views.delete_product, name='delete_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()