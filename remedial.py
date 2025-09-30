#python 3.7.1

print ("Hello, Dcoder!")

jenis = input("Masukkan jenis produk (Elektronik/Pakaian/Makanan/Kosmetik): ")
harga = int(input("Masukkan harga produk (dalam Rupiah): "))
penjualan = int(input("Masukkan jumlah produk terjual: "))

if jenis == "elektronik":
    kategori_jenis = "Elektronik"
elif jenis == "pakaian":
    kategori_jenis = "Pakaian"
elif jenis == "makanan":
    kategori_jenis = "Makanan"
elif jenis == "kosmetik":
    kategori_jenis = "Kosmetik"
else:
    kategori_jenis = "Jenis produk tidak dikenali"

if harga > 100000:
    kategori_harga = "Premium"
elif harga >= 50000:
    kategori_harga = "Menengah"
else:
    kategori_harga = "Terjangkau"

if penjualan >= 100:
    kategori_penjualan = "Best Seller"
elif penjualan >= 50:
    kategori_penjualan = "Populer"
else:
    kategori_penjualan = "Normal"

print("\n=== Hasil Kategori Produk ===")
print(f"Kategori Jenis     : {kategori_jenis}")
print(f"Kategori Harga     : {kategori_harga}")
print(f"Kategori Penjualan : {kategori_penjualan}")