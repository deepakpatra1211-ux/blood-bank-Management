from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import BloodRequestForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def stock(request):
    blood_stock = [
        {'group': 'A+', 'units': 12},
        {'group': 'A-', 'units': 5},
        {'group': 'B+', 'units': 9},
        {'group': 'B-', 'units': 3},
        {'group': 'AB+', 'units': 4},
        {'group': 'AB-', 'units': 2},
        {'group': 'O+', 'units': 15},
        {'group': 'O-', 'units': 6},
    ]
    return render(request, 'stock.html', {'blood_stock': blood_stock})


def apply(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your blood request has been saved. The blood bank team can review it.',
            )
            return redirect('apply')
    else:
        form = BloodRequestForm()

    return render(request, 'apply.html', {'form': form})


def location(request):
    return render(request, 'location.html')
