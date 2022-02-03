# Include File  ----------------------------------------------------------------------
from Inc.argmt_class import arguments


# Memo 장 용 Test widget -------------------------------------------------------------
from SubWindows.Win_Memo import MdiChild


# Extern File widget Test ------------------------------------------------------------
from SubWindows.Extern_Window.sub_win1 import sub_win1
from SubWindows.Extern_Window.sub_win2 import sub_win2
from SubWindows.Extern_Window.sub_win3 import sub_win3
# Signal Test ------------------------------------------------------------------------
from SubWindows.Signal_Sub.signal1 import sig_win1
from SubWindows.Signal_Sub.signal2 import sig_win2
from SubWindows.Signal_Sub.signal3 import sig_win3
# Signal Class Argument Test ---------------------------------------------------------
from SubWindows.Class_argm.sig_cls1 import cls_sig_win1
from SubWindows.Class_argm.sig_cls2 import cls_sig_win2
# ------------------------------------------------------------------------------------



# Main 화면에 종속된 child 하면을 생성하기 위한 Dictionary를 생성한다.
# Key 값은 화면 ID(화면 Class 명)로 한다, 
# Value 값은 0:Menu에 표시되는 명칭, 1:화면ID(Class), 2:Width, 3:Height 로 구성된 List(Tuple도 됨)로 한다.
Win_Dic = {'sub_win1':['테스트 윈도우 1', sub_win1, 480, 320],
           'sub_win2':['테스트 윈도우 2', sub_win2, 640, 480],
           'sub_win3':['테스트 윈도우 3', sub_win3, 600, 400],
           'sep1':['seperator', None, 0, 0],                    # 메뉴상에서 Sererator를 생성한다
           'sig_win1':['테스트 윈도우 4', sig_win1, 300, 150],
           'sig_win2':['테스트 윈도우 5', sig_win2, 300, 150],
           'sig_win3':['테스트 윈도우 6', sig_win3, 300, 150],
           'sep2':['seperator', None, 0, 0],                    # 메뉴상에서 Sererator를 생성한다
           'cls_sig_win1':['테스트 윈도우 7', cls_sig_win1, 300, 150],
           'cls_sig_win2':['테스트 윈도우 8', cls_sig_win2, 300, 150]}
