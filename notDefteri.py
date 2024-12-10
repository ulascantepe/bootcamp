import datetime  

class NotDefteri:  
    def __init__(self):  
        self.notlar = []  

    def not_ekle(self, not_text):  
        tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        self.notlar.append((tarih, not_text))  
        print("Not eklendi.")  

    def not_goruntule(self):  
        if not self.notlar:  
            print("Hiç not yok.")  
        else:  
            for index, (tarih, not_text) in enumerate(self.notlar, start=1):  
                print(f"{index}. [{tarih}] {not_text}")  

    def not_guncelle(self, not_numara, yeni_not):  
        if 1 <= not_numara <= len(self.notlar):  
            tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
            self.notlar[not_numara - 1] = (tarih, yeni_not)  
            print("Not güncellendi.")  
        else:  
            print("Geçersiz not numarası.")  

    def not_sil(self, not_numara):  
        if 1 <= not_numara <= len(self.notlar):  
            silinen_not = self.notlar.pop(not_numara - 1)  
            print(f"'{silinen_not[1]}' notu silindi.")  
        else:  
            print("Geçersiz not numarası.")  

    def notlari_yazdir(self, dosya_adi):  
        with open(dosya_adi, 'w', encoding='utf-8') as dosya:  
            for tarih, not_text in self.notlar:  
                dosya.write(f"[{tarih}] {not_text}\n")  
        print(f"Tüm notlar '{dosya_adi}' dosyasına kaydedildi.")  

    def notlardan_yukle(self, dosya_adi):  
        try:  
            with open(dosya_adi, 'r', encoding='utf-8') as dosya:  
                self.notlar = []  
                for line in dosya:  
                    # Satırı tarih ve not metni olarak ayır  
                    tarih, not_text = line.split(']', 1)  
                    tarih = tarih.strip('[')  # `[` karakterini temizle  
                    not_text = not_text.strip()  
                    self.notlar.append((tarih, not_text))  
            print(f"Güncellenmiş notlar '{dosya_adi}' dosyasından yüklendi.")  
        except FileNotFoundError:  
            print(f"{dosya_adi} bulunamadı.")  
        except Exception as e:  
            print(f"Hata: {e}")  



def main():  
    not_defteri = NotDefteri()  

    while True:  
        print("\nNot Defteri İşlemleri:")  
        print("1. Not Ekle")  
        print("2. Not Görüntüle")  
        print("3. Not Güncelle")  
        print("4. Not Sil")  
        print("5. Notları TXT'ye Kaydet")  
        print("6. Notları TXT'den Yükle")  
        print("7. Çıkış")  

        secenek = input("Bir seçenek girin (1-7): ")  

        if secenek == "1":  
            not_text = input("Eklenecek notu girin: ")  
            not_defteri.not_ekle(not_text)  
        elif secenek == "2":  
            not_defteri.not_goruntule()  
        elif secenek == "3":  
            not_defteri.not_goruntule()  
            not_numara = int(input("Güncellenmek istenen not numarasını girin: "))  
            yeni_not = input("Yeni not metnini girin: ")  
            not_defteri.not_guncelle(not_numara, yeni_not)  
        elif secenek == "4":  
            not_defteri.not_goruntule()  
            not_numara = int(input("Silinmek istenen not numarasını girin: "))  
            not_defteri.not_sil(not_numara)  
        elif secenek == "5":  
            dosya_adi = input("Notları kaydedecek dosya adını girin (örn. notlar.txt): ")  
            not_defteri.notlari_yazdir(dosya_adi)  
        elif secenek == "6":  
            dosya_adi = input("Notları yükleyecek dosya adını girin (örn. notlar.txt): ")  
            not_defteri.notlardan_yukle(dosya_adi)  
        elif secenek == "7":  
            print("Çıkış yapılıyor...")  
            break  
        else:  
            print("Geçersiz seçim, lütfen tekrar deneyin.")  
