""" Python'da dosya, verilerin kalıcı 
olarak saklandığı bir depolama birimidir. 
Dosyalar, metin, resim, ses, veritabanı vb. 
türlerde verileri içerebilir."""
# Dosya oluşturma
# With dosyayı otomatik olarak kapatır ve yerleşik
# bir ifadedir.
with open("yeni dosya.txt", "w") as dosya:
    dosya.write("Bu bir yeni dosyadir.")
# Diğer yöntem
dosya = open ("dosya.txt", "w")
dosya.write("Bu bir dosyadır.")
dosya.close()




