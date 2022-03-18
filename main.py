
from tokenize import String
from pygame import mixer

from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QLCDNumber, QApplication, QMainWindow, QStyleOptionSlider, QStyle
from views.ui_main import Ui_MainWindow
import sys

class RegApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(RegApp, self).__init__(parent=parent)
        self.setupUi(self)
        ######################################
        # Button to play music
        self.btnPlay_a.clicked.connect(self.player)
        #self.btnPlay_a.clicked.connect(self.testaBtn)
        ######################################
        
        ######################################
        # Dial
        self.dial_a.setRange(0, 99)
        self.dial_a.setSingleStep(10)
        self.dial_a.setNotchesVisible(True)
        self.dial_a.notchesVisible()
        self.dial_a.valueChanged.connect(self.lcd.display)
        ######################################

    def player(self):
        
        if self.btnPlay_a.isChecked():

            print("dando play")    
            mixer.init()
            mixer.music.load('sound/music.mp3')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            return
        
        mixer.pause()
        return

    def testaBtn(self):
        if self.btnPlay_a.isChecked():
            print("botão não está checado")
        else:
            print("botão não checado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle("Default")
    #app.setStyle("Fusion")
    #app.setStyle("imagine")
    #app.setStyle("Material")
    #app.setStyle("Universal")
    
    window = RegApp()
    window.show()
    sys.exit(app.exec())