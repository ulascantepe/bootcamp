class BankaHesabi:  
    def __init__(self, hesap_sahibi):  
        self.hesap_sahibi = hesap_sahibi  
        self.bakiye = 0.0  

    def parayatir(self, miktar):  
        if miktar > 0:  
            self.bakiye += miktar  
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")  
        else:  
            print("Yatırılacak miktar sıfırdan büyük olmalıdır.")  

    def paracek(self, miktar):  
        if miktar > 0:  
            if miktar <= self.bakiye:  
                self.bakiye -= miktar  
                print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")  
            else:  
                print("Yetersiz bakiye.")  
        else:  
            print("Çekilecek miktar sıfırdan büyük olmalıdır.")  

    def hesap_bakiyesi(self):  
        print(f"{self.hesap_sahibi} için hesap bakiyesi: {self.bakiye} TL")  



 
hesap_adi = input("Hesap sahibi adını girin: ")  
hesap = BankaHesabi(hesap_adi)  

while True:  
    print("\nİşlemler:")  
    print("1. Para Yatır")  
    print("2. Para Çek")  
    print("3. Hesap Bakiyesi Görüntüle")  
    print("4. Çıkış")  
    
    secenek = input("Bir seçenek girin (1-4): ")  

    if secenek == "1":  
        miktar = float(input("Yatırmak istediğiniz miktarı girin (Simge kullanmayın sadece sayı): "))  
        hesap.parayatir(miktar)  
    elif secenek == "2":  
        miktar = float(input("Çekmek istediğiniz miktarı girin (Simge kullanmayın sadece sayı): "))  
        hesap.paracek(miktar)  
    elif secenek == "3":  
        hesap.hesap_bakiyesi()  
    elif secenek == "4":  
        print("Çıkış yapılıyor...")  
        break  
    else:  
        print("Geçersiz seçim, lütfen tekrar deneyin.")
