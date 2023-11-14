import csv
import time

def register():
    # Get username
    username = input("Masukkan username yang ingin didaftarkan: ")

    # Open CSV file for writing
    file2 = open("login_database.csv", 'a', newline="")
    writer = csv.writer(file2)

    # Display loading message
    print('\n', 'Loading...', '\n')

    # Wait for 5 seconds
    for seconds in range(5, 0, -1):
        time.sleep(1)

    print('======Username telah terdaftar======')

    while True:
        # Get password and ensure it meets criteria
        password = input("Buat password (harus mengandung satu angka, satu huruf kapital, dan satu simbol): ")

        if password == "":
            print("Password tidak boleh kosong.")
        elif len(password) >= 8 and any(char.isdigit() for char in password) \
                and any(char.isupper() for char in password) and any(not char.isalnum() for char in password):
            # Password meets criteria
            print('\n', f'Akun telah terdaftar. Selamat datang {username}', '\n')
            writer.writerow([username, password])
            file2.close()
            break
        else:
            print('Password tidak aman.')

# Call the register function
register()
