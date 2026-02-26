from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# 1. Profile API (JSON Response)

def profile(request):
    data = {
        "name": "Doremon",
        "email": "dora@gmail.com",
        "membership": "Premium",
    }

    return JsonResponse(data)


# 2. Dashboard (HTML Response)

def dashboard(request):
    customer_dashboard = """
        <h1 style='color:violet; font-size:60px'>
            Welcome to Customer Dashboard...
        </h1>
    """

    return HttpResponse(customer_dashboard)