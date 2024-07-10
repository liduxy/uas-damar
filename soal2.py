def main():
    total_pemasukan = 0
    total_pengeluaran = 0

    while True:
        print("Pilih transaksi:")
        print("1. Pemasukan")
        print("2. Pengeluaran")
        pilihan = input("Masukkan pilihan Anda (1/2): ")

        if pilihan == '1':
            print("-"*70)
            nama_pemberi = input("Masukkan nama pemberi: ")
            nominal_pemasukan = float(input("Masukkan nominal pemasukan: "))
            total_pemasukan += nominal_pemasukan
            print(f"Total pemasukan: {total_pemasukan}")

            lanjut_pengeluaran = input("Apakah ada pengeluaran? (y/t): ")
            if lanjut_pengeluaran.lower() == 'y':
                nama_pengeluaran = input("Masukkan nama pengeluaran untuk: ")
                nominal_pengeluaran = float(input("Masukkan nominal pengeluaran: "))
                total_pengeluaran += nominal_pengeluaran
                print(f"Sisa kas: {total_pemasukan - total_pengeluaran}")

        elif pilihan == '2':
            print("-"*70)
            nama_pengeluaran = input("Masukkan nama pengeluaran untuk: ")
            nominal_pengeluaran = float(input("Masukkan nominal pengeluaran: "))
            total_pengeluaran += nominal_pengeluaran
            print(f"Sisa kas: {total_pemasukan - total_pengeluaran}")

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

        lanjut_transaksi = input("Apakah Anda ingin melanjutkan transaksi? (y/t): ")
        if lanjut_transaksi.lower() != 'y':
            print("Transaksi selesai.")
            break

if __name__ == "__main__":
    main()
