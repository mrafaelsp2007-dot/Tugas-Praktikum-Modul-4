#kelompok 35
#RAFIF ILMAN PRAYATA               NIM = 21120126130099
#Muhammad Rafael Shaka Putra       NIM = 21120126140135
#Ikhsan Seno Hanif                 NIM = 21120126140190

def tampilkan_watermark():
    print("=" * 40)
    print("Pemantauan Kota Bekasi")
    print("Kelompok = 35")
    print("=" * 40)

def sapa_pengunjung(nama, asal_daerah):
    print(f"Selamat datang {nama} dari {asal_daerah} "
          f"di sistem pemantauan Kota Bekasi.")

def ambil_nama_desa():
    return "Kota Bekasi"

def cek_status_suhu(suhu):
    if suhu < 20:
        return "Suhu terpantau dingin."
    elif suhu <= 30:
        return "Suhu normal."
    else:
        return "Suhu terpantau Panas."


# Arbitrary function (jumlah argumen bebas), non-return
def catat_titik_cctv(*titik_lokasi):
    print("Lokasi CCTV yang sedang aktif:")
    for lokasi in titik_lokasi:
        print(f"- {lokasi}")


# Lambda function
hitung_selisih = lambda x, y: x - y


# ===== Pemanggilan fungsi =====
tampilkan_watermark()
print("Wilayah pemantauan:", ambil_nama_desa())
print("-" * 30)
sapa_pengunjung("Rafael", "Bekasi")
print("-" * 30)
hasil_suhu = cek_status_suhu(37)
print(hasil_suhu)
print("-" * 37)
catat_titik_cctv("Gerbang", "Lapangan", "Masjid")
print("-" * 30)
print("Selisih pengunjung hari ini dan kemarin:",
      hitung_selisih(178, 140))