""" "Class" anahtar kelimesi Python'da nesne yönelimli 
programlamayı (OOP) desteklemek için kullanılır."""
""" Aşağıdaki örnekte, "Ögrenci" adında bir sınıf 
(class) tanımlanmıştır. Bu sınıf, öğrenci nesnelerinin 
ad, soyad ve numara bilgilerini içeren özelliklere 
(attributes) ve "bilgileri göster" adında bir metoda 
(method) sahiptir."""

"""__init__: Bu özel bir metod olup sınıfın yapıcı 
(constructor) metodu olarak adlandırılır."""
""" self: Bu, sınıf içindeki bir metodun kendisini 
temsil eden bir referanstır."""
"""bilgileri göster: Sınıf içinde tanımlanan bir 
metoddur. Öğrenci bilgilerini ekrana yazdırır. """
class Ögrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara

    def bilgileri_göster(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad}, Numara: {self.numara}")

# Sınıfı kullanma
ögrenci1 = Ögrenci("Ahmet", "Yılmaz", "12345")
ögrenci2 = Ögrenci("Ayşe", "Demir", "67890")

ögrenci1.bilgileri_göster()
ögrenci2.bilgileri_göster()


