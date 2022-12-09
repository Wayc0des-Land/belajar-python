# membuat program menggunakan For-Loop,  type data List dan  type data Range

banyak = int(input("Berapa Banyak data?")) #data integer "int"

nama = [] #variable nama berupa list
umur = [] #variable umur

for i in range(0, banyak): #perulangan sejumlah input data, "i" nama variable
    print(f"Data ke {i}")
    input_nama = input("Nama :") #minta data nama
    input_umur = int(input("Umur :")) #minta data umur

    nama.append(input_nama) #penambahan data nama
    umur.append(input_umur) #penambahan data umur

print(nama)
print(umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur} tahun")