import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def jacobi(a, n):
        s = 1
        while True:
            if n < 1: raise ValueError("small module: " + str(n))
            if n & 1 == 0: return a
            if n == 1: return s
            a = a % n
            if a == 0: return 0
            if a == 1: return s

            if a & 1 == 0:
                if n % 8 in (3, 5):
                    s = -s
                a >>= 1
                continue

            if a % 4 == 3 and n % 4 == 3:
                s = -s

            a, n = n, a
        return

    def testSolovey(n, t):
        for index in range(t):
            randomNumber = 2 + random.randint(1, 32767) % int((n - 1)/2)
            r = pow(int(randomNumber), int(((n - 1) / 2)), int(n))
            symbolJ = App.jacobi(randomNumber, n)
            if (r != 1 and r != (n - 1)):
                return 0
            if (symbolJ == -1):
                if ((symbolJ + n) != r):
                    return 0
                else:
                    return 1
            return 1

    def fastSqrt(value):
        iter = 0
        aZero = value
        aOne = 0

        while 1:
            aOne = int(((int(value) / int(aZero)) + int(aZero))) >> 1
            if (aZero <= aOne):
                if ((aZero * aZero) <= value and value < (aZero + 1) * (aZero + 1)):
                    return aZero
                else:
                    iter += 1
            else:
                aZero = aOne

    def FermaMethod(value):
        x = App.fastSqrt(value)
        temp = (value + 9) / 6
        index = App.fastSqrt(value)
        for index in range(value):
            if (x * x == value):
                return x
            x = x + 1
            if (x > temp):
                return 1

            z = x * x - value
            y = App.fastSqrt(z)
            if ((y * y) == z):

                return x + y
        return value

    def Factoriz(value, result):
        check = App.testSolovey(value, 100)
        if check == 1:
            result.append(value)
        else:
            div = App.FermaMethod(value)
            print(div)
            App.Factoriz(div, result)
            App.Factoriz(int(value / div), result)
        return result



    def __init__(self):
        super().__init__()
        self.title = 'Prime Generator'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(180, 20)
        self.textbox.resize(120, 20)

        button = QPushButton('Factorization', self)
        button.setToolTip('')
        button.move(180, 70)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()

    def on_click(self):
        textvalue = int(self.textbox.text())
        check = App.testSolovey(textvalue, 100)
        factor = App.Factoriz(textvalue, result=[])


        if textvalue % 2 == 0:
            QMessageBox.question(self, 'Prime generator', "Its Iven number: ", QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            QMessageBox.question(self, 'Prime generator', "You factor numbers: " + str(factor), QMessageBox.Ok,
                                 QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
