from django.shortcuts import render

# Create your views here.

def achievements(request):
    return render(request, "achievments/achievements.html")