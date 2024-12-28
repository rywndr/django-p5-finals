# Generated by Django 5.1.4 on 2024-12-28 00:12

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.IntegerField(editable=False, unique=True)),
                ('nama', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('jenis_kelamin', models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=20)),
                ('tempat_lahir', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=20)),
                ('alamat', models.CharField(max_length=255)),
                ('kota', models.CharField(max_length=255)),
                ('provinsi', models.CharField(max_length=255)),
                ('warga_negara', models.CharField(choices=[('Indonesia', 'Indonesia'), ('Singapore', 'Singapore'), ('Malaysia', 'Malaysia'), ('Lainnya', 'Lainnya')], max_length=20)),
                ('golongan_darah', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2)),
                ('jenis_id', models.CharField(choices=[('KTP', 'KTP'), ('Kartu Pelajar', 'Kartu Pelajar'), ('SIM', 'SIM'), ('Passport', 'Passport')], max_length=20)),
                ('nomor_id', models.CharField(max_length=255)),
                ('id_upload', models.FileField(upload_to=home.models.ktp_upload_path, validators=[home.models.validate_file_extension, home.models.validate_file_size])),
                ('kategori', models.CharField(choices=[('Umum', 'Umum (dibawah 45 tahun)'), ('Master', 'Master (45 tahun ke atas)')], max_length=20)),
                ('emergency_contact', models.CharField(max_length=255)),
                ('emergency_phone', models.CharField(max_length=20)),
                ('memiliki_riwayat_penyakit_jantung', models.CharField(choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], max_length=5)),
                ('memiliki_riwayat_penyakit_hipertensi', models.CharField(choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], max_length=5)),
                ('memiliki_riwayat_penyakit_kronik_tahunan_lainnya', models.CharField(choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], max_length=5)),
                ('memiliki_riwayat_penyakit_epilepsi_dan_atau_gangguan_saraf_lainnya', models.CharField(choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], max_length=5)),
                ('memiliki_riwayat_penyakit_asma_saluran_pernafasan_lainnya', models.CharField(choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], max_length=5)),
                ('memiliki_asuransi_bpjs_dan_atau_asuransi_lainnya', models.CharField(choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], max_length=5)),
                ('memiliki_riwayat_alergi_terhadap_obat_tertentu', models.CharField(choices=[('Ya', 'Ya'), ('Tidak', 'Tidak')], max_length=5)),
                ('allergies', models.CharField(blank=True, max_length=255, null=True)),
                ('bib_name', models.CharField(max_length=255)),
                ('ukuran_baju', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=2)),
                ('payment_proof', models.FileField(upload_to=home.models.payment_upload_path, validators=[home.models.validate_file_extension, home.models.validate_file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['registration_number'],
            },
        ),
    ]