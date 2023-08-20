# Try (tri) except (eksıpt) finally (faynali)
""" Bu örnekte, kullanıcıdan bir sayı girmesi istenir 
ve girilen sayının karesi hesaplanarak ekrana 
yazdırılır. Eğer kullanıcı geçerli bir sayı girmeyi 
unutursa veya başka bir hata olursa, ilgili except 
bloğu çalışır ve hata mesajı görüntülenir. 
Son olarak, finally bloğu her durumda çalışarak 
işlem tamamlandığını belirtir."""
try:
    sayı = int(input("Bir sayı girin: "))
    kare = sayı ** 2
    print(f"{sayı}'nin karesi: {kare}")
except ValueError:
    print("Hata: Geçerli bir sayı girilmedi.")
finally:
    print("İşlem tamamlandı.")
    