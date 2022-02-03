from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt

from Inc.argmt_class import arguments

class cls_sig_win1(QtWidgets.QWidget):
    send_sig = QtCore.pyqtSignal(arguments)
    def __init__(self):
        super(cls_sig_win1, self).__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Class Signal Input")
        self.inputbox = QtWidgets.QLineEdit(self)
        self.inputbox.resize(300, 150)
        self.inputbox.returnPressed.connect(self.sendCommand)   # InputBox 에서 Enter Key를 눌렀을때
        self.show()
 
    @QtCore.pyqtSlot()
    def sendCommand(self):
        msg = arguments()
        msg.call_from = "cls_sig_win1"
        msg.call_to = "cls_sig_win2"
        msg.arg_cnt = 1
        msg.str_buf1 = self.inputbox.text()
        
        self.send_sig.emit(msg)
        self.inputbox.setText("")
