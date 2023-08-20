""" Return ifadesi Python'da bir fonksiyonun 
çalışmasını sonlandırarak belirli bir değeri veya 
sonucu döndürmek için kullanılır."""
"""Aşağıdaki örnekte, kalanıbul adında bir fonksiyon
tanımlanmıştır. Bu fonksiyon, bölünen sayısının 
bölen sayısına bölümünden kalanı hesaplar ve bu 
kalan değerini return ifadesiyle döndürür.
Daha sonra bu fonksiyon çağrılarak hesaplanan 
kalan değeri alınır ve ekrana yazdırılır."""

def kalanıbul (bölünen, bölen):
    return bölünen % bölen
sayı1 = 17
sayı2 = 4
kalan = kalanıbul(sayı1, sayı2)
print(f"{sayı1} sayısının {sayı2} ile bölümünde kalan:{kalan}")

