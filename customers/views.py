from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {'customers': customers})

@login_required
def show(request, customers_id):
    customer = Customer.objects.get(id=customers_id)
    return render(request, 'customers/detail.html', {'customer': customer})

# @login_required
# def detail(request, customers_id):
#     customer = Customer.objects.filter(id=customers_id)
#     return render(request, 'customers/detail.html', {'customer': customer})

@login_required
def new(request):
    if request.POST:
        form = CustomerForm(request.POST)
        if form.is_valid():
            if form.save():
                print(form.cleaned_data)
                return redirect('/customers', messages.success(request, f'Customer was successfully created.', 'bg-success'))
            else:
                return redirect('/customers', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/customers', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = CustomerForm()
        return render(request, 'customers/new.html', {'form':form})

@login_required
def edit(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.POST:
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            if form.save():
                return redirect('/customers', messages.success(request, 'Customer was successfully updated.', 'bg-success'))
            else:
                return redirect('/customers', messages.error(request, 'Data is not saved', 'bg-danger'))
        else:
            return redirect('/customers', messages.error(request, 'Form is not valid', 'bg-danger'))
    else:
        form = CustomerForm(instance=customer)
        return render(request, 'customers/edit.html', {'form':form})

@login_required
def destroy(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer_name = customer.name
    customer.delete()
    return redirect('/customers', messages.success(request, f'Customer {customer_name} was successfully deleted.', 'bg-success'))
