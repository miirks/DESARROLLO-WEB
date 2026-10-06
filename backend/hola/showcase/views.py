from django.shortcuts import render


def index(request):
    """Render the showcase page."""
    return render(request, 'showcase/index.html')