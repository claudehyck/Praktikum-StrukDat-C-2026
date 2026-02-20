from kurs import data_kurs

def konversi_ke_idr(kode_asal, jumlah):
    if kode_asal == "IDR":
        return jumlah
    return jumlah * data_kurs.get(kode_asal, 0)

def konversi_dari_idr(kode_tujuan, jumlah_idr):
    if kode_tujuan == "IDR":
        return jumlah_idr
    kurs = data_kurs.get(kode_tujuan, 0)
    if kurs == 0:
        return 0
    return jumlah_idr / kurs