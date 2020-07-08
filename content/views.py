from django.contrib import admin
from django.shortcuts import render, redirect
from .forms import ModalEnquiry, PulllEnquiry
from .models import Enquiry
from django.contrib import messages


def panel(request):
    return redirect(admin.sites.urls)


def home(request):
    context = {
    }
    return render(request, 'home.html', context)


def products(request):
    return render(request, 'products.html')


def about(request):
    return render(request, 'about.html')


def order(request):
    context = {
    }
    return render(request, 'order.html', context)


def pull(request):
    context = {
        "form": PulllEnquiry

    }
    return render(request, 'enquiries.html', context)


def fetchEnquiry(request):
    form = PulllEnquiry(request.POST)
    enquiries = {'None': None}
    if form.is_valid():
        try:
            enquiries = Enquiry.objects.filter(id=form.cleaned_data['number'])
        except ValueError:
            enquiries = {'None': None}

    context = {
        'enquiries': enquiries
    }
    return render(request, 'results.html', context)


def help(request):
    context = {
        "form": ModalEnquiry
    }
    return render(request, 'help.html', context)


def addQuery(request):
    goto = 'home'
    form = ModalEnquiry(request.POST)

    if form.is_valid():
        enquiries = Enquiry.objects.filter(question=form.cleaned_data['question'])
        if not enquiries:
            form.save(Enquiry)
            messages.add_message(request, messages.SUCCESS, "Your enquiry has been submitted")
        else:
            goto = 'help'
            enquiry_id = enquiries[0].id
            messages.add_message(request, messages.INFO, f'Enquiry already exists, Check Enquiry ID : {enquiry_id}')
    else:
        goto = 'help'
        messages.add_message(request, messages.WARNING, "This is an alphanumeric field, please use alphanumeric "
                                                        "characters  ONLY i.e. [0-9, a-z, A-Z]")

    return redirect(goto)
