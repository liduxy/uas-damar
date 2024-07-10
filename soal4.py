import math
    
def main():
    print("---------------------KALKULATOR------------------")
    angka_pertama = float(input("Masukkan Angka Pertama: "))
    operator = input("Masukkan Operator (*, /, +, -, %, ^, V, sin, cos, tan, lingkaran, kubus): ")
    hasil = 0.0
    print("-"*70)
    if operator == "*":
        angka_kedua = float(input("Masukkan Angka Kedua: "))
        hasil = angka_pertama * angka_kedua
    elif operator == "/":
        angka_kedua = float(input("Masukkan Angka Kedua: "))
        hasil = angka_pertama / angka_kedua
    elif operator == "+":
        angka_kedua = float(input("Masukkan Angka Kedua: "))
        hasil = angka_pertama + angka_kedua
    elif operator == "-":
        angka_kedua = float(input("Masukkan Angka Kedua: "))
        hasil = angka_pertama - angka_kedua
    elif operator == "%":
        angka_kedua = float(input("Masukkan Angka Kedua: "))
        hasil = angka_pertama % angka_kedua
    elif operator == "^":
        hasil = math.pow(angka_pertama, 2)
    elif operator == "V":
        hasil = math.sqrt(angka_pertama)
    elif operator.lower() == "sin":
        hasil = math.sin(math.radians(angka_pertama))
    elif operator.lower() == "cos":
        hasil = math.cos(math.radians(angka_pertama))
    elif operator.lower() == "tan":
        hasil = math.tan(math.radians(angka_pertama))
    elif operator.lower() == "lingkaran":
        luas_lingkaran = math.pi * math.pow(angka_pertama, 2)
        volume_bola = (4 / 3) * math.pi * math.pow(angka_pertama, 3)
        print(f"Luas Lingkaran = {luas_lingkaran}")
        print(f"Volume Bola = {volume_bola}")
        return
    elif operator.lower() == "kubus":
        luas_persegi = math.pow(angka_pertama, 2)
        volume_kubus = math.pow(angka_pertama, 3)
        print(f"Luas Persegi = {luas_persegi}")
        print(f"Volume Kubus = {volume_kubus}")
        return
    else:
        print("E R R O R!")
        return

    print(f"Hasilnya: {hasil}")

if __name__ == "__main__":
    main()