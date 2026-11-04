import sys
import os
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from main_win_design import Ui_MainWindow
from description_line_function import Description_line_function
from description_module_function import Description_module_function
from description_root_function import Description_root_function
from description_fraction_function import Description_fraction_function
from description_square_function import Description_square_function
from description_cube_function import Description_cube_function
from coefficient import Coefficient


class Main_Win(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(700, 350)
        base_dir = os.path.dirname(os.path.abspath(__file__))     
        image_path = os.path.join(base_dir, 'Images', 'img_1.png')
        self.img = QImage(image_path)    
        self.pixmap = QPixmap(self.img)
        self.image.setPixmap(self.pixmap)
        self.radio_button = ''
        # Создаем группу кнопок и добавляем туда кнопки
        self.radio_button_group = QButtonGroup(self)
        self.radio_button_group.addButton(self.radioButton)
        self.radio_button_group.addButton(self.radioButton_2)
        self.radio_button_group.addButton(self.radioButton_3)
        self.radio_button_group.addButton(self.radioButton_4)
        self.radio_button_group.addButton(self.radioButton_5)
        self.radio_button_group.addButton(self.radioButton_6)
        self.initUI()

    def initUI(self):
        self.radioButton.clicked.connect(self.doo)
        self.radioButton_2.clicked.connect(self.doo)
        self.radioButton_3.clicked.connect(self.doo)
        self.radioButton_4.clicked.connect(self.doo)
        self.radioButton_5.clicked.connect(self.doo)
        self.radioButton_6.clicked.connect(self.doo)

    def graf(self):
            w = self.lineEdit.text() == '' or self.lineEdit_2.text() == ''
            q = self.lineEdit_3.text() == '' and self.radio_button == '6'
            r = self.lineEdit_3.text() == '' and self.lineEdit_4.text() == '' and self.radio_button == '4'
            if w or q or r:
                self.cof = Coefficient('Вы не написали коэффициенты', self)
                self.cof.setWindowModality(Qt.WindowModality.ApplicationModal)
                self.cof.show()
            else:
                try:
                    if self.radio_button == '1':
                        test = [float(self.lineEdit.text()), float(self.lineEdit_2.text())]
                        self.mod_win = Description_line_function(self.lineEdit.text(), self.lineEdit_2.text())
                    elif self.radio_button == '2':
                        test = [float(self.lineEdit.text()), float(self.lineEdit_2.text())]
                        self.mod_win = Description_module_function(self.lineEdit.text(), self.lineEdit_2.text())
                    elif self.radio_button == '3':
                        test = [float(self.lineEdit.text()), float(self.lineEdit_2.text())]
                        self.mod_win = Description_root_function(self.lineEdit.text(), self.lineEdit_2.text())
                    elif self.radio_button == '4':
                        test = [float(self.lineEdit.text()), float(self.lineEdit_2.text()), float(self.lineEdit_3.text()), float(self.lineEdit_4.text())]
                        self.mod_win = Description_cube_function(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())
                    elif self.radio_button == '5':
                        test = [float(self.lineEdit.text()), float(self.lineEdit_2.text())]
                        self.mod_win = Description_fraction_function(self.lineEdit.text(), self.lineEdit_2.text())
                    else:
                        test = [float(self.lineEdit.text()), float(self.lineEdit_2.text()), float(self.lineEdit_3.text())]
                        self.mod_win = Description_square_function(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
                    self.mod_win.show()
                except ValueError:
                    self.cof = Coefficient('Вы написали не числа', self)
                    self.cof.setWindowModality(Qt.WindowModality.ApplicationModal)
                    self.cof.show()

    def eraser(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

    def doo(self):
        _translate = QtCore.QCoreApplication.translate
        for i in self.radio_button_group.buttons():
            if i.isChecked():
                self.radio_button = i.text()[-2]
        if self.radio_button:
            if self.radio_button == '6':
                self.setFixedSize(700, 470)
                self.label_d_1.setGeometry(QtCore.QRect(30, 360, 221, 31))
                self.label_d_2.setGeometry(QtCore.QRect(240, 360, 221, 31))
                self.label_d_3.setGeometry(QtCore.QRect(450, 360, 221, 31))
                self.label_d_4.setGeometry(QtCore.QRect(0, 0, 0, 31))
                self.lineEdit.setGeometry(QtCore.QRect(130, 360, 101, 31))
                self.lineEdit_2.setGeometry(QtCore.QRect(340, 360, 101, 31))
                self.lineEdit_3.setGeometry(QtCore.QRect(550, 360, 101, 31))
                self.lineEdit_4.setGeometry(QtCore.QRect(0, 0, 0, 31))
                self.label_d_1.setText(_translate("MainWindow", "Введите a:"))
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.pushButton_2.setGeometry(QtCore.QRect(30, 400, 131, 51))
                self.pushButton_3.setGeometry(QtCore.QRect(175, 400, 131, 51))
            elif self.radio_button == '4':
                self.setFixedSize(700, 520)
                self.label_d_1.setGeometry(QtCore.QRect(30, 360, 221, 31))
                self.label_d_2.setGeometry(QtCore.QRect(350, 360, 221, 31))
                self.label_d_3.setGeometry(QtCore.QRect(30, 410, 221, 31))
                self.label_d_4.setGeometry(QtCore.QRect(350, 410, 221, 31))
                self.lineEdit.setGeometry(QtCore.QRect(150, 360, 151, 31))
                self.lineEdit_2.setGeometry(QtCore.QRect(470, 360, 151, 31))
                self.lineEdit_3.setGeometry(QtCore.QRect(150, 410, 151, 31))
                self.lineEdit_4.setGeometry(QtCore.QRect(470, 410, 151, 31))
                self.label_d_1.setText(_translate("MainWindow", "Введите a:"))
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.pushButton_2.setGeometry(QtCore.QRect(30, 450, 131, 51))
                self.pushButton_3.setGeometry(QtCore.QRect(175, 450, 131, 51))
            else:
                self.setFixedSize(700, 470)
                self.label_d_1.setGeometry(QtCore.QRect(30, 360, 221, 31))
                self.label_d_2.setGeometry(QtCore.QRect(350, 360, 221, 31))
                self.label_d_3.setGeometry(QtCore.QRect(0, 0, 0, 31))
                self.label_d_4.setGeometry(QtCore.QRect(0, 0, 0, 31))
                self.lineEdit.setGeometry(QtCore.QRect(150, 360, 151, 31))
                self.lineEdit_2.setGeometry(QtCore.QRect(470, 360, 151, 31))
                self.lineEdit_3.setGeometry(QtCore.QRect(0, 0, 0, 31))
                self.lineEdit_4.setGeometry(QtCore.QRect(0, 0, 0, 31))
                self.label_d_1.setText(_translate("MainWindow", "Введите k:"))
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.pushButton_2.setGeometry(QtCore.QRect(30, 400, 131, 51))
                self.pushButton_3.setGeometry(QtCore.QRect(175, 400, 131, 51))
            self.pushButton_2.clicked.connect(self.graf)
            self.pushButton_3.clicked.connect(self.eraser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Win()
    ex.show()
    sys.exit(app.exec())