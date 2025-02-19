import os
import sys
import argparse
import qdarkstyle

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile, QTextStream, QSettings

NAME = 'CQ-editor'

#need to initialize QApp here, otherewise svg icons do not work on windows
app = QApplication(sys.argv,
                   applicationName=NAME)

from .main_window import MainWindow

def main():

    parser = argparse.ArgumentParser(description=NAME)
    parser.add_argument('-r', '--restore_defaults',
        required = False,
        action = 'store_true',
        help = 'restore default settings and exit')
    parser.add_argument('filename',nargs='?',default=None)
    args = parser.parse_args(app.arguments()[1:])

    if args.restore_defaults:
        settings = QSettings(MainWindow.org, MainWindow.name)
        print('Deleting settings file ' + settings.fileName() + '\n')
        # The config file may not exist yet
        try:
            os.remove(settings.fileName())
        except FileNotFoundError:
            pass
        sys.exit()
    else:
        app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', 
            palette=qdarkstyle.DarkPalette))	
        win = MainWindow()

        if args.filename:
           win.components['editor'].load_from_file(args.filename)

        win.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()
