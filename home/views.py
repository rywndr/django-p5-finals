from django.shortcuts import redirect, render

from .forms import RegistrationForm


def index(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("success_page_todo")
    else:
        form = RegistrationForm()

    return render(request, "home/index.html", {"form": form})
