from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QComboBox, QLabel, QVBoxLayout, QLineEdit

class sig_win1(QtWidgets.QWidget):
    send_sig = QtCore.pyqtSignal(str)
    def __init__(self):
        super(sig_win1, self).__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Signal Input")

        self.cmb_win = QComboBox(self)
        self.cmb_win.addItem('Sub Window 1')
        self.cmb_win.addItem('Sub Window 2')        
        self.cmb_win.activated.connect(self.combo_change)
        self.win_list = ('sig_win2', 'sig_win3')

        self.inputbox = QLineEdit(self)
        self.inputbox.resize(300, 150)
        self.inputbox.returnPressed.connect(self.sendCommand)   # InputBox 에서 Enter Key를 눌렀을때

        V_layout = QVBoxLayout()
        H_layout = QHBoxLayout()
        H_layout.addWidget(QLabel('Select Sub Screen'))
        H_layout.addWidget(self.cmb_win)        
        V_layout.addLayout(H_layout)
        V_layout.addWidget(self.inputbox)

        self.setLayout(V_layout)
        self.show()
 
    def combo_change(self, idx):
        # print(self.win_list[idx])
        pass

    @QtCore.pyqtSlot()
    def sendCommand(self):
        idx = self.cmb_win.currentIndex()
        scr = self.win_list[idx]
        msg = self.inputbox.text()
        self.send_sig.emit(scr + '|' + msg)
        self.inputbox.setText("")
 
