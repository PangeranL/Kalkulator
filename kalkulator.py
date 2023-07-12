def penjumalahan(a, b):
    return a + b 

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian Tidak Bisa Dibagi Nol"
    
print("---!Kalkulator Sederhana---")
print("---------------------------")

while True:
    print("Pilih Menu")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukan Pilihan (1/2/3/4/5): ")

    if pilihan == "5":
        print("Anda Telah Keluar Dari Kalkulator")
        break

    angka1 = float(input("Masukan Angka Pertama: "))
    angka2 = float(input("Masukan Angka Kedua: "))

    if pilihan == "1":
        hasil = penjumalahan(angka1, angka2)
        print("Hasil penjumalahan = ", hasil)
    elif pilihan == "2":
        hasil = pengurangan(angka1, angka2)
        print("Hasil Pengurangan = ", hasil)
    elif pilihan == "3":
        hasil = perkalian(angka1, angka2)
        print("Hasil Perkalian = ", hasil)
    elif pilihan == "4":
        hasil = pembagian(angka1, angka2)
        print("Hasil Pembagian = ", hasil)
    else:
        print("Anda Tidak Memasukan Pilihan.") 