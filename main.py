
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QLCDNumber, QApplication, QMainWindow, QStyleOptionSlider, QStyle
from views.ui_main import Ui_MainWindow
import sys

from pygame import mixer

class RegApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(RegApp, self).__init__(parent=parent)
        self.setupUi(self)
        
        ###############################################################
        # Inicializando o mix e carregando musica 
        mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
        mixer.init()
        mixer.music.load('sound/music.mp3')
        mixer.music.set_volume(1.0)
        ###############################################################
        
        ###############################################################
        # Status control Player
        self.status = 0
        ###############################################################

        ###############################################################
        # Button to play/pause
        self.btnPlay_a.clicked.connect(self.statusSee)
        ###############################################################

    def statusSee(self):
        if self.status == 0:
            print(f"Playing {self.status}")
            self.play()
            self.status = 1
            return self.status

        if self.status == 1:
            print(f"Pausing {self.status}")
            self.pause()
            self.status = 2
            return self.status
        
        if self.status == 2:
            print(f"Unpausing {self.status}")
            self.unpause()
            self.status = 1
            return self.status
        
    ###############################################################
    # Play Function
    def play(self):
        mixer.music.play()
        self.status = 1
        return self.status
    ###############################################################

    ###############################################################
    # Pause Function
    def pause(self):
        mixer.music.pause()
        self.status = 2
        return self.status
    ###############################################################

    ###############################################################
    # Pause Function
    def unpause(self):
        mixer.music.unpause()
        self.status = 2
        return self.status
    ###############################################################


        ######################################
        
        ######################################
        # Dial
        self.dial_a.setRange(0, 99)
        self.dial_a.setSingleStep(10)
        self.dial_a.setNotchesVisible(True)
        self.dial_a.notchesVisible()
        self.dial_a.valueChanged.connect(self.lcd.display)
        ######################################  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle("Default")
    app.setStyle("Fusion")
    #app.setStyle("imagine")
    #app.setStyle("Material")
    #app.setStyle("Universal")
    
    window = RegApp()
    window.show()
    sys.exit(app.exec())