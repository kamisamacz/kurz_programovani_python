from django.shortcuts import render

def get_form(request):
    return render(request, "get_form.html")

def submit_form(request):
    data = request.GET.get("name", "unknown")
    print(f"Zadané meno data: {data}")
    return render(request, "submit_data.html", {"data": data})


def post_form(request):
    if request.method == "POST":
        data = request.POST["name"]
        print(f"Zadané meno: {data}")
        return render(request, "submit_data.html", {"data": data})

    return render(request, "post_form.html")
