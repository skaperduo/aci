from django.shortcuts import render

# Create your views here.


def about_us(request):
    return render(request, 'about_us.html', {})


def aci_history(request):
    return render(request, 'aci_history.html', {})


def aci_vmgo(request):
    return render(request, 'aci_vmgo.html', {})


