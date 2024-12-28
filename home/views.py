import mailtrap as mt
from decouple import config
from django.shortcuts import redirect, render

from .forms import RegistrationForm
from .models import Registration


def index(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            registration = Registration(
                nama=form.cleaned_data["nama"],
                email=form.cleaned_data["email"],
                jenis_kelamin=form.cleaned_data["jenis_kelamin"],
                tempat_lahir=form.cleaned_data["tempat_lahir"],
                birth_date=form.cleaned_data["birth_date"],
                phone=form.cleaned_data["phone"],
                alamat=form.cleaned_data["alamat"],
                kota=form.cleaned_data["kota"],
                provinsi=form.cleaned_data["provinsi"],
                warga_negara=form.cleaned_data["warga_negara"],
                golongan_darah=form.cleaned_data["golongan_darah"],
                jenis_id=form.cleaned_data["jenis_id"],
                nomor_id=form.cleaned_data["nomor_id"],
                id_upload=form.cleaned_data["id_upload"],
                kategori=form.cleaned_data["kategori"],
                emergency_contact=form.cleaned_data["emergency_contact"],
                emergency_phone=form.cleaned_data["emergency_phone"],
                memiliki_riwayat_penyakit_jantung=form.cleaned_data[
                    "memiliki_riwayat_penyakit_jantung"
                ],
                memiliki_riwayat_penyakit_hipertensi=form.cleaned_data[
                    "memiliki_riwayat_penyakit_hipertensi"
                ],
                memiliki_riwayat_penyakit_kronik_tahunan_lainnya=form.cleaned_data[
                    "memiliki_riwayat_penyakit_kronik_dan_atau_tahunan_lainnya"
                ],
                memiliki_riwayat_penyakit_epilepsi_dan_atau_gangguan_saraf_lainnya=form.cleaned_data[
                    "memiliki_riwayat_penyakit_epilepsi_dan_atau_gangguan_saraf_lainnya".replace(
                        " ", "_"
                    ).lower()
                ],
                memiliki_riwayat_penyakit_asma_saluran_pernafasan_lainnya=form.cleaned_data[
                    "memiliki_riwayat_penyakit_asma_atau_saluran_pernafasan_lainnya".replace(
                        " ", "_"
                    ).lower()
                ],
                memiliki_asuransi_bpjs_dan_atau_asuransi_lainnya=form.cleaned_data[
                    "memiliki_asuransi_bpjs_dan_atau_asuransi_lainnya".replace(
                        " ", "_"
                    ).lower()
                ],
                memiliki_riwayat_alergi_terhadap_obat_tertentu=form.cleaned_data[
                    "memiliki_riwayat_alergi_terhadap_obat_tertentu".replace(
                        " ", "_"
                    ).lower()
                ],
                allergies=form.cleaned_data["allergies"],
                bib_name=form.cleaned_data["bib_name"],
                ukuran_baju=form.cleaned_data["ukuran_baju"],
                payment_proof=form.cleaned_data["payment_proof"],
            )

            mail = mt.Mail(
                sender=mt.Address(
                    email="hello@demomailtrap.com",
                    name="Registration Form Submission for {}".format(
                        registration.nama
                    ),
                ),
                to=[mt.Address(email=registration.email)],
                subject="Polda Kepri Registration Form Submission",
                text="Thank you {} for submitting the registration form.",
                category="Registration Form Submission",
            )

            client = mt.MailtrapClient(token=config("MAILTRAP_API_TOKEN"))
            client.send(mail)

            registration.save()

            return redirect("success")
    else:
        form = RegistrationForm()

    return render(request, "home/index.html", {"form": form})


def success_page(request):
    return render(request, "home/success_page.html")
