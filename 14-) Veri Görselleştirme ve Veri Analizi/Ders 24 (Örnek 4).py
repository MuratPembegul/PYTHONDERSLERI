import pandas as pd
# Örnek veri oluşturma (CSV formatında)
data = {'Öğrenci': ['Ali', 'Veli', 'Ayşe', 'Mehmet', 'Zeynep'],
    'Sınıf': [9, 10, 9, 11, 10],
    'Not': [85, 78, 92, 65, 88]}
# Veriyi Pandas DataFrame'e dönüştürme
df = pd.DataFrame(data)
# Veri analizi
print("Veri Seti:")
print(df)
# Ortalama not hesaplama
ortalama_not = df['Not'].mean()
print("\nOrtalama Not:", ortalama_not)
# En yüksek notu alan öğrenci
en_yuksek_not = df[df['Not'] == df['Not'].max()]
print("\nEn Yüksek Notu Alan Öğrenci:")
print(en_yuksek_not)
