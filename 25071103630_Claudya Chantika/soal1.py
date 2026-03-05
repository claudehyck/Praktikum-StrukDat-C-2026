def registrasi_gadget(merk, tipe, harga, sn):
    if harga <= 1000000:
        print("error")
        return None

    if len(sn) < 5:
        print("error")
        return None
    return{"merk" : merk, "tipe" : tipe, "harga" : harga, "sn" : sn, "status" : "tersedia"}

inventaris = []

for i in range(3):
    merk = input("Merk Gadget :")
    tipe = input("Tipe Gadget :")
    harga = int(input("Harga Gadget :"))
    sn = input("SN Gadget :")
    gadget = registrasi_gadget(merk, tipe, harga, sn)
    if gadget :
        inventaris.append(gadget)
    else :
        print("Registrasi gagal")

for item in inventaris :
    print(item)