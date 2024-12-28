import os

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Max


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".pdf", ".jpg", ".jpeg", ".png"]
    if ext.lower() not in valid_extensions:
        raise ValidationError("File harus berupa PDF, JPG, JPEG, atau PNG.")


def validate_file_size(value):
    limit = 2 * 1024 * 1024  # 2 MB
    if value.size > limit:
        raise ValidationError("Ukuran file terlalu besar. Maksimal 2 MB.")


def ktp_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    print(f"File extension: {ext}")

    if not instance.registration_number:
        last_reg = Registration.objects.aggregate(Max("registration_number"))
        next_number = (last_reg.get("registration_number__max") or 0) + 1
        print(f"Next registration number: {next_number}")

        if not isinstance(next_number, int):
            raise ValueError("Unexpected type for next_number, expected int.")

        new_filename = f"ktp_{next_number:04d}{ext}"
    else:
        new_filename = f"ktp_{instance.registration_number:04d}{ext}"

    if not isinstance(new_filename, str):
        raise ValueError("Unexpected type for new_filename, expected str.")

    path = os.path.join("ktp", new_filename)
    print(f"Generated path: {path}")
    return path


def payment_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    print(f"File extension: {ext}")

    if not instance.registration_number:
        last_reg = Registration.objects.aggregate(Max("registration_number"))
        next_number = (last_reg.get("registration_number__max") or 0) + 1
        print(f"Next registration number: {next_number}")

        if not isinstance(next_number, int):
            raise ValueError("Unexpected type for next_number, expected int.")

        new_filename = f"payment_{next_number:04d}{ext}"
    else:
        new_filename = f"payment_{instance.registration_number:04d}{ext}"

    if not isinstance(new_filename, str):
        raise ValueError("Unexpected type for new_filename, expected str.")

    path = os.path.join("payment_proofs", new_filename)
    print(f"Generated path: {path}")
    return path


class Registration(models.Model):
    registration_number = models.IntegerField(unique=True, editable=False)
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    jenis_kelamin = models.CharField(
        max_length=20, choices=[("Laki-laki", "Laki-laki"), ("Perempuan", "Perempuan")]
    )
    tempat_lahir = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    alamat = models.CharField(max_length=255)
    kota = models.CharField(max_length=255)
    provinsi = models.CharField(max_length=255)
    warga_negara = models.CharField(
        max_length=20,
        choices=[
            ("Indonesia", "Indonesia"),
            ("Singapore", "Singapore"),
            ("Malaysia", "Malaysia"),
            ("Lainnya", "Lainnya"),
        ],
    )
    golongan_darah = models.CharField(
        max_length=2, choices=[("A", "A"), ("B", "B"), ("AB", "AB"), ("O", "O")]
    )
    jenis_id = models.CharField(
        max_length=20,
        choices=[
            ("KTP", "KTP"),
            ("Kartu Pelajar", "Kartu Pelajar"),
            ("SIM", "SIM"),
            ("Passport", "Passport"),
        ],
    )
    nomor_id = models.CharField(max_length=255)
    id_upload = models.FileField(
        upload_to=ktp_upload_path,
        validators=[validate_file_extension, validate_file_size],
    )

    kategori = models.CharField(
        max_length=20,
        choices=[
            ("Umum", "Umum (dibawah 45 tahun)"),
            ("Master", "Master (45 tahun ke atas)"),
        ],
    )

    emergency_contact = models.CharField(max_length=255)
    emergency_phone = models.CharField(max_length=20)

    # Medical conditions
    memiliki_riwayat_penyakit_jantung = models.CharField(
        max_length=5, choices=[("Ya", "Ya"), ("Tidak", "Tidak")]
    )
    memiliki_riwayat_penyakit_hipertensi = models.CharField(
        max_length=5, choices=[("Ya", "Ya"), ("Tidak", "Tidak")]
    )
    memiliki_riwayat_penyakit_kronik_tahunan_lainnya = models.CharField(
        max_length=5, choices=[("Ya", "Ya"), ("Tidak", "Tidak")]
    )
    memiliki_riwayat_penyakit_epilepsi_dan_atau_gangguan_saraf_lainnya = (
        models.CharField(max_length=5, choices=[("Ya", "Ya"), ("Tidak", "Tidak")])
    )
    memiliki_riwayat_penyakit_asma_saluran_pernafasan_lainnya = models.CharField(
        max_length=5, choices=[("Ya", "Ya"), ("Tidak", "Tidak")]
    )
    memiliki_asuransi_bpjs_dan_atau_asuransi_lainnya = models.CharField(
        max_length=5, choices=[("Ya", "Ya"), ("Tidak", "Tidak")]
    )
    memiliki_riwayat_alergi_terhadap_obat_tertentu = models.CharField(
        max_length=5, choices=[("Ya", "Ya"), ("Tidak", "Tidak")]
    )

    allergies = models.CharField(max_length=255, blank=True, null=True)

    bib_name = models.CharField(max_length=255)
    ukuran_baju = models.CharField(
        max_length=2, choices=[("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")]
    )

    payment_proof = models.FileField(
        upload_to=payment_upload_path,
        validators=[validate_file_extension, validate_file_size],
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.registration_number:
            # Get all existing registration numbers
            existing_numbers = set(
                Registration.objects.values_list("registration_number", flat=True)
            )

            # Find the first available number starting from 1
            number = 1
            while number in existing_numbers:
                number += 1

            self.registration_number = number

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.registration_number:04d} - {self.nama}"

    class Meta:
        ordering = ["registration_number"]
