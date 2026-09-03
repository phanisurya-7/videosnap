from django.shortcuts import render

# Create your views here.
def linkedin(request):
    return render(request, "landingpages/linkedin.html")