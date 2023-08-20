import matplotlib.pyplot as plt
# Tarih ve kapanış fiyatları
dates = ['2023-08-19', '2023-08-20', '2023-08-21', '2023-08-22']
closing_prices = [7800, 7700, 7600, 7500]
# Konya Çimento hisse senedi verileri
konya_dates = ['2023-08-19', '2023-08-20', '2023-08-21', '2023-08-22']
konya_closing_prices = [4500, 4700, 5100, 5800]
# Kapanış fiyatlarını çizgi grafiği olarak gösterme
plt.figure(figsize=(10, 6))
plt.plot(dates, closing_prices, marker='o', label='Bist 100')
plt.plot(konya_dates, konya_closing_prices, marker='o', label='Konya Çimento Hisse Senedi')
plt.title('Hisse Senedi Kapanış Fiyatları')
plt.xlabel('Tarih')
plt.ylabel('Kapanış Fiyatı')
plt.xticks(rotation=45)
plt.legend()
plt.show()
