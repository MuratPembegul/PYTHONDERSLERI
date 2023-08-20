import numpy as np
# 10 elemanlı rastgele bir dizi oluşturma
dizi = np.random.rand(10)
print("Oluşturulan Dizi:")
print(dizi)
# Dizinin ortalamasını hesaplama
ortalama = np.mean(dizi)
print("\nDizi Ortalaması:", ortalama)
# Dizinin standart sapmasını hesaplama
standart_sapma = np.std(dizi)
print("Dizi Standart Sapması:", standart_sapma)
# Dizinin en büyük ve en küçük elemanlarını bulma
en_buyuk = np.max(dizi)
en_kucuk = np.min(dizi)
print("En Büyük Değer:", en_buyuk)
print("En Küçük Değer:", en_kucuk)
""" Veri analizi, toplanan veya mevcut verileri 
inceleyerek desenleri, eğilimleri ve ilişkileri 
anlamak amacıyla gerçekleştirilen süreçtir. 
Bu süreç, verileri temizlemeyi, dönüştürmeyi ve 
özetlemeyi içerir. Veri analizi, istatistiksel 
yöntemler, olasılık dağılımları ve veri madenciliği 
teknikleri kullanarak verilerdeki anlamlı bilgileri 
ortaya çıkarır. Bu aşama, kararlar almak ve 
hipotezleri test etmek için veriye dayalı argümanlar 
geliştirmek için temel bilgi sağlar. """