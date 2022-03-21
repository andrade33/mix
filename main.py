
from PySide6 import QtGui
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
        mixer.music.pause()
        mixer.music.set_volume(0.1)
        ###############################################################
        
        ###############################################################
        # Status control Player
        self.status = 0
        ###############################################################

        ###############################################################
        # Button to play/pause
        self.btnPlay_a.clicked.connect(self.seeStatus)
        self.liga_Btn_02.clicked.connect(self.rew)
        ###############################################################

        ######################################
        # Dial
        self.dial_a.setRange(0, 99)
        self.dial_a.setSingleStep(10)
        self.dial_a.setNotchesVisible(True)
        self.dial_a.notchesVisible()
        self.dial_a.valueChanged.connect(self.lcd.display)
        self.dial_a.valueChanged.connect(self.volchange)
        ######################################
        
        ######################################
        # Moving the cursor from each other, but the dlz_01 (Slider Button) has no real time changed, 
        # because it has no implementation funtion for it (with event)
        self.dial_a.valueChanged.connect(self.dlz_01.setValue)
        self.dlz_01.valueChanged.connect(self.dial_a.setValue)
        ######################################
        
    ###############################################################
    # Volume Function
    def volchange(self):
        volume = self.dial_a.value() / 100
        print(f"Volume: {(volume) *100 :.0f}")
        mixer.music.set_volume(volume)
    ###############################################################

    ###############################################################
    # 
    def isplaying():
        return mixer.music.get_busy()
    
    def rew(self):    
        print("Rewind")
        mixer.music.rewind()
    ###############################################################

    ###############################################################
    # Status Function
    def seeStatus(self):
        if self.status == 0:
            print(f"Playing {self.status}")
            self.play()
            self.status = 1
            self.btnPlay_a.setIcon(QtGui.QIcon("icons/play.svg"))
            return self.status

        if self.status == 1:
            print(f"Pausing {self.status}")
            self.pause()
            self.status = 2
            self.btnPlay_a.setIcon(QtGui.QIcon("icons/pause.svg"))
            return self.status
        
        if self.status == 2:
            print(f"Unpausing {self.status}")
            self.unpause()
            self.status = 1
            self.btnPlay_a.setIcon(QtGui.QIcon("icons/play.svg"))
            return self.status
    ###############################################################
    
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
    # Unpause Function
    def unpause(self):
        mixer.music.unpause()
        self.status = 2
        return self.status
    ###############################################################
        
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