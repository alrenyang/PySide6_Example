import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtGui import *
from Example_Slider import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setText("0")
        self.ui.horizontalSlider.valueChanged.connect(lambda v: self.ui.label.setText(str(v)))
        self.ui.verticalSlider.valueChanged.connect(lambda v:self.SetTextFnc(str(v)))

    def SetTextFnc(self, valu):
        print(valu)
        self.ui.label.setText(valu)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.resize(800,600)
    window.move(geo.topLeft())
    window.setWindowTitle("Slider Test")
    window.show()

    sys.exit(app.exec())