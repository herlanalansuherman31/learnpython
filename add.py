import math
from platform import system
class mengitung_luas:
    def luas_persegi(sisi):
        return sisi * sisi
    def luas_segitiga(alas, tinggi):
        return 0.5 * alas * tinggi  
    def luas_lingkaran(jari_jari):
        return math.pi * jari_jari * jari_jari
    def luas_trapesium(sisi_a, sisi_b, tinggi):
        return 0.5 * (sisi_a + sisi_b) * tinggi

def main():
    print("""
pilih bangun datar yang ingin dihitung luasnya:
1. Persegi
2. Segitiga
3. Lingkaran
4. Trapesium
5. Keluar""")
    while True: 
        pilihan = input("Masukkan pilihan (1-5): ")
        try:
            if pilihan == '1':
                sisi = float(input("Masukkan panjang sisi persegi: "))
                print("Luas Persegi:", mengitung_luas.luas_persegi(sisi))
            elif pilihan == '2':
                alas = float(input("Masukkan alas segitiga: "))
                tinggi = float(input("Masukkan tinggi segitiga: "))
                print("Luas Segitiga:", mengitung_luas.luas_segitiga(alas, tinggi))
            elif pilihan == '3':
                jari_jari = float(input("Masukkan jari-jari lingkaran: "))
                print("Luas Lingkaran:", mengitung_luas.luas_lingkaran(jari_jari))
            elif pilihan == '4':
                sisi_a = float(input("Masukkan panjang sisi a trapesium: "))
                sisi_b = float(input("Masukkan panjang sisi b trapesium: "))
                tinggi = float(input("Masukkan tinggi trapesium: "))
                print("Luas Trapesium:", mengitung_luas.luas_trapesium(sisi_a, sisi_b, tinggi))
            elif pilihan == '5':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("input tidak valid, silahkan masukan angka")

if __name__ == "__main__":
    main()