import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Rastgele veri oluşturma
veri = {'Öğrenci': ['Ahmet', 'Ayşe', 'Mehmet', 'Zeynep'],
'Not': [85, 90, 78, 95]}
df = pd.DataFrame(veri)
# Veriyi görüntüleme
print(df)
# Notların ortalaması
ortalama = np.mean(df['Not'])
print("Not Ortalaması:", ortalama)
# Sütun grafiği çizdirme
plt.bar(df['Öğrenci'], df['Not'])
plt.xlabel('Öğrenci')
plt.ylabel('Not')
plt.title('Öğrenci Notları')
plt.show()
""" Veri görselleştirme, verileri grafik, tablo, 
harita veya benzeri görsel öğelerle temsil ederek 
daha anlamlı ve anlaşılabilir hale getirme sürecidir. 
Görselleştirme, karmaşık veri setlerini daha 
erişilebilir hale getirir, desenleri vurgular ve 
genel bir bakış açısı sunar. İyi tasarlanmış grafikler 
ve görseller, veri analiz sonuçlarını daha kolay 
yorumlama ve iletişim kurma amacıyla kullanılır. """
