from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
from .models import Inventory, Product


def home(request):
    return render(request, 'home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('inventory')
        else:
            messages.success(request, "Invalid credentials. Try again.")
            return redirect('login')
    return render(request, 'login.html', {})



def logout_user(request):
    messages.success(request, "Logged out Successfully.")
    logout(request)
    return redirect('home')

#To register a new user.
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            
            messages.success(request, "You have Registered successfully. You can login now.")
            return redirect('login')
    else:
        form = RegisterUserForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


#To see the Inventories.
def inventory_view(request):
    inventories = Inventory.objects.all()
    if request.user.is_authenticated:
        return render(request, 'inventory.html', {'inventories':inventories})


#To add a new Inventory.
def add_inventory(request):
    if request.method == 'POST':
        data = request.POST

        inventory_name = data.get('inventory_name')
        inventory_type = data.get('inventory_type')
        inventory_description = data.get('inventory_desc')

        Inventory.objects.create(
            inventory_name = inventory_name,
            inventory_type = inventory_type,
            inventory_description = inventory_description,
        )
        messages.success(request, "Inventory added succesfully.")
        return redirect('inventory')

    return render(request, 'add_inventory.html', {})


#To Update the inventory details.
def update_inventory(request, pk): 
    if request.method == 'POST':    
        inventory = Inventory.objects.get(id=pk)
        inv_name = request.POST.get('inventory_name')
        inv_type = request.POST.get('inventory_type')
        inv_description = request.POST.get('inventory_desc')

        inventory.inventory_name = inv_name
        inventory.inventory_type = inv_type
        inventory.inventory_description = inv_description
        
        inventory.save()

        return redirect('inventory')
    else:
        inventory = Inventory.objects.get(id=pk)
        initial_data = {
            'inventory_name': inventory.inventory_name,
            'inventory_type': inventory.inventory_type,
            'inventory_description': inventory.inventory_description
            }    
        return render(request, 'update_inventory.html', {'initial_data':initial_data})
    
#To delete an Inventory
def delete_inventory(request, pk):
    inv_to_be_deleted = Inventory.objects.get(id=pk)
    inv_to_be_deleted.delete()
    messages.success(request, "Inventory deleted succesfully.")
    return redirect('inventory')
    

#For the products page.
def products(request, pk):
    if request.user.is_authenticated:
        inventory = Inventory.objects.get(id=pk)
        products = Product.objects.filter(inventory=inventory)
        return render(request, 'products.html', {'products':products})
    else:
        messages.success(request, "You must login to see products.")
        return redirect('products')

#To add products in an Inventory.
def add_product(request, pk=None):
    inventory = Inventory.objects.get(id=pk)

    if request.method == 'POST':
        data = request.POST

        inventory = inventory,
        product_name = data.get('product_name')
        product_description = data.get('product_description')
        products_in_inventory = data.get('product_in_inventory')
        product_image = request.FILES.get('product_image')

        Product.objects.create(
            inventory = inventory[0],
            product_name = product_name,
            product_description = product_description,
            num_in_inventory = products_in_inventory,
            product_image = product_image,
        )
        messages.success(request, "Product added succesfully.")
        new_link = f'/products/{pk}'
        return redirect(new_link)

    return render(request, 'add_product.html', {'inventory':'inventory'})

#To delete the products
def delete_product(request, pk=None):
    if request.user.is_authenticated:
        product_to_be_deleted = Product.objects.get(id=pk)
        ipk = product_to_be_deleted.inventory.id
        product_to_be_deleted.delete()
        messages.success(request, "Product has been deleted.")
        return redirect(f'http://127.0.0.1:8000/products/{ipk}', status=303)      #redirecting to the given link instead of the wrong path
        # return redirect(f'/products/{ipk}')
    else:
        messages.success(request, "You must login to delete records.")
        return redirect('products')