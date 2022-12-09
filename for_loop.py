# Belajar for loop

pelanggan = ["Aditra", "Vanya", "Yessi", "Fatur"]

pelanggan.append("Tono") #tambah data
pelanggan.append("Toni")

# mengakses semua nama pelanggan? secara manual
#print(pelanggan[0])
#print(pelanggan[1])
#print(pelanggan[2])
#print(pelanggan[3])

#mengakses semua nama penlanggan secara otomatis
for nama in pelanggan: #nama adalah variable yang kita buat sendiri
    print(nama) #statement setelah perintah "for"    akan diulang-ulang 
    print(f"Nama Pelanggan: {nama}")