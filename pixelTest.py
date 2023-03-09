import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont

class ColorSquare(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 380)
        self.setWindowTitle('Color Palette')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for i in range(256):
            # Calculate the RGB values using bitwise operators
            r = (i >> 5) * 36  # i >> 5 is equivalent to i // 32
            g = ((i >> 2) & 7) * 36  # (i >> 2) & 7 is equivalent to (i // 4) % 8
            b = (i & 3) * 85  # i & 3 is equivalent to i % 4

            # Convert RGB values to hexadecimal format
            color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)

            # Draw the square
            x = (i % 16) * 48
            y = (i // 16) * 48
            qp.setBrush(QColor(color_hex))
            qp.drawRect(x, y, 48, 48)

            # Draw the hexadecimal value
            qp.setPen(QColor(255, 255, 255))
            font = QFont('Arial', 8)
            qp.setFont(font)
            qp.drawText(x + 3, y + 10, "{:02X}".format(i))

        # Draw the column labels
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(font)
        for i in range(16):
            qp.drawText(i * 48 + 3, 350, "{:X}0".format(i))

        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorSquare()
    sys.exit(app.exec_())
