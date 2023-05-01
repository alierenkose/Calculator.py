güzel = "-------------------------------------------------"

while True:
 print("Hesap Makinesi(hm) , Üs Bulma(üb) , Asal Mı(as) , Köşegen Bulma(kb) , Ortalama Bul(ob) , Kök Hesaplayıcı(kh)")
 hesaptürüü = input("Bunlardan Hangisi: ")
 hesaptürü = hesaptürüü.lower()
 if hesaptürü not in ["hm", "üb", "as", "kb", "ob", "kh"]:
   print("Hatalı işlem türü seçtiniz.")
   exit()
 if hesaptürü == "hm":


  islem_turu = input("Hangi işlemi yapmak istiyorsunuz? (+, -, *, /): ")
  if islem_turu not in ["+", "-", "*", "/"]:
    print("Hatalı işlem türü seçtiniz.")
    exit()

  toplanacak_sayi_sayisi = int(input("Kaç sayıyı işleme dahil etmek istiyorsunuz? "))

  sayilar = []
  for i in range(toplanacak_sayi_sayisi):
    print (güzel)
    sayi = float(input(f"\n{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

  if islem_turu == "+":
    sonuc = sum(sayilar)
  elif islem_turu == "-":
    sonuc = sayilar[0] - sum(sayilar[1:])
  elif islem_turu == "*":
    sonuc = 1
    for sayi in sayilar:
      sonuc *= sayi
  else:
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
      sonuc /= sayi
  print(güzel)
  print(f"{toplanacak_sayi_sayisi} sayının {islem_turu} işlemi sonucu: ", sonuc)
 elif hesaptürü == "üb":

   üslü_sayı = float(input("Sayıyı Girin: "))
   print(güzel)
   üslü_üs = int(input("Üssü Girin: "))
   print(güzel)
   üslü_sonuç = üslü_sayı ** üslü_üs
   print(f"{üslü_sayı} üssü {üslü_üs} işleminin cevabı {üslü_sonuç}")
 elif hesaptürü == "as":

   a_s = int(input("Sayıyı Girin: "))
   print(güzel)
   if a_s > 1:
     for i in range(2,a_s):
       if (a_s % i) == 0:
         print(a_s," Asal Sayı Değil")
         break
     else:
       print(a_s," Asal Sayı")
   else:
     print(a_s," Asal Sayı Değil")
 elif hesaptürü == "kb":

  köşe_sayısı = int(input("Cisimde kaç kenar var: "))
  print(güzel)
  sonucköşe = köşe_sayısı * (köşe_sayısı - 3) / 2
  print(sonucköşe)
 elif hesaptürü == "ob":
  ortalama_kaç_sayı = int(input("Kaç Tane Sayı Girceksin: "))
  ao_toplam = 0
  for i in range(ortalama_kaç_sayı):
   ao_sayı = float(input("{}. sayıyı girin: ".format(i + 1)))
   ao_toplam += ao_sayı
  ao_ortalama = ao_toplam / ortalama_kaç_sayı
  print("Girdiğiniz sayıların aritmetik ortalaması: ", ao_ortalama)
 elif hesaptürü == "kh":
  kök_sayi = float(input("Köklü ifadeyi hesaplamak istediğiniz sayıyı girin: "))
  kok_derecesi = int(input("Kök derecesini girin (örneğin, 2 for karekök, 3 for küpkök): "))
  print(güzel)
  sonuc = kök_sayi ** (1 / kok_derecesi)
  print(f"Girilen sayının {kok_derecesi}. dereceden kökü: {sonuc}")
 print("")
 print("TEKRAR BAŞLATILIYOR.....")
 print("")