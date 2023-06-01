import csv
import os
import random

# Nama file input
file_input = 'mahasiswa_a.csv'

# Buat nama file output
nama_file, ext = os.path.splitext(file_input)
file_output = f'{nama_file}_terpilih{ext}'

# Baca file input
with open(file_input, mode='r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Ambil 10 baris data random dari file
data_terpilih = random.sample(data, k=10)

# Simpan data terpilih ke file output
with open(file_output, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['NIM', 'Nama', 'Nilai Tugas1', 'Nilai Tugas2', 'Nilai Tugas3'])
    writer.writerows(data_terpilih)
