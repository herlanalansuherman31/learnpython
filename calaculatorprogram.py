def main():
    while True:
        print("kalkulator sederhana")
        operasi = input("masukan operasi(+,-,*,/): ")
        try:
            if operasi == "+":
                bilangan1 = float(input("masukan bilangan pertama: "))
                bilangan2 = float(input("masukan bilangan kedua: "))
                hasil = bilangan1+bilangan2
                print(f"hasil penjumlahan adalah {hasil}")
            elif operasi == "-":
                bilangan1 = float(input("masukan bilangan pertama: "))
                bilangan2 = float(input("masukan bilangan kedua: "))
                hasil = bilangan1-bilangan2
                print(f"hasil pengurangan adalah {hasil}")
            elif operasi == "*":
                bilangan1 = float(input("masukan bilangan pertama: "))
                bilangan2 = float(input("masukan bilangan kedua: "))
                hasil = bilangan1*bilangan2
                print(f"hasil perkalian adalah {hasil}")
            elif operasi == "/":
                bilangan1 = float(input("masukan bilangan pertama: "))
                bilangan2 = float(input("masukan bilangan kedua: "))
                if bilangan2 == 0:
                    print("error: pembagian dengan nol tidak diperbolehkan")
                    continue
                else:
                    hasil = bilangan1/bilangan2
                    print(f"hasil pembagian adalah {round(hasil,2)}")
            else:
                print("bilangan tidak diemukan silahkan masukan angka")
        except ValueError:
            print("input tidak valid masukan angka")
        lanjut = input("apakah ingin melanjutkan(y/n): ")
        if lanjut == "y":
            continue
        elif lanjut == "n":
            print("terimakasih sudah mencoba")
            break
        else:
            print("terimakasih sudah mencoba")
            break
    
if __name__=="__main__":
    main()





