from django.shortcuts import render
from .models import Package,Booking
from .forms import PackageForm, BookingForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def dashboard(request):
    return render(request, 'dashboard.html')

def add_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('packages_list')
    else:
        form = PackageForm()
    return render(request, 'add_package.html', {'form': form})

def packages_list(request):
    packages = Package.objects.all()
    return render(request, 'packages_list.html', {'packages': packages})

def edit_package(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('packages_list')
    else:
        form = PackageForm(instance=package)
    return render(request, 'edit_package.html', {'form': form, 'package': package})

def add_booking(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_info')
    else:
        form = BookingForm(initial={'package': package})
    return render(request, 'add_booking.html', {'form': form, 'package': package})

def booking_info(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_info.html', {'bookings': bookings})

def delete_package(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        package.delete()
        return redirect('packages_list')
    return render(request, 'delete_package.html', {'package': package})