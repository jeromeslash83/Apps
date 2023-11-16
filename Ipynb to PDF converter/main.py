import sys
from PyQt5.QtWidgets import QApplication
from widgets import PDFConverterApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PDFConverterApp()
    ex.show()
    sys.exit(app.exec_())
