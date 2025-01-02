"Program Manajemen Kontak"

class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        # Melihat kontak
        if self.kontak:
            print("\nBerikut adalah kontak yang Anda miliki: ")
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["nama"]}, {item["HP"]}, Email({item["Email"]})')
        else:
            print("Kontak Anda masih kosong!")
            return 1

    def menambahkan_kontak(self):
        # menambahkan kontak
        nama = input("\nMasukkan nama kontak yang akan ditambahkan: ")
        HP = input("Masukkan nomor kontak hp yang ingin ditambahkan: ")
        Email = input("Masukkan nama email yang ingin ditambahkan: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'Email': Email}
        self.kontak.append(kontak_baru)
        print("\tKontak berhasil ditambahkan!!!")

    def menghapus_kontak(self):
        # menghapus kontak
        if self.melihat_kontak() == 1:

            return
            print("\tKontak Anda masih kosong!")
        else:
            hapus_kontak = int(input("\nMasukkan nomor kontak yang ingin dihapus: "))
            del self.kontak[hapus_kontak-1]
            print("\nKontak telah berhasil dihapus!")

kontak_keluarga = Kontak()
kontak_teman = Kontak()
kontak_kerja = Kontak()


while True:

    #menu pilihan
    print("\nMenu Kontak:")
    print("1. Melihat semua kontak")
    print("2. Menambahkan kontak")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    #input pilihan
    pilihan = input("\nMasukkan pilihan menu kontak (1-4) : ")
    if pilihan == '1':
        kontak_kerja.melihat_kontak()
    elif pilihan == '2':
        kontak_kerja.menambahkan_kontak()
    elif pilihan == '3':
        kontak_kerja.menghapus_kontak()
    elif pilihan == '4':
        #keluar kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah!")
