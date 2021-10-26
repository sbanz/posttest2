mahasiswa = {
    "nama": "",
    "nim": "",
    "prodi": "",
    "angkatan": "",
    "ipk": "",
}

def data():
    print("Masukkan data Mahasiswa dibawah :")
    mahasiswa["nama"] = input("Nama : ")
    mahasiswa["nim"] = input("NIM : ")
    mahasiswa["prodi"] = input("Prodi : ")
    mahasiswa["angkatan"] = input("Angkatan : ")
    mahasiswa["ipk"] = float(input("IPK : "))
data()

ulang = "y"
while ulang == "y" :
    print("""
    Pilih menu selanjutnya :
    1. Ubah data
    2. Lihat data
    3. keluar
    """)
    pilih = input("Pilihan Menu : ")

    if pilih == "1":
        data()
    elif pilih == "2":
        print("Nama : " , mahasiswa["nama"])
        print("NIM : " , mahasiswa["nim"])
        print("Prodi : " , mahasiswa["prodi"])
        print("Angkatan : " , mahasiswa["angkatan"])
        print("IPK : ", mahasiswa["ipk"])
        ulang = input("kembali ke menu ? (y/n) : ")
    elif pilih == "3":
        break
    else:
        print()
        print("Pilih antara 1-3 !!!")

print()
print("Terima Kasih !!!")
