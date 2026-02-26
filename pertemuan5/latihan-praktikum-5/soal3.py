ukm_coding = {"Andi", "Budi", "Caca", "Deni"}  
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"} 

#a
hanya_coding = ukm_coding - ukm_robotik
print("Hanya mendaftar coding :", hanya_coding)

#b
seluruh_mahasiswa = ukm_coding | ukm_robotik
print("Seluruh mahasiswa unik :", seluruh_mahasiswa)

#c
andi_robotik = "Andi" in ukm_robotik
print("Apakah Andi anggota robotik?", andi_robotik)