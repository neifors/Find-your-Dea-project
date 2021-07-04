from django.shortcuts import render
from django.http import HttpResponse
from .models import Dea as D
from .queries import *

def index(request):
    return render(request, "finder/index.html")

# def listado(request):
#     context = { "data": D.objects.all() }
#     return render(request, "finder/listado.html", context)

def nearest_dea(request):
    if request.method == "POST": 
        user_lat = request.POST["lat"]
        user_long = request.POST["long"]
        dea, dea_latlong, distance = dea_by_distance(D.objects.all(),user_lat , user_long)
        anchor_tag = f"https://www.google.com/maps/dir/{user_lat},+{user_long}/{dea_latlong[1]},{dea_latlong[0]}"
        context = {"dea": dea, "anchor_tag": anchor_tag, "distance": f'{distance:.2f}'}
        return render(request, "finder/nearest_dea.html", context)

def login(request):
    return render(request, "finder/login.html")

def suggestions(request):
    return render(request, "finder/suggestions.html")

def map(request):
    return render(request, "finder/maps.html")

def informationsent(request):
    return render(request, "finder/informationSent.html")