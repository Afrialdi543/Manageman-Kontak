"Program Manajemen Kontak"

kontak1 = {'nama': "Rizal", 'HP': '082250795878', 'Email': 'afrialdirizal5@gmail.com'}
kontak2 = {'nama': "Rizal2", 'HP': '082250795878', 'Email': 'afrialdirizal25@gmail.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak:")
    print("1. Melihat semua kontak")
    print("2. Menambahkan kontak")
    print("3. Menghapus kontak")
    print("4. Keluar dari kontak")

    pilihan = input("\nMasukkan pilihan menu kontak (1-4) : ")
    if pilihan == '1':
        #Melihat kontak
        if kontak:
            print("\nBerikut adalah kontak yang Anda miliki: ")
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]}, {item["HP"]}, Email({item["Email"]})')
        else:
            print("Kontak Anda masih kosong!")

    elif pilihan == '2':
        #menambahkan kontak
        nama = input("\nMasukkan nama kontak yang akan ditambahkan: ")
        HP = input("Masukkan nomor kontak hp yang ingin ditambahkan: ")
        Email = input("Masukkan nama email yang ingin ditambahkan: ")
        kontak_baru = {'nama':nama, 'HP':HP, 'Email':Email}
        kontak.append(kontak_baru)
        print("\tKontak berhasil ditambahkan!!!")
    elif pilihan == '3':
        #menghapus kontak
        if kontak:
            print("\nBerikut adalah kontak yang Anda miliki: ")
            for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item["nama"]}, {item["HP"]}, {item["Email"]}')
        else:
            print("Kontak Anda masih kosong!")
            continue

        hapus_kontak = int(input("\nMasukkan nomor kontak yang ingin dihapus: "))
        del kontak[hapus_kontak-1]
        print("\nKontak telah berhasil dihapus!")
    elif pilihan == '4':
        #keluar kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah!")
