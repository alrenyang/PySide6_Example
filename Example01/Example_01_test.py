import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from Example_01 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def Button_slot1(self):
        self.ui.label.setText("첫번째 버튼 눌러짐")

    def Button_slot2(self):
        self.ui.label.setText("두번째 버튼")
    
    def Button_slot3(self):
        self.ui.label.setText("세번째 버튼")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(800,600)
    window.show()

    sys.exit(app.exec())