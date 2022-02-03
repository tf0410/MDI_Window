# from PyQt6 import QtWidgets
# from PyQt6.QtCore import Qt
from SubWindows.Signal_Sub.signal2 import sig_win2 

class sig_win3(sig_win2):
    def __init__(self):
        super(sig_win3, self).__init__()
        self.setWindowTitle("Signal Receive 2")

# class sig_win3(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True) 
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Signal Receive")
#         self.label = QtWidgets.QLabel("text", self)
#         self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.label.resize(300, 150)
#         self.show()

#     def recv_argument(self, msg):
#         self.label.setText(msg)
