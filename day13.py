jumlah_data = int(input("masukkan jumlah data:"))
data_ke = 0
for i in range(1,jumlah_data+1):
    nilai = int(input("masukkan nilai ke-%d :" %i))
    data_ke += nilai
    rata2 = data_ke/jumlah_data

print("rata-ratanya adalah : {}". format(round(rata2)))
    
    
