from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def fake(request, id):
    return render(request, "fake_detail.html", {"id": id})
