from django.shortcuts import render
from .utils import predict_price_function, get_locations


def estimate_price(request):
    locations = get_locations()

    if request.method == "POST":
        area = float(request.POST.get("area", 1000))
        bhk = int(request.POST.get("bhk", 1))
        bath = int(request.POST.get("bath", 1))
        location = request.POST.get("location", "")

        result = predict_price_function(location, area, bhk, bath)

        return render(request, "index.html", {"locations": locations, "result": result})

    return render(request, "index.html", {"locations": locations, "result": None})
