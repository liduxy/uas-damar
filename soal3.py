def konsuhu():
    skala = {
        "1": 'Fahrenheit',
        "2": 'Kelvin',
        "3": 'Reamur',
        "4": 'Semua skala'
    }
    
    while True:
        print("-"*15,"MENU","-"*15)
        print("Pilih skala konversikan celcius ke :")
        
        for no, i in skala.items():
            print(f"{no}. {i}")
        print("5. Keluar")
        
        pil = input("Masukkan pilih Anda (1/2/3/4/5): ")
        print("-"*35)

        if pil == "5":
            break
        if pil in skala:
            suhu = float(input("Masukkan suhu dalam Celsius: "))
            if pil == "1":
                suhukon = suhu * 9/5 + 32
                print(f"Suhu dalam {skala[pil]}: {suhukon}")
            elif pil == "2":
                suhukon = suhu + 273.15
                print(f"Suhu dalam {skala[pil]}: {suhukon}")
            elif pil == "3":
                suhukon = suhu * 4/5
                print(f"Suhu dalam {skala[pil]}: {suhukon}")
            elif pil == "4":
                fahrenheit = suhu * 9/5 + 32
                kelvin = suhu + 273.15
                reamur = suhu * 4/5
                print(f"Suhu dalam Fahrenheit: {fahrenheit}")
                print(f"Suhu dalam Kelvin: {kelvin}")
                print(f"Suhu dalam Reamur: {reamur}")

            tanya_keluar = input("\nApakah Anda ingin keluar? (y/t): ").lower()
            if tanya_keluar == 'y':
                break
        else:
            print("Error: Skala tidak didukung. Silakan coba lagi.")

konsuhu()
