from django.shortcuts import render
from .forms import FrontTimesForm, NoTeensForm, XYZForm, CenteredAverageForm
from django.http import HttpResponse, HttpRequest


def FrontTimesView(request: HttpRequest) -> HttpResponse:
    form = FrontTimesForm()
    if request.GET:
        form = FrontTimesForm(request.GET)
        if form.is_valid():
            string = form.cleaned_data["string"]
            integer = form.cleaned_data["integer"]
            length = 3
            if length > len(string):
                length = len(string)
            front = string[:length]
            result = ""
            for i in range(integer):
                result = result + front
            return render(
                request,
                "FrontTimes.html",
                context={
                    "form": form,
                    "string": string,
                    "integer": integer,
                    "result": result,
                },
            )
    return render(request, "FrontTimes.html", context={"form": form})


def NoTeenView(request: HttpRequest) -> HttpResponse:
    form = NoTeensForm()

    if request.GET:
        form = NoTeensForm(request.GET)
        if form.is_valid():
            integer_1 = form.cleaned_data["integer_1"]
            integer_2 = form.cleaned_data["integer_2"]
            integer_3 = form.cleaned_data["integer_3"]

            def no_teen_sum(a, b, c):
                def fix_teen(n):
                    if 13 <= n <= 19 and n not in [15, 16]:
                        return 0
                    else:
                        return n

                result = fix_teen(a) + fix_teen(b) + fix_teen(c)
                return result

            total_sum = no_teen_sum(integer_1, integer_2, integer_3)

            return render(
                request,
                "NoTeens.html",
                context={
                    "form": form,
                    "integer_1": integer_1,
                    "integer_2": integer_2,
                    "integer_3": integer_3,
                    "total_sum": total_sum,
                },
            )

    return render(request, "NoTeen.html", context={"form": form})


def XYZThereView(request: HttpRequest) -> HttpResponse:
    form = XYZForm()

    if request.GET:
        form = XYZForm(request.GET)
        if form.is_valid():
            string = form.cleaned_data["string"]

            def xyz_there(string):
                result = False
                for i in range(len(string) - 2):
                    if string[i : i + 3] == "xyz" and (i == 0 or string[i - 1] != "."):
                        result = True
                return result

            result = xyz_there(string)

            return render(
                request,
                "XYZ.html",
                context={
                    "form": form,
                    "string": string,
                    "result": result,
                },
            )

    return render(request, "XYZ.html", context={"form": form})


def centered_average(nums_str: list) -> int:
    nums = [int(num) for num in nums_str.split(",")]
    nums.remove(min(nums))
    nums.remove(max(nums))

    average = sum(nums) // len(nums)
    return average


def CenteredAverageView(request: HttpRequest) -> HttpResponse:
    form = CenteredAverageForm()

    if request.GET:
        form = CenteredAverageForm(request.GET)
        if form.is_valid():
            nums = form.cleaned_data["nums"]

            result = centered_average(nums)

            return render(
                request,
                "centered_average.html",
                context={
                    "form": form,
                    "nums": nums,
                    "result": result,
                },
            )

    return render(request, "centered_average.html", context={"form": form})
