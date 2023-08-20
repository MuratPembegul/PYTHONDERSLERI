# Veri tabanı kütüphanesini içe aktarma
import sqlite3
# Veri tabanı dosyası oluşturma
with sqlite3.connect("öğrenciler.db") as bağlantı:
    cursor = bağlantı.cursor()
# Veri tabanı tablosu oluşturma
    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    öğrenciler(id INTEGER PRIMARY KEY, ad TEXT, soyad 
    TEXT, numara TEXT)""")
# Veri tabanına veri ekleme
    cursor.execute("INSERT INTO öğrenciler (ad, soyad, numara) VALUES (?, ?, ?)", 
    ("Ahmet", "Yılmaz", "12345"))
# Veri tabanını sorgular ve ekrana yazdırır 
    cursor.execute("SELECT * FROM öğrenciler")
    öğrenciler = cursor.fetchall()
    for öğrenci in öğrenciler:
        print(öğrenci)
