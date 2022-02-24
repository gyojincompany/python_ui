import sys
from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from bs4 import BeautifulSoup
import requests

form_class = uic.loadUiType('ui/weatherApp.ui')[0] # ui 불러오기

class WeatherCrawler(QThread): # 쓰레드 클래스로 선언



class WeatherApp(QMainWindow, form_class):
    def __init__(self): # 초기화자
        super().__init__()
        self.setupUi(self) # 만들어 놓은 test.ui 연결
        self.setWindowTitle('오늘의 날씨') # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/test_icon.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('Weather Application Ver 1.0') # 윈도우 상태표시줄 입력



app = QApplication(sys.argv)
window = WeatherApp()
window.show()
app.exec_()