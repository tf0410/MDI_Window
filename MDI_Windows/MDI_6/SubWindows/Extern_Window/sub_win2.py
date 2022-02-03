# Frame, Slide, Dial, Spliter, TabWisget, PixMap(image), Calender, SpinBox, DoubleSpinBox, DateEdit

from PyQt6.QtWidgets import QFrame, QLineEdit, QSpinBox, QTabWidget, QVBoxLayout, QLabel, \
                            QPushButton, QSlider, QDial, QSplitter, QStatusBar, QWidget, QToolTip, \
                            QDateEdit, QDateTimeEdit, QDoubleSpinBox, QCalendarWidget, QTextEdit, QTimeEdit, \
                            QTableWidget, QTextBrowser, QAbstractItemView, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import QBasicTimer, QDateTime, QTime, Qt, QTimerEvent, QDate



class sub_win2(QWidget):
    def __init__(self):
        super(sub_win2, self).__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True) 
        self.initUI()

    def initUI(self):
        # Window 정의 ----------------------------------------------------------------------
        self.setWindowTitle('Widget Test 2')
        self.setWindowIcon(QIcon('MDI_Windows/MDI_6_2/images/web.png'))  # 경로를 포함한 File 명
        # ToolTip  정의 -------------------------------------------------
        QToolTip.setFont(QFont('SansSelif', 10))            # ToolTip에 대한 Font 정의
        self.setToolTip('this is a <b>QWidget</b> widget')  # Window에 대한 ToolTip 정의
        #  StatusBar  정의 -------------------------------------------------
        self.stbar = QStatusBar(self)                       # Status Bar 생성
        self.lb_st1 = QLabel(self.stbar)
        self.lb_st1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_st2 = QLabel(self.stbar)
        self.stbar.addWidget(self.lb_st1, 80)
        self.stbar.addWidget(self.lb_st2, 150)
        self.stbar.setGeometry(0, self.height()-30, self.width(), 30)
        #  Timer 정의 -------------------------------------------------
        self.btimer = QBasicTimer()                         # Timer 생성
        self.btimer.start(1000, self)

        # Slide / Dial 생성 (Frame 안에 생성) -----------------------------------------------
        frame1 = QFrame(self)
        frame1.setFrameShape(QFrame.Shape.Box)
        frame1.setFrameShadow(QFrame.Shadow.Sunken)
        frame1.setLineWidth(1)
        frame1.setMidLineWidth(1)
        frame1.setGeometry(0, 0, self.width(), 65)
        lbl1 = QLabel('Slider/Dial', frame1)
        lbl1.move(15, 15)
        self.sd = QSlider(Qt.Orientation.Horizontal, frame1)        # 가로방향 Slider
        self.sd.setTickPosition(QSlider.TickPosition.TicksBelow)    # 눈금 표시 (아래쪽)
        self.sd.setRange(0, 100)                                    # 범위 값
        self.sd.setSingleStep(5)                                    # 눈금 간격
        self.sd.setGeometry(150, 17, 200, 30)
        self.dl = QDial(frame1)
        self.dl.setNotchesVisible(True)         # 눈금 표시
        self.dl.setRange(0, 100)                # 범위 값
        self.dl.setSingleStep(5)                # 눈금 간격                
        self.dl.setGeometry(380, 2, 60, 60)
        # self.sd.valueChanged.connect(self.dl.setValue)   # Slider를 움직이면 Dial을 동기화 
        # self.dl.valueChanged.connect(self.sd.setValue)   # Dial을 움직이면 Slider를 동기화
        self.sd.valueChanged.connect(self.slider_change)
        self.dl.valueChanged.connect(self.slider_change)
        btn1 = QPushButton('Reset', frame1)
        btn1.setGeometry(500, 12, 60, 40)
        btn1.clicked.connect(self.btn1_click)

        # Spliter ---------------------------------------------------------------------------
        frame2 = QFrame()
        frame2.setFrameShape(QFrame.Shape.Box)
        frame2.setFrameShadow(QFrame.Shadow.Raised)
        frame2.setLineWidth(1)
        frame2.setMidLineWidth(2)
        frame2.resize(self.width()%2, 30)
        frame3 = QFrame()
        frame3.setFrameShape(QFrame.Shape.Box)
        frame3.setFrameShadow(QFrame.Shadow.Raised)
        frame3.setLineWidth(1)
        frame3.setMidLineWidth(2)
        frame3.resize(self.width()%2, 30)
        lb2 = QLabel('Split Test ... ', frame2)
        lb2.move(15, 5)
        spl = QSplitter(Qt.Orientation.Horizontal, self)           # Spliter 의 나뉘는 방향
        spl.setGeometry(0, frame1.height()+1, self.width(), 32)
        spl.addWidget(frame2)
        spl.addWidget(frame3)
        
        # TabSheet ---------------------------------------------------------------------------
        tab_sht1 = QWidget()
        tab_sht2 = QWidget()
        tab_sht3 = QWidget()
        tab_sht4 = QWidget()
        tab_sht5 = QWidget()
        tab_sht6 = QWidget()
        tab = QTabWidget(self)
        tab.addTab(tab_sht1, 'Image  ')
        tab.addTab(tab_sht2, 'Calendar  ')
        tab.addTab(tab_sht3, 'SpinBox  ')
        tab.addTab(tab_sht4, 'TextBrowser')
        tab.addTab(tab_sht5, 'TextEdit')
        tab.addTab(tab_sht6, 'TableWidget')
        tab.setGeometry(0, frame1.height()+spl.height()+2, self.width(), 
                        self.height()-frame1.height()-spl.height()-self.stbar.height()-1)
        # tab.setGeometry(0, 65+32, self.width(), self.height()-65-32-30)
        
        # PixMap (image) ---------------------------------------------------------------------------
        pixmap = QPixmap('C:/Python/Project/PyGame/PYGAME_Project/images/background.jpg')
        # pixmap.scaledToHeight(200, Qt.TransformationMode.FastTransformation)
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_img.setScaledContents(True)
        lbl_size = QLabel()
        lbl_size.setText('Height : ' + str(lbl_img.height()) + '  Width : ' + str(lbl_img.width()))
        vbox1  = QVBoxLayout()
        vbox1.addWidget(lbl_img)
        vbox1.addWidget(lbl_size)
        tab_sht1.setLayout(vbox1)

        # Calender ---------------------------------------------------------------------------
        cal = QCalendarWidget()
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.cal_click)
        self.lbl_date = QLabel()        
        self.lbl_date.setText(cal.selectedDate().toString())    # 현재 날짜를 표시한다.
        vbox2 = QVBoxLayout()
        vbox2.addWidget(cal)
        vbox2.addWidget(self.lbl_date)
        tab_sht2.setLayout(vbox2)

        # SpinBox ---------------------------------------------------------------------------
        frame4 = QFrame(tab_sht3)
        lb3 = QLabel(frame4)
        lb3.setText('SpinBox')
        lb3.setGeometry(1, 1, 100, 20)
        self.spbox = QSpinBox(frame4)
        self.spbox.setRange(-50, 50)
        self.spbox.setSingleStep(5)
        self.spbox.setGeometry(110, 1, 100, 20)
        self.lbl_spb1 = QLabel(frame4)
        self.lbl_spb1.setGeometry(250, 1, 50, 20)
        self.lbl_spb1.setText(str(self.spbox.value()))
        self.spbox.valueChanged.connect(self.change_spbox1)

        # DoubleSpinBox ---------------------------------------------------------------------------
        lb4 = QLabel(frame4)
        lb4.setText('Double SpinBox')
        lb4.setGeometry(1, 25, 100, 20)
        self.dblspb = QDoubleSpinBox(frame4)
        self.dblspb.setRange(-50, 50)
        self.dblspb.setSingleStep(0.5)
        self.dblspb.setPrefix('$')
        self.dblspb.setDecimals(2)
        self.dblspb.setGeometry(110, 25, 100, 20)
        self.lbl_spb2 = QLabel(frame4)
        self.lbl_spb2.setGeometry(250, 25, 50, 20)
        self.lbl_spb2.setText(str(self.dblspb.value()))
        self.dblspb.valueChanged.connect(self.change_spbox2)
       
        # DateEdit ---------------------------------------------------------------------------
        lb5 = QLabel(frame4)
        lb5.setText('DateEdit')
        lb5.setGeometry(1, 55, 100, 20)
        dedt = QDateEdit(frame4)
        dedt.setGeometry(110, 55, 100, 20)
        dedt.setDate(QDate.currentDate())
        dedt.setMinimumDate(QDate(1900, 1, 1))
        dedt.setMaximumDate(QDate(2100, 12, 31))
        # dedt.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        self.lb_de = QLabel(frame4)
        self.lb_de.setGeometry(250, 55, 150, 20)
        self.lb_de.setText(dedt.date().toString())
        dedt.dateChanged[QDate].connect(self.change_date)

        # TimeEdit ---------------------------------------------------------------------------
        lb6 = QLabel(frame4)
        lb6.setText('TimeEdit')
        lb6.setGeometry(1, 80, 100, 20)
        ted = QTimeEdit(frame4)
        ted.setGeometry(110, 80, 100, 20)
        ted.setDisplayFormat('hh:mm:ss')
        ted.setTime(QTime.currentTime())
        # ted.setTimeRange(QTime(2, 10, 10), QTime(22, 20, 30))
        self.lb_te = QLabel(frame4)
        self.lb_te.setGeometry(250, 80, 150, 20)
        self.lb_te.setText(ted.time().toString())
        ted.timeChanged[QTime].connect(self.change_time)

        # DateTimeEdit ---------------------------------------------------------------------------
        lb7 = QLabel(frame4)
        lb7.setText('DateTimeEdit')
        lb7.setGeometry(1, 105, 100, 20)
        dted = QDateTimeEdit(frame4)
        dted.setGeometry(110, 105, 200, 20)
        dted.setDisplayFormat('yyyy-MM-dd  hh:mm:ss')
        dted.setDateTime(QDateTime.currentDateTime())
        # dted.setDateTimeRange(QDateTime(1900, 1, 1, 02, 10, 10), QDateTime(2999, 12, 31, 22, 20, 30))
        self.lb_dte = QLabel(frame4)
        self.lb_dte.setGeometry(350, 105, 250, 20)
        self.lb_dte.setText(dted.dateTime().toString())
        dted.dateTimeChanged[QDateTime].connect(self.change_datetime)

        # TextBrowser ---------------------------------------------------------------------------
        vbox3 = QVBoxLayout()
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.add_Line1)
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        self.btn2 = QPushButton('Clear Browser')
        self.btn2.clicked.connect(self.tb.clear)   # TextBrowser Clear
        vbox3.addWidget(self.le)
        vbox3.addWidget(self.tb)
        vbox3.addWidget(self.btn2)
        tab_sht4.setLayout(vbox3)
            # test 용 Text Data : 아래 내용을 한줄씩 Line Editor에 붇여 넣으면 Rich Text 가 표현된다.
            # Plain Text
            # <b>Bold</b>
            # <i>Italic</i>
            # <p style="color: red">Red</p>
            # <p style="font-size: 20px">20px</p>
            # <a href="https://www.naver.com">Naver</a>
        
        # TextEdit ---------------------------------------------------------------------------
        vbox4 = QVBoxLayout()
        self.te = QTextEdit()
        self.te.setAcceptRichText(True)
        self.te.textChanged.connect(self.count_word)
        self.lbl_te = QLabel()
        self.lbl_te.setText('The number of words is 0')
        vbox4.addWidget(QLabel('Enter your sentence !!!'))
        vbox4.addWidget(self.te)
        vbox4.addWidget(self.lbl_te)
        tab_sht5.setLayout(vbox4)

        # TableWidget ---------------------------------------------------------------------------
        vbox5 = QVBoxLayout()
        self.tbw = QTableWidget()
        self.tbw.setRowCount(20)
        self.tbw.setColumnCount(5)
        self.tbw.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)   # 편집 불가
        # self.tbw.setEditTriggers(QAbstractItemView.DoubleClicked)              # Double Click 시 편집
        # self.tbw.setEditTriggers(QAbstractItemView.AllEditTriggers)            # 항상 편집 가능
        self.tbw.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # Widget의 폭에 맞춤
        # self.tbw.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # Data의 폭에 맞춤
        for i in range(20):
            for j in range(5):
                self.tbw.setItem(i, j, QTableWidgetItem(str(i+j)))   # Table 에 값 표시
        vbox5.addWidget(self.tbw)
        tab_sht6.setLayout(vbox5)
        # Window Display ---------------------------------------------------------------------
        # self.setGeometry(0, 0, 640, 480)
        # self.resize(640, 480)
        # self.show()        
        
    def slider_change(self, pos):
        self.dl.setValue(pos)
        self.sd.setValue(pos)
        self.lb_st2.setText('  Slide Pos : ' + str(pos))
        self.sd.setToolTip(str(pos))    # ToolTip으로 위치를 표시

    def btn1_click(self):
        self.sd.setValue(0)
        self.dl.setValue(0)

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        cur_date = QDateTime.currentDateTime()
        # self.stbar.showMessage(cur_date.toString('yyyy-MM-dd   hh:mm:ss'))
        self.lb_st1.setText(cur_date.toString('yyyy-MM-dd   hh:mm:ss'))
        return super().timerEvent(a0)

    def cal_click(self, date):
        self.lbl_date.setText(date.toString())

    def change_spbox1(self):
        self.lbl_spb1.setText(str(self.spbox.value()))

    def change_spbox2(self):
        self.lbl_spb2.setText(str(self.dblspb.value()))

    def change_date(self, sel_date):
        self.lb_de.setText(sel_date.toString())

    def change_time(self, sel_time):
        self.lb_te.setText(sel_time.toString())

    def change_datetime(self, sel_datetime):
        self.lb_dte.setText(sel_datetime.toString())

    def add_Line1(self):
        self.tb.append(self.le.text())
        self.le.setText('')

    def count_word(self):
        self.lbl_te.setText('The number of words is ' + str(len(self.te.toPlainText().split())))
        
