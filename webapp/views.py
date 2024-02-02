from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import BrandForm




def home_page(request):
	return render(request,'pages/home.html' )


def dashboard_page(request):
	brands = Brand.objects.all()

	context = {
		'brands':brands,
	}
	return render(request,'pages/dash.html', context)


def about_page(request):
	return render(request,'pages/about.html')


def index(request):
	return render(request,'pages/index.html')


def navbar(request):
	return render(request,'pages/navbar.html')


def footer(request):
	return render(request,'pages/footer.html')


def brandform_Page(request):
    form = BrandForm()
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        'form': form
    }
    return render(request, 'pages/brand_form.html', context)

def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash')  
    else:
        form = BrandForm()
    return render(request, 'pages/add_brand.html', {'form': form})

def update_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brand added successfully.')  # Add success message
            return redirect('dash')  # Redirect to menu page after editing
    else:
        form = BrandForm(instance=brand)
    return render(request, 'pages/update_brand.html',{'form': form})

def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        brand.delete()
        return redirect('dash')  # Redirect to menu page after deletion

    else:
        form = BrandForm(instance=brand)
    return render(request, 'pages/delete_brand.html', {'form': form, 'brand':brand})

def login_page(request):
    return HttpResponse("This is Log-In")


