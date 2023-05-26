# Sorting Algorithms Visualized
Proje kapsamında

Sol panelde, kullanıcının sıralanacak listeyi manuel olarak girebilme veya boyutunu belirleyerek rasgele bir liste oluşturma seçeneği olmalıdır. Ayrıca, kullanıcının animasyon hızını ölçeklendirebilmesi mümkün olmalıdır. Sıralama algoritmaları olarak Seçme Sıralaması, Kabarcık Sıralaması, Ekleme Sıralaması, Birleştirme Sıralaması ve Hızlı Sıralama seçenekleri sunulmalıdır. Grafik tipleri olarak Dağılım, Sütun ve Kök grafikleri kullanılmalıdır. Ayrıca, oluştur, başla, dur ve sıfırla butonları bulunmalıdır. Oluştur butonuna basıldığında verilen liste değerleri ve grafik türüne göre arayüz oluşturulmalı, başla butonuna basıldığında animasyon belirtilen isterlere uygun olarak başlamalı, dur butonuna basıldığında animasyon durdurulmalı ve tekrar basıldığında animasyona devam etme seçeneği sunulmalı, sıfırla butonuna basıldığında liste temizlenmelidir.

Ana panelde, sol panelde yapılan seçimlere göre görsel bir arayüz sunulmalıdır. Seçilen algoritmanın sıralama işlemi gerçekleştirilirken, karşılaştırma adımlarını anlaşılır hale getirmek için renk kodları kullanılmalıdır. Karşılaştırılan değerler aynı renk kodunu paylaşmalı ve sıralanmış ve sıralanmamış değerler farklı renk kodlarıyla tanımlanmalıdır. Ayrıca, her adımda yapılan karşılaştırma sayısı arka planda tutulmalı ve animasyon üzerinde yapılan değişikliklere paralel olarak bu sayı artırılmalıdır. Belirli periyotlarla karşılaştırma sayısı güncellenerek ana panelde gösterilmelidir. Sıralama işlemi tamamlandığında, karşılaştırma sayısı ve algoritmanın karmaşıklık analizi sonucu ekrana yazdırılmalıdır.

Arayüzün Tasarlanması
Bu projede, PyQt5 kütüphanesini kullanarak bir GUI (Grafiksel Kullanıcı Arayüzü) tasarımını oluşturuldu. GUI, sıralama algoritmalarını görselleştirmek için gerekli bileşenleri içeriyor.

Tasarımın sol panelinde aşağıdaki bileşenler bulunuyor:
•	`QListWidget`: Liste elemanlarını göstermek için kullanılıyor.
•	`QComboBox`: Grafik türünü seçmek için bir açılır menü.
•	`QSlider`: Animasyon hızını ayarlamak için bir kaydırıcı.
•	`QPushButton`: "Shuffle" (Karıştır), "Start" (Başlat), "Stop" (Dur), "Reset" (Sıfırla) butonları.
Üst panelde ise sıralama algoritmalarını temsil eden beş düğme (`QPushButton`) bulunuyor: "Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort" ve "Quick Sort".
Ana panelde ise bir `QGraphicsView` yer alıyor. Bu bileşen, seçilen grafik türüne bağlı olarak sıralama işlemini görsel olarak göstermek için kullanılacak bir grafik görüntüleyici sağlıyor.
Tasarım, `QGridLayout` yöneticisi kullanılarak düzenleniyor. Bileşenler, ilgili konumlarına yerleştiriliyor. Tasarımın tamamlanmasının ardından `MainWindow` sınıfı oluşturuluyor ve `QApplication` ile başlatılıyor.

![image](https://github.com/Zeynep-gul/Sorting-Algorithms-Visualized/assets/56768123/9f55806f-f956-44c0-a6c8-0d783272a690)
