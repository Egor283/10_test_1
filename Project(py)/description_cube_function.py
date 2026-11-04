import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from description_cube_function_design import Description_cube_function_design


class Description_cube_function(QWidget, Description_cube_function_design):
    def __init__(self, a, b, c, d):
        super().__init__()
        self.move(515, 540)
        if a == '1':
            self.a_label = ''
            self.a = '1'
        elif a == '-1':
            self.a_label = '-'
            self.a = '-1'
        else:
            self.a_label = self.a = a
        if b == '1':
            self.b_label = ''
            self.b = '1'
        elif b == '-1':
            self.b_label = '-'
            self.b = '-1'
        else:
            self.b_label = self.b = b
        if c == '1':
            self.c_label = ''
            self.c = '1'
        elif c == '-1':
            self.c_label = '-'
            self.c = '-1'
        else:
            self.c_label = self.c = c
        self.d = d
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.doo)
        a, b, c, d = float(self.a), float(self.b), float(self.c), float(self.d)
        plt.close('all')
        if a:
            if a and b and c and d:
                if b > 0 and c > 0 and d > 0:
                    self.label.setText(
                        f'y = {self.a_label}x³ + {self.b_label}x² + {self.c_label}x + {self.d}; куб. функция, графиком является куб. парабола')
                if b > 0 and c > 0 and d < 0:
                    self.label.setText(
                        f'y = {self.a_label}x³ + {self.b_label}x² + {self.c_label}x - {self.d[1:]}; куб. функция, графиком является куб. парабола')
                if b > 0 and c < 0 and d > 0:
                    self.label.setText(
                        f'y = {self.a_label}x³ + {self.b_label}x² - {self.c_label[1:]}x + {self.d}; куб. функция, графиком является куб. парабола')
                if b > 0 and c < 0 and d < 0:
                    self.label.setText(
                        f'y = {self.a_label}x³ + {self.b_label}x² - {self.c_label[1:]}x - {self.d[1:]}; куб. функция, графиком является куб. парабола')
                if b < 0 and c > 0 and d > 0:
                    self.label.setText(
                        f'y = {self.a_label}x³ - {self.b_label[1:]}x² + {self.c_label}x + {self.d}; куб. функция, графиком является куб. парабола')
                if b < 0 and c > 0 and d < 0:
                    self.label.setText(
                        f'y = {self.a_label}x³ - {self.b_label[1:]}x² + {self.c_label}x - {self.d[1:]}; куб. функция, графиком является куб. парабола')
                if b < 0 and c < 0 and d > 0:
                    self.label.setText(
                        f'y = {self.a_label}x³ - {self.b_label[1:]}x² - {self.c_label[1:]}x + {self.d}; куб. функция, графиком является куб. парабола')
                if b < 0 and c < 0 and d < 0:
                    self.label.setText(
                        f'y = {self.a_label}x³ - {self.b_label[1:]}x² - {self.c_label[1:]}x - {self.d[1:]}; куб. функция, графиком является куб. парабола')
        else:
            if b and c and d:
                if d > 0 and c > 0:
                    self.label.setText(
                        f'y = {self.b_label}x² + {self.c_label}x + {self.d}; квадрат. функция, графиком является парабола')
                elif d < 0 and c > 0:
                    self.label.setText(
                        f'y = {self.b_label}x² + {self.c_label}x - {self.d[1:]}; квадрат. функция, графиком является парабола')
                elif d > 0 and c < 0:
                    self.label.setText(
                        f'y = {self.b_label}x² - {self.c_label[1:]}x + {self.d}; квадрат. функция, графиком является парабола')
                else:
                    self.label.setText(
                        f'y = {self.b_label}x² - {self.c_label[1:]}x - {self.d[1:]}; квадрат. функция, графиком является парабола')
                x_0 = round(-c / (b * 2), 3)
                y_0 = round((x_0 ** 2 * b) + (c * x_0) + d, 3)
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = ({y_0};+∞)')
                if b > 0:
                    self.label_3.setText(f'f(x) ↗ возрастает x ({x_0};+∞); f(x) ↘ убывает x (-∞;{x_0})')
                else:
                    self.label_3.setText(f'f(x) ↗ возрастает x (-∞;{x_0}); f(x) ↘ убывает x ({x_0};+∞)')
                self.label_4.setText(f'Пересечение с Осью y (0;{self.d})')
                if (b > 0 and y_0 < 0) or (b < 0 and y_0 > 0):
                    dis = b ** 2 - 4 * a * c
                    x_1, x_2 = (-c + (dis ** 0.5)) / (2 * b), (-c - (dis ** 0.5)) / (2 * b)
                    self.label_5.setText(f'Нули функции y = 0 при x = {x_1} или {x_2}')
                elif (b > 0 and y_0 > 0) or (b < 0 and y_0 < 0):
                    self.label_5.setText(f'Нулей функции нет')
                else:
                    self.label_5.setText(f'Нули функции y = 0 при x = 0')
            elif b and c and not d:
                if c > 0:
                    self.label.setText(f'y = {self.b_label}x² + {self.c_label}x; квадрат. функция, графиком является парабола')
                else:
                    self.label.setText(f'y = {self.b_label}x² - {self.c_label[1:]}x; квадрат. функция, графиком является парабола')
                x_0 = round(-c / (b * 2), 3)
                y_0 = round((x_0 ** 2 * b) + (c * x_0), 3)
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = ({y_0};+∞)')
                if b > 0:
                    self.label_3.setText(f'f(x) ↗ возрастает x ({x_0};+∞); f(x) ↘ убывает x (-∞;{x_0})')
                else:
                    self.label_3.setText(f'f(x) ↗ возрастает x (-∞;{x_0}); f(x) ↘ убывает x ({x_0};+∞)')
                self.label_4.setText(f'Пересечение с Осью y (0;{self.c})')
                if (b > 0 and y_0 < 0) or (b < 0 and y_0 > 0):
                    dis = c ** 2 - 4 * b * d
                    x_1, x_2 = (-c + (dis ** 0.5)) / (2 * b), (-c - (dis ** 0.5)) / (2 * b)
                    self.label_5.setText(f'Нули функции y = 0 при x = {x_1} или {x_2}')
                elif (b > 0 and y_0 > 0) or (b < 0 and y_0 < 0):
                    self.label_5.setText(f'Нулей функции нет')
                else:
                    self.label_5.setText(f'Нули функции y = 0 при x = 0')
            elif a and not b and c:
                if d > 0:
                    self.label.setText(f'y = {self.b_label}x² + {self.d}; квадрат. функция, графиком является парабола')
                else:
                    self.label.setText(f'y = {self.b_label}x² - {self.d[1:]}; квадрат. функция, графиком является парабола')
                x_0 = 0
                y_0 = round((x_0 ** 2 * b) + (c * x_0) + d, 3)
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = ({y_0};+∞)')
                if b > 0:
                    self.label_3.setText(f'f(x) ↗ возрастает x ({x_0};+∞); f(x) ↘ убывает x (-∞;{x_0})')
                else:
                    self.label_3.setText(f'f(x) ↗ возрастает x (-∞;{x_0}); f(x) ↘ убывает x ({x_0};+∞)')
                self.label_4.setText(f'Пересечение с Осью y (0;{self.c})')
                if (b > 0 and y_0 < 0) or (b < 0 and y_0 > 0):
                    dis = c ** 2 - 4 * b * d
                    x_1, x_2 = (-c + dis ** 0.5) / (2 * b), (-b - dis ** 0.5) / (2 * b)
                    self.label_5.setText(f'Нули функции y = 0 при x = {x_1} или {x_2}')
                elif (b > 0 and y_0 > 0) or (b < 0 and y_0 < 0):
                    self.label_5.setText(f'Нулей функции нет')
                else:
                    self.label_5.setText(f'Нули функции y = 0 при x = 0')
            elif b and not c and not d:
                self.label.setText(f'y = {self.b_label}x²; квадрат. функция, графиком является парабола')
                x_0 = 0
                y_0 = 0
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = ({y_0};+∞)')
                if b > 0:
                    self.label_3.setText(f'f(x) ↗ возрастает x ({x_0};+∞); f(x) ↘ убывает x (-∞;{x_0})')
                else:
                    self.label_3.setText(f'f(x) ↗ возрастает x (-∞;{x_0}); f(x) ↘ убывает x ({x_0};+∞)')
                self.label_4.setText(f'Пересечение с Осью y (0;0)')
                self.label_5.setText(f'Нули функции y = 0 при x = 0')
            else:
                if c and d:
                    self.label.setText(f'y = {self.c_label}x + {self.d}; линейная функция, графиком является прямая')
                    self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = (-∞;+∞)')
                elif c and not d:
                    self.label.setText(f'y = {self.c_label}x; линейная функция, графиком является прямая')
                    self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = (-∞;+∞)')
                else:
                    self.label.setText(f'y = {self.d}; линейная функция, графиком является прямая')
                    self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = {self.d}')
                if c > 0:
                    self.label_3.setText(f'f(x) ↗ возрастает')
                elif c < 0:
                    self.label_3.setText(f'f(x) ↘ убывает')
                else:
                    self.label_3.setText(f'f(x) параллельно оси Ox')
                self.label_4.setText(f'Пересечение с осью y (0;{self.d})')
                if c:
                    x_0 = round(-d / c, 2)
                    self.label_5.setText(f'Нули функции y = 0 при x = {x_0}')
                else:
                    self.label_5.setText(f'Нулей не существует')
        x = np.linspace(-20, 20, 10000)
        fig, ax = plt.subplots()
        fig.set_size_inches(2, 2)
        ax.set_ylim(-20, 20)
        ax.set_xlim(-20, 20)
        fig.set_size_inches(5, 4)
        ax.grid()
        y = a * (x ** 3) + b * (x ** 2) + c * x + d
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlabel('Ось x', fontsize=14)
        plt.ylabel('Ось y', fontsize=14)
        plt.title('График', fontsize=14)
        fig.canvas.manager.window.move(515, 75)
        ax.plot(x, y)
        plt.show(block=False)

    def doo(self):
        plt.close()
        self.close()