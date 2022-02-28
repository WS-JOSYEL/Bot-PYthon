import sys
import os
import time
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        
        Dspeak = mainT()
        Dspeak.start()
        
        self.label_gif = QLabel(self)
        self.label_gif.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gif.move(0,0)
        self.label_gif.resize(400,300)
        self.movie = QMovie("JARVIS.gif")
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        
        self.label_jarvis = QLabel(self)
        self.label_jarvis.setText("J.A.R.V.I.S")
        self.label_jarvis.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jarvis.move(0,0)
        self.label_jarvis.setStyleSheet('QLabel {font:bold;font-size:16px;color:#2F00FF}')
        self.label_jarvis.resize(400,300)
        
        self.label_cpu = QLabel(self)
        self.label_cpu.setText("Uso da CPU: 32%")
        self.label_cpu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpu.move(10,270)
        self.label_cpu.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_cpu.resize(131,20)
        cpu = QTimer(self)
        cpu.timeout.connect(self.MostrarCPU)
        cpu.start(1000)
        
        self.label_assv = QLabel(self)
        self.label_assv.setText("Assistente Virtual")
        self.label_assv.move(5,5)
        self.label_assv.setStyleSheet('QLabel {font:bold;font-size:14px;color:#000079}')
        self.label_assv.resize(200,20)

        self.label_version = QLabel(self)
        self.label_version.setText("Alpha version 1.2.1")
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.move(265,270)
        self.label_version.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_version.resize(131,20)
        
        data =  QDate.currentDate()
        datahoje = data.toString('dd/MM/yyyy')
        self.label_data = QLabel(self)
        self.label_data.setText(datahoje)
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.move(316,25)
        self.label_data.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_data.resize(75,20)
          
        self.label_horas = QLabel(self)
        self.label_horas.setText("22:36:09")
        self.label_horas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_horas.move(0,25)
        self.label_horas.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_horas.resize(71,20)
        horas = QTimer(self)
        horas.timeout.connect(self.MostrarHorras)
        horas.start(1000)
        
        botao_fechar = QPushButton("",self)
        botao_fechar.move(370,5)
        botao_fechar.resize(20,20)
        botao_fechar.setStyleSheet("background-image : url(fechar.png);border-radius: 15px") 
        botao_fechar.clicked.connect(self.fechartudo)
        
        self.CarregarJanela()
		
    def CarregarJanela(self):
        self.setWindowFlag(Qt.FramelessWindowHint) #sem botoes e titulo
        self.setGeometry(50,50,400,300)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 300)
        self.setWindowOpacity(0.98) 
        self.setWindowIcon(QtGui.QIcon('icone.png'))
        self.setWindowTitle("Assistente Virtual")
        self.show()

    def fechartudo(self):
        print('botao fechar presionado')
        sys.exit()

    def mousePressEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def MostrarHorras(self):
        hora_atual = QTime.currentTime()
        label_time = hora_atual.toString('hh:mm:ss')
        self.label_horas.setText(label_time)

    def MostrarCPU(self):
        usocpu =  str(psutil.cpu_percent())
        self.label_cpu.setText("Uso da CPU: " +usocpu +"%")
		
