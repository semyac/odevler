# 8 Mart Ödev 1. Kısım

# Pyton Veri Tipleri
#   Metinsel Veri Tipi (Text)
#       String: Uygulamada yer alan metinsel ifadelerin içerisinde tutulduğu değişkenlerdir. ‘…’  , “…” , str().

#   Sayısal Veri Tipleri (Numeric)
#       Integer: Sınırsız uzunluktaki pozitif veya negatif tamsayı ifadelerin içerisinde tutulduğu değişkenlerdir. int()
#       Float: Ondalıklı pozitif veya negatif sayı ifadelerinin içerisinde tutulduğu veri tipidir. float()
#       Complex: İleri düzey matematiksel işlemlerde (karmaşık sayılar gibi) ifadelerin tutulduğu değişkenlerdir. complex(5+0j)

#   Sıralama Veri Tipleri (Sequence)
#       List: Köşeli parantez içerisinde tanımlanan [..] , içerisinde farklı veri türlerini tutabilen, liste içerisindeki elemanların düzenlenip değiştirilebildiği sıralı veri tipleridir. Elemanlarına index yardımıyla ulaşılabilir (sıralı olduğu için). list()
#       Tuple: Parantezler içerisinde tanımlanan (...), içerisinde yer alan elemanlarına index yardımıyla ulaşılabilindiği fakat değiştirilemediği sıralı veri tipleridir. tuple()
#       Range: Belirtilen belirli bir aralıktaki sayıları tutan veri tipidir. range()

#   Haritalama Veri Tipi (Mapping)
#       Dictionary: {...} içerisinde tanımlanan, verilerin anahtar kelime ve değer ilişkisi şeklinde tutulduğu türdür. İçerisinde her tip veri saklanabilir ve bu elemanlar değiştirilebilir.

#   Küme Veri Tipleri (Set)
#       Set: {...} içerisinde tanımlanırlar, ancak anahtar kelime-değer gibi ikili ilişkiler barındırmazlar. Farklı veri türlerini bulundurabilir, elemanları değiştirilebilen fakat index yardımıyla ulaşılamayan(sırasız) veri tipleridir.
#       FrozenSet: Set veri tipinden tek farkı elemanlarının değiştirilemiyor olmasıdır.

#   Boolean Veri Tipi
#       Bool: Bu yapı içerisinde tutulan ifadeler doğru veya yanlış (True/False) şeklinde iki değer alabilirler. bool()

#   İkili Veri Tipleri (Binary)
#       Bytes: Bir değişkeni byte nesnesine dönüştürerek tutar. Değişkenin değerini değiştirmez. bytes()
#       Bytesarray: Bytes ile benzer mantıkdadır, ancak değişkenin sunduğu değer farklılaşabilir. bytesarray()
#       Memoryview: Bellek görüntüleme nesnesi oluşturularak yapılan veri tutma işlemidir böylece arabellek protokolüne güvenli erişim sağlanır.

# 8 Mart Ödev 2. Kısım
# 	Veri tiplerinin kodlama.io sitesinde yer alan örnekleri:
# 		String: “Kurslarım, Tüm Kurslar, Giriş Yap, Kaydol, Eğitmen, vb.”
# 		Integer: Kurs tamamlama yüzdeleri
# 		Bool: Giriş Yap alanındaki kullanıcı adı ve şifre kombinasyonları bu veri tipiyle tutulur.





# 8 Mart Ödev 3. Kısım
# Siteye giriş yap şart blokları kullanılmıştır.

#Kullanıcı Adı:Pyton Şifre:2023

kullaniciAdi=input("Kullanıcı adınızı giriniz.")
sifre=input("Şifrenizi giriniz.")

kullaniciAdi="PySelenium" 
sifre=2023

if kullaniciAdi=="PySelenium" and sifre==2023:
    print("Giriş Başarılı")

else:
    print("Hatalı Kullanıcı Adı veya Şifre")