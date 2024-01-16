#List
perpustakaan = []

#Fungsi Tambahkan Buku
def tambah_buku(perpustakaan, judul, penulis):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "status": "Tersedia"
    }
    perpustakaan.append(buku)

#Fungsi Pinjam Buku
def pinjam_buku(perpustakaan, judul):
    for buku in perpustakaan:
        if buku["judul"] == judul:
            if buku["status"] == "Tersedia":
                buku["status"] = "Dipinjam"
                print("Buku ", judul, "Telah Dipinjam.")
            else:
                print("Buku ", judul, "Tidak Tersedia.")
        return
    print("Buku ", judul, "Tidak Ditemukan.")

#Fungsi Kembalikan Buku
def kembalikan_buku(perpustakaan, judul):
    for buku in perpustakaan:
        if buku["judul"] == judul:
            if buku["status"] == "Dipinjam":
                buku["status"] = "Tersedia"
                print("Buku ", judul, "Telah Dikembalikan.")
             else:
                print("Buku ", judul, "Telah Tersedia.")
        return
    print("Buku ", judul, "Tidak Ditemukan.")

#Fungsi Menampilkan Daftar Buku
def tampilkan_buku(perpustakaan):
    print("Daftar Buku :")
    for buku in perpustakaan:
        print("Judul   : ", buku["judul"])
        print("Penulis : ", buku["penulis"])
        print("Status  : ", buku["status"])
        print("")

#Menu
while True:
    print("="*50)
    print(" "*12, "===Sistem Perpustakaan===")
    print("\n1. Tambah Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Cek Daftar Buku")
    print("5. Keluar")
    print("")
    print("="*50)

    pilihan = int(input(">>> "))
    if pilihan == 1:
        judul = input("Masukkan Judul Buku : ")
        penulis = input("Masukkan Penulis Buku ")
        print("Buku Berhasil Ditambahkan.")
        tambah_buku(perpustakaan, judul, penulis)
    elif pilihan == 2:
        tampilkan_buku(perpustakaan)
        judul = input("Masukkan Judul Buku : ")
        pinjam_buku(perpustakaan, judul)
    elif pilihan == 3:
        judul = input("Masukkan Judul Buku : ")
        kembalikan_buku(perpustakaan, judul)
    elif pilihan == 4:
        tampilkan_buku(perpustakaan)
    elif pilihan == 5:
        print("Terima Kasih Telah Menggunakan Layanan Kami!")
        break
    else:
        print("Pilihan Tidak Valid. Silahkan Coba Lagi!")