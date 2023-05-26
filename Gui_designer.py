from PyQt5 import QtWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Sol Panel bileşenleri
        self.list_widget = QtWidgets.QListWidget(self)
        
        self.combo_box = QtWidgets.QComboBox(self)
        self.combo_box.addItem("Grafik Türü Seçiniz")
        self.combo_box.addItem("Kök (Stem) Grafiği")
        self.combo_box.addItem("Sütun (Bar) Grafiği")
        self.combo_box.addItem("Dağılım (Scatter) Grafiği")

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.shuffle_button = QtWidgets.QPushButton("Shuffle", self)
        self.start_button = QtWidgets.QPushButton("Start", self)
        self.pause_button = QtWidgets.QPushButton("Stop", self)
        self.reset_button = QtWidgets.QPushButton("Reset", self)
        
        # Üst Panel bileşenleri
        self.selection_button = QtWidgets.QPushButton("Selection Sort", self)
        self.bubble_button = QtWidgets.QPushButton("Bubble Sort", self)
        self.insertion_button = QtWidgets.QPushButton("Insertion Sort", self)
        self.merge_button = QtWidgets.QPushButton("Merge Sort", self)
        self.quick_button = QtWidgets.QPushButton("Quick Sort", self)
        
        # Ana Panel bileşenleri
        self.graphics_view = QtWidgets.QGraphicsView(self)
        
        # Tasarımın yerleşimi
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.list_widget, 0, 0, 1, 2)
        layout.addWidget(self.combo_box, 1, 0, 1, 2)
        layout.addWidget(self.slider, 2, 0, 1, 2)
        layout.addWidget(self.shuffle_button, 3, 0, 1, 1)
        layout.addWidget(self.start_button, 3, 1, 1, 1)
        layout.addWidget(self.pause_button, 4, 0, 1, 1)
        layout.addWidget(self.reset_button, 4, 1, 1, 1)
        layout.addWidget(self.selection_button, 0, 2, 1, 1)
        layout.addWidget(self.bubble_button, 1, 2, 1, 1)
        layout.addWidget(self.insertion_button, 2, 2, 1, 1)
        layout.addWidget(self.merge_button, 3, 2, 1, 1)
        layout.addWidget(self.quick_button, 4, 2, 1, 1)
        layout.addWidget(self.graphics_view, 0, 3, 5, 1)
        
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # İstenilen diğer ayarlamalar ve olaylar eklenebilir
        self.setWindowTitle("SIRALAMA ALGORİTMALARI GÖRSELLEŞTİRİCİSİ")

# Uygulama oluşturuluyor ve başlatılıyor
app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
