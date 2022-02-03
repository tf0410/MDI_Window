from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
 
from Inc.argmt_class import arguments

class cls_sig_win2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True) 
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Class Signal Receive")
        self.label = QtWidgets.QLabel("text", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.resize(300, 150)
        self.show()

    def recv_argument(self, msg:arguments):
        self.label.setText(msg.call_from + ' ' + str(msg.arg_cnt) + ' ' + msg.str_buf1)
