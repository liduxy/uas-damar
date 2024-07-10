def main():
    customers = {}

    while True:
        print("Pilih :")
        print("1. Tambah data pembelian customer")
        print("2. Lihat ranking customer terbaik")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan Anda (1/2/3): ")

        if pilihan == '1':
            nama_cust = input("Masukkan nama customer: ")
            if nama_cust not in customers:
                customers[nama_cust] = {
                    'otak_otak': [],
                    'tahu_bulat': [],
                    'sotong': []
                }

            otak_otak = float(input("Masukkan jumlah pembelian otak-otak: "))
            tahu_bulat = float(input("Masukkan jumlah pembelian tahu bulat: "))
            sotong = float(input("Masukkan jumlah pembelian sotong: "))

            customers[nama_cust]['otak_otak'].append(otak_otak)
            customers[nama_cust]['tahu_bulat'].append(tahu_bulat)
            customers[nama_cust]['sotong'].append(sotong)

        elif pilihan == '2':
            if not customers:
                print("Belum ada data customer.")
                continue

            peringkat_cust = sorted(customers.keys(), key=lambda customer: -rata2_pembelian(customers[customer]))
            print("\nRanking Customer Berdasarkan Rata-Rata Pembelian:")
            for rank, customer in enumerate(peringkat_cust, start=1):
                avg = rata2_pembelian(customers[customer])
                print(f"Rank {rank}: {customer} - Rata-Rata Pembelian: {avg}")

        elif pilihan == '3':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def rata2_pembelian(customer_data):
    total_otak2 = sum(customer_data['otak_otak'])
    total_tahubulat = sum(customer_data['tahu_bulat'])
    total_sotong = sum(customer_data['sotong'])
    return (total_otak2 + total_tahubulat + total_sotong) / 3

if __name__ == "__main__":
    main()
