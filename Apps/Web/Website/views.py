from django.shortcuts import render


def home_page(request):
    context = {}
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {}
    return render(request, 'about_page.html', context)
