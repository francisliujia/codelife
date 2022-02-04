from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def window():
	app = QtGui.QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(300, 200, 500, 500)
	win.setWindowTitle("Python Developer")

	label = QtWidgets.QLabel(win)
	label.setText("my first label")
	label.move(50, 50)

	

	model = QtGui.QStringListModel()
	model.setStringList(['some', 'words', 'in', 'my', 'dictionary'])

	completer = QtGui.QCompleter()
	completer.setModel(model)

	lineedit = QtGui.QLineEdit()
	lineedit.setCompleter(completer)
	lineedit.show()

	win.show()
	sys.exit(app.exec_())


window()