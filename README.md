# Pytest'te Dekoratörler

Dekoratörler testlerimizi özelleştirmemizi sağlayarak daha okunaklı ve anlaşılır hale getirmemize yardımcı olurlar.
En yaygın kullanılan Pytest dekoratörleri;

@pytest.fixture: Test fonksiyonlarının ihtiyaç duydukları bağımlılıkları ayarlamak için kullanılır. Örneğin, bir test fonksiyonunun bir veritabanı bağlantısına ihtiyacı varsa, bu bağımlılığı @pytest.fixture ile tanımlayabiliriz.

@pytest.mark.parametrize: Aynı test fonksiyonunu farklı parametrelerle çalıştırmak için kullanılır. Örneğin, bir fonksiyonun farklı giriş değerlerini test etmek istiyorsak, @pytest.mark.parametrize kullanarak bu değerleri belirleyebiliriz.

@pytest.mark.skip: Belirli bir testin çalıştırılmasını atlamak için kullanılır. Örneğin, bir test henüz tamamlanmadıysa veya hatalar içeriyorsa, bu testi atlamak için @pytest.mark.skip kullanabiliriz.

@pytest.mark.xfail: Bir testin başarısız olması beklenen durumlarda kullanılır. Örneğin, bir testin bir hata döndürmesi bekleniyorsa, bu testi @pytest.mark.xfail ile işaretleyebiliriz.

@pytest.mark.timeout: Bir testin belirli bir zaman sınırı içinde tamamlanmasını sağlar. Örneğin, bir testin 5 saniye içinde tamamlanması gerekiyorsa, @pytest.mark.timeout(5) kullanarak bu sınırı belirleyebiliriz.
