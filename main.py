import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import json

with open("base.json", "r") as file:
    users = json.load(file)

app = QApplication(sys.argv)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Логин')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label_username = QLabel('Имя пользователя:')
        self.lineEdit_username = QLineEdit()
        layout.addWidget(self.label_username)
        layout.addWidget(self.lineEdit_username)

        self.label_password = QLabel('Пароль:')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.lineEdit_password)

        self.button_login = QPushButton('Войти')
        
        layout.addWidget(self.button_login)

        self.label_message = QLabel()
        layout.addWidget(self.label_message)

        self.setLayout(layout)

    def check_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        # Проверка имени пользователя и пароля
        if username in users and users[username] == password:
            self.label_message.setText('Успешный вход!')
            # self.open_data_window(username)
        else:
            reply = QMessageBox.question(self, 'Регистрация', 'Пользователь не найден. Хотите зарегистрироваться?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.register_user(username, password)
            else:
                self.label_message.setText('Неверное имя пользователя или пароль')

    def register_user(self, username, password):
        # Реализация регистрации пользователя
        users[username] = password
        with open("base.json", "w") as file:
            json.dump(users, file)
        QMessageBox.information(self, 'Регистрация', f'Пользователь {username} успешно зарегистрирован!')
    

class DataWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Данные')
        self.setGeometry(200, 200, 300, 250)

        layout = QVBoxLayout()

        self.label_age = QLabel('Возраст: 25')
        layout.addWidget(self.label_age)

        self.label_location = QLabel('Место жительства: Нью-Йорк')
        layout.addWidget(self.label_location)

        self.label_nationality = QLabel('Национальность: Американец')
        layout.addWidget(self.label_nationality)

        # self.label_name = QLabel('Имя:')
        # layout.addWidget(self.label_name)

        # self.lineEdit_name = QLineEdit()
        # layout.addWidget(self.lineEdit_name)

        # self.lineEdit_school = QLineEdit()
        # layout.addWidget(self.lineEdit_school)

        self.button_logout = QPushButton('Меню')
        
        layout.addWidget(self.button_logout)

        self.setLayout(layout)

data_window = DataWindow()
login_window = LoginWindow()


def login():
    login_window.check_login()
    login_window.hide()
    data_window.show()
login_window.button_login.clicked.connect(login)

def logout():
    login_window.show()
    data_window.hide()
data_window.button_logout.clicked.connect(logout)

login_window.show()
sys.exit(app.exec_())
