#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################
import sys
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMdiArea, QMessageBox, QMdiSubWindow, QWidget, QStatusBar, QLabel, QToolTip
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QFileInfo, QPoint, QSettings, QSignalMapper, QSize, Qt, QBasicTimer, QDateTime, QTimerEvent
from PyQt6.QtGui import  QFont, QIcon, QAction, QKeySequence


# Include File  ----------------------------------------------------------------------
from SubWindows.Sub_Window import *



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MDI Example")
        self.setWindowIcon(QIcon('MDI_Windows/MDI_6/images/web.png'))  # 경로를 포함한 File 명
        self.resize(1024, 768)
        # ToolTip  정의 -------------------------------------------------
        QToolTip.setFont(QFont('SansSelif', 10))            # ToolTip에 대한 Font 정의
        self.setToolTip('this is a <b>QMainWindow (MDI)</b> widget')  # Window에 대한 ToolTip 정의

        self.mdiArea = QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)
        self.mdiArea.subWindowActivated.connect(self.updateMenus)
        # Sub Window의 메뉴 할당 후 메뉴 선택시 열려있는 화면의 Activation을 활성화하기 위해 연결하여 준다
        self.windowMapper = QSignalMapper(self)
        self.windowMapper.mappedObject.connect(self.setActiveSubWindow)
        self.MenuMapper = QSignalMapper(self)
        self.MenuMapper.mappedString.connect(self.openTestMenu)

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.updateMenus()

        self.readSettings()    # 이전에 종료될때의 화면의 위치와 크기를 복원한다 (OS의 기능을 이용한다)
        #  Timer 정의 -------------------------------------------------
        self.btimer = QBasicTimer()                         # Timer 생성
        self.btimer.start(1000, self)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.mdiArea.closeAllSubWindows()
        if self.mdiArea.currentSubWindow():
            event.ignore()
        else:
            self.writeSettings()  # 종료시점의 화면의 위치와 크기를 OS 상에 저장하여 준다 (다시 시작시 복원하기 위해)
            event.accept()
        return super().closeEvent(event)

    def newFile(self):
        child = self.createMdiChild()
        child.newFile()
        child.show()

    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self)
        if fileName:
            existing = self.findMdiChild(fileName)
            if existing:
                self.mdiArea.setActiveSubWindow(existing)
                return

            child = self.createMdiChild()
            if child.loadFile(fileName):
                self.lb_st2.setText("File loaded")
                child.show()
            else:
                child.close()

    def save(self):
        if self.activeMdiChild() and self.activeMdiChild().save():
            self.lb_st2.setText("File saved")

    def saveAs(self):
        if self.activeMdiChild() and self.activeMdiChild().saveAs():
            self.lb_st2.setText("File saved")

    def cut(self):
        if self.activeMdiChild():
            self.activeMdiChild().cut()

    def copy(self):
        if self.activeMdiChild():
            self.activeMdiChild().copy()

    def paste(self):
        if self.activeMdiChild():
            self.activeMdiChild().paste()

    def about(self):
        QMessageBox.about(self, "About MDI",
                "The <b>MDI</b> example demonstrates how to write multiple "
                "document interface applications using Qt.")

    def updateMenus(self):
        if self.activeMdiChild().__class__.__name__ == MdiChild.__name__:
            hasMdiChild = (self.activeMdiChild() is not None)
            self.saveAct.setEnabled(hasMdiChild)
            self.saveAsAct.setEnabled(hasMdiChild)
            self.pasteAct.setEnabled(hasMdiChild)
            self.closeAct.setEnabled(hasMdiChild)
            self.closeAllAct.setEnabled(hasMdiChild)
            self.tileAct.setEnabled(hasMdiChild)
            self.cascadeAct.setEnabled(hasMdiChild)
            self.nextAct.setEnabled(hasMdiChild)
            self.previousAct.setEnabled(hasMdiChild)
            self.separatorAct.setVisible(hasMdiChild)
            hasSelection = (self.activeMdiChild() is not None and
                            self.activeMdiChild().textCursor().hasSelection())
            self.cutAct.setEnabled(hasSelection)
            self.copyAct.setEnabled(hasSelection)
        else:
            hasMdiChild = (self.activeMdiChild() is not None)
            self.saveAct.setEnabled(hasMdiChild)
            self.saveAsAct.setEnabled(hasMdiChild)
            self.pasteAct.setEnabled(hasMdiChild)
            self.closeAct.setEnabled(hasMdiChild)
            self.closeAllAct.setEnabled(hasMdiChild)
            self.tileAct.setEnabled(hasMdiChild)
            self.cascadeAct.setEnabled(hasMdiChild)
            self.nextAct.setEnabled(hasMdiChild)
            self.previousAct.setEnabled(hasMdiChild)
            self.separatorAct.setVisible(hasMdiChild)
            self.cutAct.setEnabled(False)
            self.copyAct.setEnabled(False)

    def updateWindowMenu(self):
        self.windowMenu.clear()
        self.windowMenu.addAction(self.closeAct)
        self.windowMenu.addAction(self.closeAllAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.tileAct)
        self.windowMenu.addAction(self.cascadeAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.nextAct)
        self.windowMenu.addAction(self.previousAct)
        self.windowMenu.addAction(self.separatorAct)

        windows = self.mdiArea.subWindowList()
        self.separatorAct.setVisible(len(windows) != 0)

        no = 0
        for i, window in enumerate(windows):
            child = window.widget()
            if not child:  continue  # Window가 닫힌 경우 (Nonetype) Skip
            no += 1
            if child.__class__.__name__ == MdiChild.__name__:
                text = "%d %s" % (no, child.userFriendlyCurrentFile())
            else:
                text = "%d %s" % (no, child.windowTitle())
            if no < 9:  text = '&' + text

            action = self.windowMenu.addAction(text)
            action.setCheckable(True)
            action.setChecked(child is self.activeMdiChild())
            action.triggered.connect(self.windowMapper.map)
            # QSignalMapper에서 mappedObject Signal을 사용하므로 Action과 Object인 Window를 Mapping 하여준다.
            self.windowMapper.setMapping(action, window)
    
    def createMdiChild(self):
        child = MdiChild()
        self.mdiArea.addSubWindow(child)
        child.copyAvailable.connect(self.cutAct.setEnabled)
        child.copyAvailable.connect(self.copyAct.setEnabled)
        return child

    def OpenSubWindows(self, sub_Win:QWidget, width, height):
        # 기존에 Open 되어 있는 동일 화면이 있다면 다시 화면을 생성하지 않는다.
        for window in self.mdiArea.subWindowList():
            child = window.widget()
            if child.__class__.__name__ == sub_Win.__class__.__name__:
                self.mdiArea.setActiveSubWindow(window)
                return
        # 기존 Open 화면이 없으므로 신규로 생성한다.
        child = QMdiSubWindow()
        child.setWidget(sub_Win)
        self.mdiArea.addSubWindow(child)
        if (sub_Win.__class__.__name__ == sig_win1.__name__):
            sub_Win.send_sig.connect(self.msg_trans)                # String 형식의 메시지 전달
        elif (sub_Win.__class__.__name__ == cls_sig_win1.__name__):
            sub_Win.send_sig.connect(self.cls_trans)                # Class 형식의 메시지 전달
        child.resize(width, height)
        child.show()

    def Open_subwin1(self):
        self.OpenSubWindows(sub_win1(), 480, 320)

    def Open_subwin2(self):
        self.OpenSubWindows(sub_win2(), 640, 480)

    def Open_subwin3(self):
        self.OpenSubWindows(sub_win3(), 600, 400)

    def Open_sigwin1(self):
        self.OpenSubWindows(sig_win1(), 300, 150)

    def Open_sigwin2(self):
        self.OpenSubWindows(sig_win2(), 300, 150)

    def Open_sigwin3(self):
        self.OpenSubWindows(sig_win3(), 300, 150)

    def Open_sigwin2_1(self):
        self.OpenSubWindows(cls_sig_win1(), 300, 150)

    def Open_sigwin2_2(self):
        self.OpenSubWindows(cls_sig_win2(), 300, 150)

    def createActions(self):
        self.newAct = QAction(QIcon('MDI_Windows/MDI_6/images/new.png'), "&New", self,
                shortcut=QKeySequence.StandardKey.New, 
                statusTip="Create a new file",
                triggered=self.newFile)

        self.openAct = QAction(QIcon('MDI_Windows/MDI_6/images/open.png'), "&Open...", self,
                shortcut=QKeySequence.StandardKey.Open, 
                statusTip="Open an existing file",
                triggered=self.open)

        self.saveAct = QAction(QIcon('MDI_Windows/MDI_6/images/save.png'), "&Save", self,
                shortcut=QKeySequence.StandardKey.Save,
                statusTip="Save the document to disk", 
                triggered=self.save)

        self.saveAsAct = QAction("Save &As...", self,
                shortcut=QKeySequence.StandardKey.SaveAs,
                statusTip="Save the document under a new name",
                triggered=self.saveAs)

        self.exitAct = QAction(QIcon('MDI_Windows/MDI_6/images/exit.png'), "E&xit", self, 
                shortcut=QKeySequence.StandardKey.Quit,
                statusTip="Exit the application",
                triggered=QApplication.closeAllWindows)

        self.cutAct = QAction(QIcon('MDI_Windows/MDI_6/images/cut.png'), "Cu&t", self,
                shortcut=QKeySequence.StandardKey.Cut,
                statusTip="Cut the current selection's contents to the clipboard",
                triggered=self.cut)

        self.copyAct = QAction(QIcon('MDI_Windows/MDI_6/images/copy.png'), "&Copy", self,
                shortcut=QKeySequence.StandardKey.Copy,
                statusTip="Copy the current selection's contents to the clipboard",
                triggered=self.copy)

        self.pasteAct = QAction(QIcon('MDI_Windows/MDI_6/images/paste.png'), "&Paste", self,
                shortcut=QKeySequence.StandardKey.Paste,
                statusTip="Paste the clipboard's contents into the current selection",
                triggered=self.paste)

        self.closeAct = QAction("Cl&ose", self,
                statusTip="Close the active window",
                triggered=self.mdiArea.closeActiveSubWindow)

        self.closeAllAct = QAction("Close &All", self,
                statusTip="Close all the windows",
                triggered=self.mdiArea.closeAllSubWindows)

        self.tileAct = QAction("&Tile", self, 
                statusTip="Tile the windows",
                triggered=self.mdiArea.tileSubWindows)

        self.cascadeAct = QAction("&Cascade", self,
                statusTip="Cascade the windows",
                triggered=self.mdiArea.cascadeSubWindows)

        self.nextAct = QAction("Ne&xt", self, 
                shortcut=QKeySequence.StandardKey.NextChild,
                statusTip="Move the focus to the next window",
                triggered=self.mdiArea.activateNextSubWindow)

        self.previousAct = QAction("Pre&vious", self,
                shortcut=QKeySequence.StandardKey.PreviousChild,
                statusTip="Move the focus to the previous window",
                triggered=self.mdiArea.activatePreviousSubWindow)

        self.subWin1 = QAction("Sub_Win 1", self,
                statusTip="Open Window Sub_Win1",
                triggered=self.Open_subwin1)
        
        self.subWin2 = QAction("Sub_Win 2", self,
                statusTip="Open Window Sub_Win2",
                triggered=self.Open_subwin2)

        self.subWin3 = QAction("Sub_Win 3", self,
                statusTip="Open Window Sub_Win3",
                triggered=self.Open_subwin3)

        self.sig_Win1 = QAction("Signal Main", self,
                statusTip="Open Signal Window Main",
                triggered=self.Open_sigwin1)

        self.sig_Win2 = QAction("Signal Sub1", self,
                statusTip="Open Signal Window Sub 1",
                triggered=self.Open_sigwin2)

        self.sig_Win3 = QAction("Signal Sub2", self,
                statusTip="Open Signal Window Sub 2",
                triggered=self.Open_sigwin3)

        self.sig_cls_Win1 = QAction("Class Signal Main", self,
                statusTip="Open Signal Class Window Main",
                triggered=self.Open_sigwin2_1)

        self.sig_cls_Win2 = QAction("Class Signal Sub1", self,
                statusTip="Open Signal Class Window Sub 1",
                triggered=self.Open_sigwin2_2)

        self.separatorAct = QAction(self)
        self.separatorAct.setSeparator(True)

        self.aboutAct = QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QApplication.aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addSeparator()
        action = self.fileMenu.addAction("Switch layout direction")
        action.triggered.connect(self.switchLayoutDirection)
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)

        self.sub_Menu1 = self.menuBar().addMenu("SubWindow")
        self.sub_Menu1.addAction(self.subWin1)
        self.sub_Menu1.addAction(self.subWin2)
        self.sub_Menu1.addAction(self.subWin3)

        self.sub_Menu2 = self.menuBar().addMenu("Signal")
        self.sub_Menu2.addAction(self.sig_Win1)
        self.sub_Menu2.addAction(self.sig_Win2)
        self.sub_Menu2.addAction(self.sig_Win3)

        self.sub_Menu3 = self.menuBar().addMenu("Class Signal")
        self.sub_Menu3.addAction(self.sig_cls_Win1)
        self.sub_Menu3.addAction(self.sig_cls_Win2)

        self.sub_Menu4 = self.menuBar().addMenu("Menu_Test")
        self.CreateTestMenu()
        # self.windowMenu.aboutToShow.connect(self.updateWindowMenu)

        self.windowMenu = self.menuBar().addMenu("&Window")
        self.updateWindowMenu()
        self.windowMenu.aboutToShow.connect(self.updateWindowMenu)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.newAct)
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)
        self.fileToolBar.addAction(self.exitAct)

        self.editToolBar = self.addToolBar("Edit")
        self.editToolBar.addAction(self.cutAct)
        self.editToolBar.addAction(self.copyAct)
        self.editToolBar.addAction(self.pasteAct)

    def createStatusBar(self):
        # self.statusBar().showMessage("Ready")
        self.stbar = QStatusBar(self)                       # Status Bar 생성
        self.lb_st1 = QLabel(self.stbar)
        self.lb_st1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_st2 = QLabel(self.stbar)
        self.stbar.addWidget(self.lb_st1, 80)
        self.stbar.addWidget(self.lb_st2, 400)
        # self.stbar.setGeometry(0, self.height()-20, self.width(), 20)
        self.setStatusBar(self.stbar)
        self.lb_st2.setText("Ready")

    def activeMdiChild(self):
        activeSubWindow = self.mdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    def findMdiChild(self, fileName):
        canonicalFilePath = QFileInfo(fileName).canonicalFilePath()
        for window in self.mdiArea.subWindowList():
            child = window.widget()
            if child.__class__.__name__ == MdiChild.__name__:
                if window.widget().currentFile() == canonicalFilePath:
                    return window
        return None

    def setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)

    def timerEvent(self, a0:'QTimerEvent') -> None:
        cur_date = QDateTime.currentDateTime()
        self.lb_st1.setText(cur_date.toString('yyyy-MM-dd   hh:mm:ss'))
        return super().timerEvent(a0)

    def readSettings(self):
        settings = QSettings('Treefrog', 'MDI Example')
        pos = settings.value('pos', QPoint(200, 200))
        size = settings.value('size', QSize(1024, 768))
        self.move(pos)
        self.resize(size)

    def writeSettings(self):
        settings = QSettings('Treefrog', 'MDI Example')
        settings.setValue('pos', self.pos())
        settings.setValue('size', self.size())

    def switchLayoutDirection(self):
        if self.layoutDirection() == Qt.LayoutDirection.LeftToRight:
            QApplication.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        else:
            QApplication.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

    def CreateTestMenu(self):
    	for key in list(Win_Dic.keys()):
            if Win_Dic[key][0] == 'seperator':
                self.sub_Menu4.addSeparator()
            else:
                act = self.sub_Menu4.addAction(Win_Dic[key][0])
                act.triggered.connect(self.MenuMapper.map)
                self.MenuMapper.setMapping(act, key)

    def openTestMenu(self, key):
        sub_win = Win_Dic[key][1]()
        wi = Win_Dic[key][2]
        he = Win_Dic[key][3]
        self.OpenSubWindows(sub_win, wi, he)

    @QtCore.pyqtSlot(str)
    def msg_trans(self, rcv_msg:str):
        parm = rcv_msg.partition('|')   # 입력된 Parameter를 '|'를 기준으로 나누어준다.
        # 기존에 Open 되어 있는 화면을 찾아서 Parameter 값을 입력해준다.
        for window in self.mdiArea.subWindowList():
            child = window.widget()
            if child.__class__.__name__ == parm[0]:
                self.mdiArea.setActiveSubWindow(window)
                child.recv_argument(parm[2])
                window.show()
                return

    @QtCore.pyqtSlot(arguments)
    def cls_trans(self, rcv_msg:arguments):
        # 호출된 화면을 생성한다, 기존에 있는 경우 Activate 한다
        self.openTestMenu(rcv_msg.call_to)   
        # 기존에 Open 되어 있는 화면을 찾아서 Parameter 값을 입력해준다.
        for window in self.mdiArea.subWindowList():
            child = window.widget()
            if child.__class__.__name__ == rcv_msg.call_to:
                self.mdiArea.setActiveSubWindow(window)
                child.recv_argument(rcv_msg)
                window.show()
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())


