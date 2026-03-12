def pisahkan_ganjil_genap(daftar_plat):
    ganjil = []
    genap = []
    
    for plat in daftar_plat:
        bagian = plat.split() 
        angka_string = bagian[1]
        angka_terakhir = int(angka_string[-1])
        
        if angka_terakhir % 2 == 0:
            genap.append(plat)
        else:
            ganjil.append(plat)
            
    return ganjil, genap

input_plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]

list_ganjil, list_genap = pisahkan_ganjil_genap(input_plat)

print(f"Kendaraan Ganjil: {list_ganjil}")
print(f"Kendaraan Genap : {list_genap}")