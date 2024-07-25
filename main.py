import random

def guess_the_number():
  # Menentukan angka yang harus ditebak
  number_to_guess = random.randint(1, 100)
  attempts = 0
  max_attempts = 10

  print("Selamat datang di permainan Tebak Angka!")
  print("Saya telah memilih angka antara 1 dan 100. Coba tebak angka tersebut.")

  while attempts < max_attempts:
    try:
      guess = int(input("Masukkan tebakan Anda: "))
    except ValueError:
      print("Harap masukkan angka yang valid.")
      continue

    attempts += 1

    if guess < number_to_guess:
      print("Tebakan Anda terlalu rendah.")
    elif guess > number_to_guess:
      print("Tebakan Anda terlalu tinggi.")
    else:
      print(f"Selamat! Anda telah menebak angka dengan benar dalam {attempts} percobaan.")
      break
  else:
    print(f"Maaf, Anda telah mencapai batas percobaan. Angka yang benar adalah {number_to_guess}.")

guess_the_number()
