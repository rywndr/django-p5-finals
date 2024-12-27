from django import forms
from django.core.validators import RegexValidator


class RegistrationForm(forms.Form):
    nama = forms.CharField(
        label="Nama",
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Masukkan nama Anda"}),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"placeholder": "Masukkan email Anda"}),
    )
    jenis_kelamin = forms.ChoiceField(
        label="Jenis Kelamin",
        choices=[("Laki-laki", "Laki-laki"), ("Perempuan", "Perempuan")],
    )
    tempat_lahir = forms.CharField(
        label="Tempat Lahir",
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Masukkan tempat lahir Anda"}),
    )
    birth_date = forms.DateField(
        label="Birth Date",
        widget=forms.DateInput(
            attrs={
                "type": "date",
            }
        ),
    )
    phone = forms.CharField(
        label="Nomor Handphone",
        max_length=20,
        validators=[
            RegexValidator(regex=r"^\d{10,12}$", message="Invalid phone number")
        ],
        widget=forms.TextInput(attrs={"placeholder": "Masukkan nomor handphone Anda"}),
    )
    alamat = forms.CharField(
        label="Alamat",
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Masukkan alamat Anda"}),
    )
    kota = forms.CharField(
        label="Kota",
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Masukkan kota Anda"}),
    )
    provinsi = forms.CharField(
        label="Provinsi",
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Masukkan provinsi Anda"}),
    )
    warga_negara = forms.ChoiceField(
        label="Warga Negara",
        choices=[
            ("Indonesia", "Indonesia"),
            ("Singapore", "Singapore"),
            ("Malaysia", "Malaysia"),
            ("Lainnya", "Lainnya"),
        ],
    )
    golongan_darah = forms.ChoiceField(
        label="Golongan Darah",
        choices=[("A", "A"), ("B", "B"), ("AB", "AB"), ("O", "O")],
    )
    jenis_id = forms.ChoiceField(
        label="Jenis ID",
        choices=[
            ("KTP", "KTP"),
            ("Kartu Pelajar", "Kartu Pelajar"),
            ("SIM", "SIM"),
            ("Passport", "Passport"),
        ],
    )
    nomor_id = forms.CharField(
        label="Nomor ID",
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Masukkan nomor ID Anda"}),
    )
    id_upload = forms.FileField(label="Upload KTP/ID Anda")

    kategori = forms.ChoiceField(
        label="Kategori",
        choices=[
            ("Umum", "Umum (dibawah 45 tahun)"),
            ("Master", "Master (45 tahun ke atas)"),
        ],
    )

    emergency_contact = forms.CharField(
        label="Nama Kontak Darurat",
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Masukkan nama kontak darurat Anda"}
        ),
    )
    emergency_phone = forms.CharField(
        label="Nomor Telepon Kontak Darurat",
        max_length=20,
        validators=[
            RegexValidator(regex=r"^\d{10,12}$", message="Invalid phone number")
        ],
        widget=forms.TextInput(
            attrs={"placeholder": "Masukkan nomor telepon kontak darurat Anda"}
        ),
    )

    medical_conditions = [
        ("Memiliki Riwayat Penyakit Jantung", "Memiliki Riwayat Penyakit Jantung"),
        (
            "Memiliki Riwayat Penyakit Hipertensi",
            "Memiliki Riwayat Penyakit Hipertensi",
        ),
        (
            "Memiliki Riwayat Penyakit Kronik/Tahunan Lainnya (Diabetes Melitus, Ginjal, Hepatitis, dll)",
            "Memiliki Riwayat Penyakit Kronik/Tahunan Lainnya (Diabetes Melitus, Ginjal, Hepatitis, dll)",
        ),
        (
            "Memiliki Riwayat Penyakit Epilepsi dan/atau Gangguan Saraf Lainnya",
            "Memiliki Riwayat Penyakit Epilepsi dan/atau Gangguan Saraf Lainnya",
        ),
        (
            "Memiliki Riwayat Penyakit Asma/Saluran Pernafasan Lainnya",
            "Memiliki Riwayat Penyakit Asma/Saluran Pernafasan Lainnya",
        ),
        (
            "Memiliki Asuransi BPJS dan/atau Asuransi Lainnya",
            "Memiliki Asuransi BPJS dan/atau Asuransi Lainnya",
        ),
        (
            "Memiliki Riwayat Alergi Terhadap Obat Tertentu",
            "Memiliki Riwayat Alergi Terhadap Obat Tertentu",
        ),
    ]

    for condition in medical_conditions:
        locals()[condition[0].replace(" ", "_").lower()] = forms.ChoiceField(
            label=condition[0],
            choices=[("Ya", "Ya"), ("Tidak", "Tidak")],
            widget=forms.RadioSelect(
                attrs={"class": "inline-block"},  # Ensure radio buttons are stacked
            ),
        )

    allergies = forms.CharField(
        label="Jika iya sebutkan",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Sebutkan Alergi"}),
    )

    bib_name = forms.CharField(
        label="Nama pada BIB",
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Masukkan nama yang valid pada BIB"}
        ),
    )
    ukuran_baju = forms.ChoiceField(
        label="Ukuran Baju", choices=[("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")]
    )

    payment_proof = forms.FileField(label="Struk/Nota Konfirmasi Pembayaran")
