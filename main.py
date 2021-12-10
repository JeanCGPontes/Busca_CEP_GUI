import classe

import sys


if __name__ == "__main__":
    app = classe.QApplication(sys.argv)
    window = classe.MainWindow()
    sys.exit(app.exec_())
