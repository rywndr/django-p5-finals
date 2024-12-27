from django.shortcuts import render


# Create your views here.
def bib(request):
    return render(request, "bib/bib.html")
