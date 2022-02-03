from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
 

class sig_win2(QtWidgets.QWidget):
    def __init__(self):
        super(sig_win2, self).__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True) 
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Signal Receive 1")
        self.label = QtWidgets.QLabel("text", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.resize(300, 150)
        self.show()

    def recv_argument(self, msg):
        self.label.setText(msg)
