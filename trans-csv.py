import csv #mengimport model 'csv" yang diperlukan untuk membaca dan menulis file CSV

# Fungsi untuk menambahkan transaksi baru ke file CSV
def tambah_transaksi():
    tanggal = input("Tanggal Transaksi: ")
    nama_barang = input("Nama Barang: ")
    jumlah_barang = int(input("Jumlah Barang: "))
    total_harga = float(input("Harga: "))

    with open('transaksi.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, nama_barang, jumlah_barang, total_harga])

# Fungsi untuk menampilkan semua transaksi dari file CSV
def tampilkan_transaksi():
    with open('transaksi.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Fungsi untuk menghapus transaksi berdasarkan indeks dari file CSV
def hapus_transaksi(indeks):
    transaksi = []

    with open('transaksi.csv', mode='r') as file:
        reader = csv.reader(file)
        transaksi = list(reader)

    if indeks < 0 or indeks >= len(transaksi):
        print("Indeks transaksi tidak valid.")
        return

    transaksi.pop(indeks)

    with open('transaksi.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(transaksi)

    print("Transaksi telah dihapus.")

# Program utama
while True: #untuk terus menjalankan program sampai user memilih untuk keluar/exit
    print("\nMenu:")
    print("1. Tambah Transaksi")
    print("2. Tampilkan Transaksi")
    print("3. Hapus Transaksi")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        tambah_transaksi()
        print("Transaksi telah ditambahkan.")
    elif pilihan == '2':
        print("\nDaftar Transaksi:")
        tampilkan_transaksi()
    elif pilihan == '3':
        indeks = int(input("Masukkan indeks transaksi yang ingin dihapus: "))
        hapus_transaksi(indeks)
    elif pilihan == '4':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
