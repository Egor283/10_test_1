from PyQt6.QtWidgets import QWidget
from coefficient_design import Coefficient_design


class Coefficient(QWidget, Coefficient_design):
    def __init__(self, arg, s):
        super().__init__()
        self.setupUi(self)
        self.label.setText(arg)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.doo)

    def doo(self):
        self.close()