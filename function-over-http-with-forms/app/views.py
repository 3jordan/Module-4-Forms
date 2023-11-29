from django.shortcuts import render
from .forms import HeyForm, OldForm, OrderForm
from django.http import HttpResponse, HttpRequest


def HeyView(request: HttpRequest) -> HttpResponse:
    form = HeyForm()
    if request.GET:
        form = HeyForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data["name"]
            return render(request, "Hey.html", context={"form": form, "name": name})
    return render(request, "Hey.html", context={"form": form})


def OldView(request: HttpRequest) -> HttpResponse:
    form = OldForm()
    if request.GET:
        form = OldForm(request.GET)
        if form.is_valid():
            birthyear = form.cleaned_data["birthyear"]
            end_year = form.cleaned_data["end_year"]
            result = end_year - birthyear
            return render(
                request,
                "Old.html",
                context={
                    "form": form,
                    "birthyear": birthyear,
                    "end_year": end_year,
                    "result": result,
                },
            )
    return render(request, "Old.html", context={"form": form})


def OrderView(request: HttpRequest) -> HttpResponse:
    form = OrderForm()
    if request.GET:
        form = OrderForm(request.GET)
        if form.is_valid():
            # amount of items
            num_of_burgers = form.cleaned_data["num_of_burgers"]
            num_of_fries = form.cleaned_data["num_of_fries"]
            num_of_drinks = form.cleaned_data["num_of_drinks"]
            # amount of items times price
            burger_price = num_of_burgers * 4.5
            fries_price = num_of_fries * 1.5
            drinks_price = num_of_drinks * 1
            # total
            total = burger_price + fries_price + drinks_price
            return render(
                request,
                "Order.html",
                context={
                    "form": form,
                    "num_of_burgers": num_of_burgers,
                    "num_of_fries": num_of_fries,
                    "num_of_drinks": num_of_drinks,
                    "burger_price": burger_price,
                    "drinks_price": drinks_price,
                    "fries_price": fries_price,
                    "total": total,
                },
            )
    return render(request, "Order.html", context={"form": form})
