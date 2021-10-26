ulang = "y"
while ulang == "y":
    print("""
    Pilih satuan suhu yang ingin diubah ke celcius :
    1. Fahreinheit
    2. Kelvin
    3. Reamur
    4. exit
    """)
    pilih = int(input("Pilih : "))
    print("======================================")
    if pilih == 1 :
        print("Konversi Fahreinheit")
        f = int(input("Masukkan Nilai Fahreinheit : "))
        fa = f-32*(5/9)
        print("Nilai Celcius : ",str(fa), " C")
        print()
        ulang = input("Ingin menghitung lagi ? (y/n) : ")
    elif pilih == 2 :
        print("Konversi Kelvin")
        k = int(input("Masukkan Nilai Kelvin : "))
        ke = k-273
        print("Nilai Celcius : ", str(ke), " C")
        print()
        ulang = input("Ingin menghitung lagi ? (y/n) : ")
    elif pilih == 3:
        print("Konversi Reamur")
        r = int(input("Masukkan Nilai Reamur : "))
        re = (5/4)*r
        print("Nilai Celcius : ", str(re), " C")
        print()
        ulang = input("Ingin menghitung lagi ? (y/n) : ")
    elif pilih == 4:
        break
    else :
        print("Pilih antara 1-3 !!!")

print("======================================")
print("Terima Kasih")