from KaryawanKriteria.models import KaryawanKriteria

# Pembentukan rules 
rules = [
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'rendah', 'Kebersihan': 'rendah', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'rendah', 'Kebersihan': 'rendah', 'Ketelitian': 'tinggi', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'rendah', 'Kebersihan': 'tinggi', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'rendah', 'Kebersihan': 'tinggi', 'Ketelitian': 'tinggi', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'tinggi', 'Kebersihan': 'rendah', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'tinggi', 'Kebersihan': 'rendah', 'Ketelitian': 'tinggi', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'tinggi', 'Kebersihan': 'tinggi', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'tinggi', 'Kebersihan': 'tinggi', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'rendah', 'Kebersihan': 'rendah', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'rendah', 'Kebersihan': 'rendah', 'Ketelitian': 'tinggi', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'rendah', 'Kebersihan': 'tinggi', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'rendah', 'Kebersihan': 'tinggi', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'tinggi', 'Kebersihan': 'rendah', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'tinggi', 'Kebersihan': 'rendah', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'tinggi', 'Kebersihan': 'tinggi', 'Ketelitian': 'rendah', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'rendah', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'tinggi', 'Kebersihan': 'tinggi', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'rendah', 'Kebersihan': 'rendah', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'rendah', 'Kebersihan': 'rendah', 'Ketelitian': 'tinggi', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'rendah', 'Kebersihan': 'tinggi', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'rendah', 'Kebersihan': 'tinggi', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'tinggi', 'Kebersihan': 'rendah', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'tinggi', 'Kebersihan': 'rendah', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'tinggi', 'Kebersihan': 'tinggi', 'Ketelitian': 'rendah', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'rendah', 'Kerja Sama': 'tinggi', 'Kebersihan': 'tinggi', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'rendah', 'Kebersihan': 'rendah', 'Ketelitian': 'rendah', 'Kinerja': 'buruk'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'rendah', 'Kebersihan': 'rendah', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'rendah', 'Kebersihan': 'tinggi', 'Ketelitian': 'rendah', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'rendah', 'Kebersihan': 'tinggi', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'tinggi', 'Kebersihan': 'rendah', 'Ketelitian': 'rendah', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'tinggi', 'Kebersihan': 'rendah', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'tinggi', 'Kebersihan': 'tinggi', 'Ketelitian': 'rendah', 'Kinerja': 'baik'},
    {'Kedisiplinan': 'tinggi', 'Tanggung Jawab': 'tinggi', 'Kerja Sama': 'tinggi', 'Kebersihan': 'tinggi', 'Ketelitian': 'tinggi', 'Kinerja': 'baik'},
]

# Fungsi keanggotaan untuk "Rendah"
def membership_rendah(x):
    if x <= 33:
        return 1
    elif 33 < x < 67:
        return (67 - x) / (67 - 33)
    else:  # x >= 67
        return 0

# Fungsi keanggotaan untuk "Tinggi"
def membership_tinggi(x):
    if 67 <= x <= 100:
        return 1
    elif 33 < x < 67:
        return (x - 33) / (67 - 33)
    else:  # x < 33 or x > 100
        return 0

# Fungsi fuzzifikasi yang hanya mempertimbangkan "rendah" dan "tinggi"
def fuzzifikasi(nilai):
    rendah = membership_rendah(nilai)
    tinggi = membership_tinggi(nilai)
    
    return {'rendah': rendah, 'tinggi': tinggi}

def calculate_alpha_predicate_and_z(kriteria_dict, rule):
    values = []
    missing_kriteria = []

    for kriteria, kondisi in rule.items():
        if kriteria != 'Kinerja':
            if kriteria not in kriteria_dict:
                missing_kriteria.append(kriteria)
            else:
                values.append(kriteria_dict[kriteria][kondisi])

    if missing_kriteria:
        raise KeyError(f'Kriteria berikut tidak ditemukan dalam data fuzzifikasi: {", ".join(missing_kriteria)}')

    alpha_predikat = min(values)

    if alpha_predikat == 0:
        z = 67  # Nilai default jika alpha_predikat 0 (tidak memberikan kontribusi)
    else:
        if rule['Kinerja'] == 'buruk':
            z = -((alpha_predikat * (67 - 33)) - 67)  # Rumus untuk Kinerja "buruk"
        elif rule['Kinerja'] == 'baik':
            z = ((alpha_predikat * (67 - 33)) + 33)  # Rumus untuk Kinerja "baik"
    
    return alpha_predikat, z

# Fungsi utama untuk perhitungan Fuzzy Tsukamoto
def fuzzy_tsukamoto_calculate(karyawan_kriteria):
    kriteria_dict = {}
    total_alpha_z = 0
    total_alpha = 0

    for item in karyawan_kriteria:
        kriteria_dict[item.kriteria.nama] = fuzzifikasi(item.nilai)

    for rule in rules:
        try:
            alpha_predikat, z = calculate_alpha_predicate_and_z(kriteria_dict, rule)
            print(f'Rule: {rule}, Alpha: {alpha_predikat}, Z: {z}')  # Debugging
            total_alpha_z += alpha_predikat * z
            total_alpha += alpha_predikat
        except KeyError as e:
            print(e)  # Debugging untuk melihat kriteria mana yang tidak ditemukan
            continue  # Lanjutkan ke rule berikutnya jika ada kriteria yang tidak ditemukan

    if total_alpha != 0:
        hasil_akhir = total_alpha_z / total_alpha
    else:
        hasil_akhir = 0

    return hasil_akhir

