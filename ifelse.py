class atm:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal

    def cek_saldo(self):
        return self.saldo

    def setor_uang(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            return True
        else:
            return False

    def tarik_uang(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            return True
        else:
            return False
def main():
    atm_user = atm(1000000)  # saldo awal 1.000.000
    while True:
        print("""
        ATM Sederhana
        1. Cek Saldo
        2. Setor Uang
        3. Tarik Uang
        4. Keluar
        """)
        pilihan = input("Pilih menu (1-4): ")
        try:
            if pilihan == '1':
                print("Saldo Anda:", atm_user.cek_saldo())
            elif pilihan == '2':
                jumlah_setor = float(input("Masukkan jumlah uang yang akan disetor: "))
                if atm_user.setor_uang(jumlah_setor):
                    print("Setor uang berhasil.")
                else:
                    print("Jumlah setor harus positif.")
            elif pilihan == '3':
                jumlah_tarik = float(input("Masukkan jumlah uang yang akan ditarik: "))
                if atm_user.tarik_uang(jumlah_tarik):
                    print("Tarik uang berhasil.")
                else:
                    print("Saldo tidak mencukupi atau jumlah tarik tidak valid.")
            elif pilihan == '4':
                print("Terima kasih telah menggunakan ATM kami.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid, silahkan masukan angka.")
if __name__ == "__main__":
    main()