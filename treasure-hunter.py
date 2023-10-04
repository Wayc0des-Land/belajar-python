# Mendefinisikan fungsi evaluate_treasure untuk menghitung nilai harta karun
def evaluate_treasure(input_string):
    # Inisialisasi nilai harta karun awal
    treasure_value = 0
    
    # Iterasi melalui setiap karakter dalam string input
    for char in input_string:
        if char == '$':
            # Jika karakter adalah '$', tambahkan 100 ke nilai harta karun
            treasure_value += 100
        elif char == 'x':
            # Jika karakter adalah 'x'
            # - Jika nilai harta karun kurang dari 10, setel nilai harta karun menjadi 0
            # - Jika nilai harta karun lebih besar atau sama dengan 10, kurangkan 10 dari nilai harta karun
            if treasure_value < 10:
                treasure_value = 0
            else:
                treasure_value -= 10
        elif char == '#':
            # Jika karakter adalah '#'
            # - Jika nilai harta karun lebih besar dari 0, kurangi nilai harta karun menjadi setengah
            if treasure_value > 0:
                treasure_value /= 2
    
    return treasure_value

# Input string dari treasure hunter
input_string = input("Masukkan string perjalanan treasure hunter: ")

# Memanggil fungsi evaluate_treasure untuk menghitung nilai harta karun
result = evaluate_treasure(input_string)

# Menampilkan hasil
print(f"Nilai harta karun yang ditemukan: {result}")
