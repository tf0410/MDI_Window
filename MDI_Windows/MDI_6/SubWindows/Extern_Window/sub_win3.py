# Label, CheckBox, RadioButton, comboBox, LineEdit, Button, Porgress Bar, Timer 

from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout, QLineEdit, QProgressBar,
                             QRadioButton, QWidget, QPushButton, QToolTip, QLabel, QVBoxLayout)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QTimerEvent, Qt, QBasicTimer


class sub_win3(QWidget):
    def __init__(self):
        super(sub_win3, self).__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True) 
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSelif', 10))   # ToolTip에 대한 Font 정의
        self.setToolTip('this is a <b>QWidget</b> widget')  # Window에 대한 ToolTip 정의
        # Label
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)
        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)
        label2.setFont(font2)

        # CheckBox
        chkBox1 = QCheckBox('Check Box 1')
        chkBox1.stateChanged.connect(self.chkBox1_Changed)  # CheckBox 값 변경시 처리할 함수 정의
        chkBox2 = QCheckBox('Check Box 2')
        chkBox3 = QCheckBox('Check Box 3')     
        chkBox3.setChecked(True)   

        # RadioButton
        rbt1 = QRadioButton('Radio Button 1')
        rbt2 = QRadioButton('Radio Button 2')
        rbt2.setChecked(True)
        rbt1.toggled.connect(self.radio_change)

        # comboBox
        cmbx = QComboBox(self)
        cmbx.addItem('Option 1')
        cmbx.addItem('Oprion 2')
        cmbx.addItem('Option 3')
        cmbx.addItem('Option 4')
        cmbx.activated.connect(self.combo_change)

        # QLineEdit
        ed = QLineEdit()
        ed.textChanged.connect(self.ed_text_chg)
        self.label3 = QLabel()
        self.label3.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Button 정의
        btn1 = QPushButton('  &Quit', self)
        btn1.setIcon(QIcon('pyqt6_test/exit.png'))
        # btn1.move(500, 350)            # Button 의 위치 조정
        # btn1.resize(btn1.sizeHint())   # Button Caption에 따른 크기 자동 조정
        btn1.setGeometry(450, 300, 70, 50)  # Button의 위치 및 크기 정의 : 상기 move와 resize를 대체한다.
        btn1.setToolTip('this is a <b>QPushButton</b> widget')  # Button에 대한 ToolTip 정의
        # btn1.clicked.connect(QCoreApplication.instance().quit)  # Window 종료
        btn1.clicked.connect(QApplication.quit)  # Window 종료

        # Porgress Bar / Timer 
        self.btn2 = QPushButton('Start Progress Bar !!!', self)
        self.btn2.resize(30, 100)
        self.btn2.clicked.connect(self.start_progress)

        self.pbar = QProgressBar()
        self.pbar.setGeometry(30, 40, 200, 25)

        self.timer = QBasicTimer()
        self.step = 0


        # Layout
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addStretch(1)
        layout.addWidget(cmbx)
        layout.addWidget(chkBox1)
        layout.addWidget(chkBox2)
        layout.addWidget(chkBox3)
        layout.addStretch(1)
        layout.addWidget(rbt1)
        layout.addWidget(rbt2)
        layout.addStretch(1)
        layout2 = QGridLayout()
        layout2.addWidget(QLabel('Input LineEdit'), 0, 0)
        layout2.addWidget(ed, 0, 1)
        layout2.addWidget(self.label3, 1, 1)
        layout.addLayout(layout2)
        layout.addStretch(1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.pbar)
        layout.addStretch(1)
        layout.addWidget(btn1)

        self.setLayout(layout)


        # Window 정의
        self.setWindowTitle('My Win App')
        self.setWindowIcon(QIcon('pyqt6_test/web.png'))  # 경로를 포함한 File 명
        self.setGeometry(300, 300, 600, 400)
        self.show()

    def chkBox1_Changed(self, stat):
        # print(stat)
        if stat:
            print('check Box 1 Checked !!!')
        else:
            print('check Box 1 UnChecked !!!')

    def radio_change(self, stat):
        print(stat)

    def combo_change(self, idx):
        print(idx)

    def ed_text_chg(self, str):
        self.label3.setText(str)

    def start_progress(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn2.setText('Start Progress Bar !!!')
        else:
            if self.step >= 100:
                self.pbar.reset()        
                self.step = 0
            self.timer.start(100, self)
            self.btn2.setText('Stop Progress Bar !!!')

    def timerEvent(self, a0: 'QTimerEvent') -> None:  # timerEvent 원형
        if self.step >= 100:
            self.timer.stop()    
            self.btn2.setText('Start Progress Bar !!!')
        self.step += 1
        self.pbar.setValue(self.step)
        return super().timerEvent(a0)   # timerEvent Return 원형

