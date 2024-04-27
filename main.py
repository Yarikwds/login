import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

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
        self.button_login.clicked.connect(self.check_login)
        layout.addWidget(self.button_login)

        self.label_message = QLabel()
        layout.addWidget(self.label_message)

        self.setLayout(layout)

    def check_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        # Список пользователей с их именами и паролями
        users = {'admin': 'password', 'user1': '1234', 'user2': 'qwerty'}

        # Проверка имени пользователя и пароля
        if username in users and users[username] == password:
            self.label_message.setText('Успешный вход!')
            self.open_data_window(username)
        else:
            reply = QMessageBox.question(self, 'Регистрация', 'Пользователь не найден. Хотите зарегистрироваться?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.register_user(username, password)
            else:
                self.label_message.setText('Неверное имя пользователя или пароль')

    def open_data_window(self, username):
        self.hide()  # Скрыть окно входа
        self.data_window = DataWindow(username=username)
        self.data_window.show()

    def register_user(self, username, password):
        # Реализация регистрации пользователя
        QMessageBox.information(self, 'Регистрация', f'Пользователь {username} успешно зарегистрирован!')

class DataWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle('Данные')
        self.setGeometry(200, 200, 300, 250)

        layout = QVBoxLayout()

        self.label_username = QLabel(f'Имя пользователя: {username}')
        layout.addWidget(self.label_username)

        self.label_static_info = QLabel('Статическая информация:')
        layout.addWidget(self.label_static_info)

        self.label_age = QLabel('Возраст: 25')
        layout.addWidget(self.label_age)

        self.label_location = QLabel('Место жительства: Нью-Йорк')
        layout.addWidget(self.label_location)

        self.label_nationality = QLabel('Национальность: Американец')
        layout.addWidget(self.label_nationality)

        self.label_name = QLabel('Имя:')
        layout.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit()
        layout.addWidget(self.lineEdit_name)

        self.label_school = QLabel('Место обучения:')
        layout.addWidget(self.label_school)

        self.lineEdit_school = QLineEdit()
        layout.addWidget(self.lineEdit_school)

        self.button_logout = QPushButton('Выйти')
        self.button_logout.clicked.connect(self.logout)
        layout.addWidget(self.button_logout)

        self.setLayout(layout)

    def logout(self):
        self.close()  # Закрыть окно с данными

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
