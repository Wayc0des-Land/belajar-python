# belajar elif => else if
# menerima input dari user setelah itu kita menampilkan sesuai dengan user tersebut

menu_pilihan = input("Silahkan pilih menu [1-3] : ")

if menu_pilihan == "1":
    print("Anda memilih menu 1")
elif menu_pilihan == "2":
    print("Anda memilih menu 2")
elif menu_pilihan == "3":
    print("Anda memilih menu 3")
else:
    print("Menu tidak tersedia")