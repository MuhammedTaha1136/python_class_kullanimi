# class nedir?
#class diğer adıyla sınıf, Sınıfın herhangi bir nesnesini karakterize eden bir özellik kümesi tanımlayan bir nesne için 
#kullanıcı tanımlı bir prototiptir. Sınıf özellikleri üyelere, değişkenlere ve metotlara sahiptir.

#class(sınıf) nasıl oluşturulur?

#class sınıf_adı :
    # değişken  
    # değişken2

    #def methot_adi(self):
        #print(self.değişken)
        #print(self.değişken2)
    # ekrana yazdırmak için self komutunu kullanıyoruz.

# örnek bir araba sınıfı oluşturalım.

class Araba :
    marka = "FORD"
    model = "FOCUS"
    motor = "1.5"
    renk = "FÜME"
    print("Araba Oluşturuldu !!")
    
    def araba_yazdır(self):
        print(self.marka)
        print(self.model)
        print(self.motor)
        print(self.renk)

araba = Araba()
print("Marka : " + araba.marka)
print("Model : " + araba.model)
print("Motor : " + araba.motor)
print("Renk  : " + araba.renk)













