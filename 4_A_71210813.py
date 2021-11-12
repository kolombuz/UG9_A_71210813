#Program catatan pemesanan dan penghitung pengeluaran pelanggan
#Dengan inputan
print("")
print("Test case 1")
print ("=====MASUKKAN JUMLAH MAKANAN YANG DIPESAN=====")
IKAN  = int(input('IKAN BAKAR       RP 25.000,00   : '))
ES = int(input('ES DOGER         RP 6.000,00    : '))
RUJAK = int(input('RUJAK CINGUR     RP 8.000,00    : '))

MENU1 = 25000 * IKAN
MENU2 = 6000 * ES
MENU3 = 8000 * RUJAK
JUMLAH = MENU1 + MENU2 + MENU3

print ("=====TOTAL=====")
print(f'TOTAL IKAN BAKAR                : {MENU1}')
print(f'TOTAL ES DOGER                  : {MENU2}')
print(f'TOTAL RUJAK CINGUR              : {MENU3}')
print(f'Jumlah total biaya yang harus dibayar adalah {JUMLAH}')
print("")
print("Test case 2")
print ("=====MASUKKAN JUMLAH MAKANAN YANG DIPESAN=====")
IKAN  = int(input('IKAN BAKAR       RP 25.000,00   : '))
ES = int(input('ES DOGER         RP 6.000,00    : '))
RUJAK = int(input('RUJAK CINGUR     RP 8.000,00    : '))

MENU1 = 25000 * IKAN
MENU2 = 6000 * ES
MENU3 = 8000 * RUJAK
JUMLAH = MENU1 + MENU2 + MENU3

print ("=====TOTAL=====")
print(f'TOTAL IKAN BAKAR                : {MENU1}')
print(f'TOTAL ES DOGER                  : {MENU2}')
print(f'TOTAL RUJAK CINGUR              : {MENU3}')
print(f'Jumlah total biaya yang harus dibayar adalah {JUMLAH}')
