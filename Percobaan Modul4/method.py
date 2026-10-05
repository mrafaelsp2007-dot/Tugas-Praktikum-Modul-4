#kelompok 35
#RAFIF ILMAN PRAYATA               NIM = 21120126130099
#Muhammad Rafael Shaka Putra       NIM = 21120126140135
#Ikhsan Seno Hanif                 NIM = 21120126140190


class LaprakModul4:
    def __init__(self, nama, konsentrasi):
        self.nama = nama
        self.konsentrasi = konsentrasi

    def profil(self):
        print(f"Halo! Saya {self.nama}, mahasiswa Teknik Komputer "
              f"dengan fokus di {self.konsentrasi}.")

    def deadline_tugas(self, hari):
        print("Waktu tersisa untuk pengumpulan project:")
        while hari > 0:
            print(f"{hari} hari lagi, kerjain tugasnya")
            hari -= 1
        print("Waktu habis! Sistem ditutup.")

obj = LaprakModul4("Rafael", "IPK 4")
obj.profil()
obj.deadline_tugas(2)