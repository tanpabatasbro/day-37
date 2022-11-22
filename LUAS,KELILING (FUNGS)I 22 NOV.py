import os

def header():
    os.system("cls")
    print(f"{'PROGRAM MENGHITUG LUAS ':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANNG ':^40}")
    print(f"{'-'*40:^40}")

def input_nilai():
    lebar = int(input("Masukkan Nilai Lebar : "))
    panjang = int(input("Masukkan Nilai panjang :"))
    return  lebar,panjang

def hitung_luas(lebar,panjang):
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    return 2*(lebar+panjang)

def display(message,value):
    print(f"Hasil Perhitungan {message} = {value}")

while  True:
    header()

    LEBAR,PANJANG = input_nilai()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display("Luas", LUAS)
    display("Keliling", KELILING)

    isContinue = input("\nApakah Ingin Lanjut (y/n)?")
    if  isContinue == "n":
        break

print(f"\nPROGRAM TELAH  SELESAI TERIMA KASIH ")
    
