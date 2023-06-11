import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QTabWidget, QMenuBar, QMenu, QAction,
                             QActionGroup, QVBoxLayout, QLabel)


class DemoTabWidget(QMainWindow):
    def __init__(self, parent=None):
        super(DemoTabWidget, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('实战PyQt5: QTabWidget Demo!')
        # 设置窗口大小
        self.resize(480, 360)

        self.initUi()

    def initUi(self):
        self.initMenu()

        self.tw = QTabWidget(self)
        self.tw.addTab(self.createWidget(0), '常规')
        self.tw.addTab(self.createWidget(1), '快捷方式')
        self.tw.addTab(self.createWidget(2), '兼容性')
        self.tw.addTab(self.createWidget(3), '安全')
        self.tw.addTab(self.createWidget(4), '详细信息')
        self.tw.addTab(self.createWidget(5), '以前的版本')

        self.setCentralWidget(self.tw)

    def initMenu(self):
        menuBar = self.menuBar()
        # 添加一个菜单项，在菜单项下课添加子菜单项
        fileMenu = menuBar.addMenu('文件')
        aExit = QAction('Exit', self)
        aExit.triggered.connect(self.close)
        fileMenu.addAction(aExit)

        # 标签条位置控制
        posMenu = menuBar.addMenu('标签条位置')

        aNorth = QAction('上方', self)
        aNorth.setCheckable(True)
        aNorth.setChecked(True)
        aNorth.triggered.connect(lambda: self.changeTabPos(0))
        aSouth = QAction('下方', self)
        aSouth.setCheckable(True)
        aSouth.triggered.connect(lambda: self.changeTabPos(1))
        aWest = QAction('左边', self)
        aWest.setCheckable(True)
        aWest.triggered.connect(lambda: self.changeTabPos(2))
        aEast = QAction('右边', self)
        aEast.setCheckable(True)
        aEast.triggered.connect(lambda: self.changeTabPos(3))

        posGroup = QActionGroup(self)
        posGroup.addAction(aNorth)
        posGroup.addAction(aSouth)
        posGroup.addAction(aWest)
        posGroup.addAction(aEast)

        posMenu.addAction(aNorth)
        posMenu.addAction(aSouth)
        posMenu.addAction(aWest)
        posMenu.addAction(aEast)

        # 标签条形状
        shapeMenu = menuBar.addMenu('标签条形状')
        aRounded = QAction('圆角矩形', self)
        aRounded.setCheckable(True)
        aRounded.setChecked(True)
        aRounded.triggered.connect(lambda: self.changeTabShape(0))
        aTriangular = QAction('三角形', self)
        aTriangular.setCheckable(True)
        aTriangular.triggered.connect(lambda: self.changeTabShape(1))

        shapeGroup = QActionGroup(self)
        shapeGroup.addAction(aRounded)
        shapeGroup.addAction(aTriangular)

        shapeMenu.addAction(aRounded)
        shapeMenu.addAction(aTriangular)

    def changeTabPos(self, index):
        switcher = {
            0: QTabWidget.North,
            1: QTabWidget.South,
            2: QTabWidget.West,
            3: QTabWidget.East
        }
        self.tw.setTabPosition(switcher.get(index))

    def changeTabShape(self, index):
        if index == 0:
            self.tw.setTabShape(QTabWidget.Rounded)
        else:
            self.tw.setTabShape(QTabWidget.Triangular)

    def createWidget(self, index):
        wid = QWidget()
        layout = QVBoxLayout(wid)
        label = QLabel(wid)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont(self.font().family(), 36))
        label.setText("选项卡 {}".format(index + 1))

        layout.addWidget(label)
        wid.setLayout(layout)
        return wid


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoTabWidget()
    window.show()
    sys.exit(app.exec())