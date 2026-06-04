jam = int(input("Waktu mulai (jam): "))
menit = int(input("Waktu mulai (menit): "))
durasi = int(input("Durasi Acara (menit): "))

total_menit = menit + durasi
jam += total_menit // 60
menit = total_menit % 60

jam = jam % 24  # agar tidak lebih dari 23

print("Acara selesai pukul {:02d}:{:02d}".format(jam, menit))