#perogram untuk meminta biodata user
class biodata_user:
    def __init__(self):
        self.nama = "HERLAN ALAN SUHERMAN"
        self.pasword = "alan123"
    def input_user(self):
        nama = input("masukan nama anda: ")
        pasword = input("masukan pasword anda: ")
        if nama == self.nama and pasword == self.pasword:
            return True
        else:
            return False
    def tampil_biodata(self):
        print("===BIODATA USER===")
        print("nama :", self.nama)
        print("""
alamat                : KP. BENTENG, RT 03 RW 05, DS.KUTAJAYA
tempat, tanggal lahir : Cicurug, 12 juni 2006
hobi                  : menggambar, membaca buku
cita-cita             : menjadi seorang programmer handal
pendidikan            : Univeristas Djuanda
pekerjaan             : Indomaret
agama                 : islam
status                : pelajar/mahasiswa
status hubungan       : single""")

def main():
    user = biodata_user()
    if user.input_user():
        user.tampil_biodata()
    else:
        print("nama atau pasword salah")
if __name__ == "__main__":
    main()