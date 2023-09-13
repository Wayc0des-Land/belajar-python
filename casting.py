# Membuat variable 'ini_string' dengan angka 1 sampai 10 dalam bentuk string
ini_string = '1 2 3 4 5 6 7 8 9 10'

# Melakukan casting 'ini_string' ke integer dengan memisahkan angka-angka menggunakan split() dan map()
casting_ke_integer = list(map(int, ini_string.split()))

# Menampilkan nilai 'casting_ke_integer' yang sekarang berbentuk list
print(casting_ke_integer)