from django.shortcuts import render

# Create your views here.
def rest(request):
    return render(request, 'rest/rest.html')