from django.shortcuts import render


def index(request):
    """Render the FitHub homepage."""
    return render(request, 'home/index.html')