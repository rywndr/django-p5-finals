from django.shortcuts import redirect, render

from .forms import BibForm
from .models import Bib


# Create your views here.
def bib(request):
    if request.method == "POST":
        form = BibForm(request.POST)
        if form.is_valid():
            bib = form.cleaned_data["bib"]
            Bib.objects.create(bib=bib)
            return redirect("success")

    else:
        form = BibForm()

    return render(request, "bib/bib.html", {"form": form})
