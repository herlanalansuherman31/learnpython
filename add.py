import math
# x = 3.3
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)
# print(result)
# abs mengilangkan pangkat, mac angka terteinggi min angka terendah
print ("==================keliling lingkaran=======================")
radius = float(input("masukan radius lingkaran: "))
keliling = 2* math.pi * radius
print(f"keliling lingkaran adalah: {round(keliling, 2)} cm") #round buat membulatkan

print ("==================area lingkaran=======================")
radius = float(input("masukan radius lingkaran = "))

area = math.pi * pow(radius, 2) # pow menghitung pangkat 
print(f"nilai area lingkaran adalah = {round(area, 2)}cm^2")

print ("==================luas segitiga=======================")

a = float(input("masukan sisi a = "))
b = float(input("masukan sisi b = "))

c = math.sqrt(pow(a, 2) + pow(b, 2))  #math.sqrt adalah akar pangkat

print(f"sisi c = {round(c, 2)}")