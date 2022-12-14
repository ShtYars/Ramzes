import tkinter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from intormation import *
from PyQt5 import *
from PyQt5 import QtWidgets
import sys





def result(name, surname, age):
    victory_win = QMessageBox()
    victory_win.setWindowTitle('Картка залишеного котика')
    try:
        text_result = get_question_after(str(name), str(surname), int(age))
        victory_win.setText(f"Кличка: {text_result[0]}\n"
                            f"Стать: {text_result[1]}\n"
                            f"Рік народження: {text_result[2]}\n"
                            f"Особливості: {text_result[3]}\n"
                            f"Де загубили: {text_result[4]}\n"
                            f"Порода: {text_result[5]}\n"
                            f"Вік: {text_result[6]}")
    except:
        victory_win.setText("Такого котика не знайдено")

    victory_win.exec_()


def main_menu():
    def get_info():
        name = txt_name.text()
        surname = txt_surname.text()
        age = txt_age.text()
        result(name, surname, age)
     
    def add_label():
        win = QMessageBox()
        win.setWindowTitle('База данних')
        win.setText(f"{show()}")
        win.exec_()

        
    app = QApplication([])
    window = QMainWindow
    main_win = QWidget()
    main_win.setWindowTitle('ЄПошук')
    main_win.resize(400, 200)
    main_win.setObjectName("MainWindow")
    main_win.setStyleSheet("#MainWindow{border-image:url(background.jpg)}")

    label_1 = QLabel('   Для пошуку залишених котиків, внесіть дані  відповідні поля   ')
    label_1.setStyleSheet("background-color: rgb(255,255,255);")
    label_1.setFont(QtGui.QFont('SansSerif', 10))

    label_2 = QLabel("   Кличка   ")
    label_2.setStyleSheet("background-color: rgb(255,255,255);")
    label_2.setFont(QtGui.QFont('SansSerif', 10))

    txt_name = QLineEdit('')

    label_3 = QLabel('   Стать   ')
    label_3.setStyleSheet("background-color: rgb(255,255,255);")
    label_3.setFont(QtGui.QFont('SansSerif', 10))

    txt_surname = QLineEdit('')

    label_4 = QLabel('   Рік народження   ')
    label_4.setStyleSheet("background-color: rgb(255,255,255);")
    label_4.setFont(QtGui.QFont('SansSerif', 10))

    txt_age = QLineEdit('')
    btn_ok = QPushButton('ЗНАЙТИ')
    btn_ok.clicked.connect(get_info)

    btn_lebra = QPushButton('База данних')
    btn_lebra.clicked.connect(add_label)

    layout_main = QVBoxLayout()
    layoutH1 = QHBoxLayout()
    layoutH2 = QHBoxLayout()
    layoutH3 = QHBoxLayout()
    layoutH4 = QHBoxLayout()
    layoutH5 = QHBoxLayout()
    layoutH6 = QHBoxLayout()
    
    

    layoutH1.addWidget(label_1, alignment=Qt.AlignCenter)
    layoutH2.addWidget(label_2, alignment=Qt.AlignCenter)
    layoutH2.addWidget(txt_name, alignment=Qt.AlignCenter)
    layoutH3.addWidget(label_3, alignment=Qt.AlignCenter)
    layoutH3.addWidget(txt_surname, alignment=Qt.AlignCenter)
    layoutH4.addWidget(label_4, alignment=Qt.AlignCenter)
    layoutH4.addWidget(txt_age, alignment=Qt.AlignCenter)
    layoutH5.addWidget(btn_ok, alignment=Qt.AlignCenter)
    layoutH6.addWidget(btn_lebra, alignment=Qt.AlignCenter)
    
    

    layout_main.addLayout(layoutH1)
    layout_main.addLayout(layoutH2)
    layout_main.addLayout(layoutH3)
    layout_main.addLayout(layoutH4)
    layout_main.addLayout(layoutH5)
    layout_main.addLayout(layoutH6)
    main_win.setLayout(layout_main)

    main_win.show()
    app.exec_()


if __name__ == "__main__":
    main_menu()