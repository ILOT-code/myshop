import sys

from PyQt5.QtWidgets import QApplication

from Controller import Controller



if __name__ == '__main__':
    app = QApplication(sys.argv)
    contr = Controller()
    sys.exit(app.exec_())
