def evaluate_treasure(input_string):
    # Inisialisasi nilai harta karun awal
    treasure_value = 0
    
    # Iterasi melalui setiap karakter dalam string input
    for char in input_string:
        if char == '$':
            treasure_value += 100
        elif char == 'x':
            # Jika treasure hunter terjatuh ke laut dan nilai harta karun kurang dari 10
            if treasure_value < 10:
                treasure_value = 0
            else:
                treasure_value -= 10
        elif char == '#':
            # Jika treasure hunter terjatuh ke jurang dan nilai harta karun tidak 0
            if treasure_value > 0:
                treasure_value /= 2
    
    return int(treasure_value)

# Input string dari treasure hunter
input_string = input("Masukkan string perjalanan treasure hunter: ")

# Memanggil fungsi evaluate_treasure untuk menghitung nilai harta karun
result = evaluate_treasure(input_string)

# Menampilkan hasil
print(f"Nilai harta karun yang ditemukan: {result}")
