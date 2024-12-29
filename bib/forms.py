from django import forms
from django.core.validators import EmailValidator


class BibForm(forms.Form):
    bib = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Masukkan email yang telah terdaftar"}
        ),
        validators=[EmailValidator()],
    )
