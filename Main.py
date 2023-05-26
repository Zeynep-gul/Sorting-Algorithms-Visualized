import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import*
from PyQt5.QtWidgets import QWidget
from Gui_designer import Ui_MainWindow
import tkinter as tk
from tkinter import ttk
import threading
import random
import time

class main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtTasarim = Ui_MainWindow()
        self.qtTasarim.setupUi(self)

app = QApplication([])
pencere = main()
pencere.show()
app.exec_()