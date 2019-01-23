# format() metotu ile dilekçe örneği
# dosya olarak çıktı almayı sağlar. IDLE neredeyse oraya kaydediyor
dilekçe="""
                                                            Tarih: {}


T.C.
{} ÜNİVERSİTESİ
{} Fakültesi Dekanlığına


Fakültenizin {} Bölümü, {} numaralı öğrencisiyim. Ekte sunduğum belgede
belirtilen mazeretim gereğince {} Eğitim-Öğretim Yılı {}. yarıyılında
öğrenimime ara vermek istiyorum.


imza

İsim          : {}
Soyisim       : {}
T.C. Kimlik No: {}
Adres         : {}
Telefon       : {}
Ek Belgeler   : {}

"""

tarih        =input("Tarih: ")
universite   =input("Üniversite Adı: ")
fakulte      =input("Fakülte Adı: ")
bolum        =input("Bölüm Adı: ")
ogrenci_no   =input("Öğrenci No: ")
ogretim_yili =input("Öğretim Yılı: ")
yariyil      =input("Yarıyıl: ")
isim         =input("İsim: ")
soyisim      =input("Soyisim: ")
t_c_kimlik_no=input("T.C. Kimlik No: ")
adres        =input("Adres: ")
telefon      =input("Tel. No: ")
ek_belgeler  =input("Ek Belgeler: ")

dosya=open("dilekçe örnek.txt","w")
print(dilekçe.format(tarih,universite,fakulte,bolum,ogrenci_no,ogretim_yili,
                     yariyil,isim,soyisim,t_c_kimlik_no,
                     adres,telefon,ek_belgeler),file=dosya)
dosya.close()

