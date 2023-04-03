#!/usr/bin/env python3

import wx

# Controllers "A", "Z" from the left side and "Arrow Up", "Arrow Down"
# from the right side.
# "Space" = "pause"


# ........Global...Variabels......................................................

tmr = 0
ind_x = 0
ind_y = 0
pause = 0
sc = 0

speed = 10

display_colour = wx.Colour(27, 41, 169)
element_colour = wx.Colour(213, 205, 29)

dis = 1


# ........Change...Speed..........................................................

class Speed(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.InitUI()
        self.SetTitle('Choose speed')
        self.SetSize((340, 110))
        self.SetPosition((200, 30))
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)

        self.sp1 = wx.RadioButton(panel, label='1', pos=(50, 30))
        self.sp2 = wx.RadioButton(panel, label='2', pos=(100, 30))
        self.sp3 = wx.RadioButton(panel, label='3', pos=(150, 30))
        self.sp4 = wx.RadioButton(panel, label='4', pos=(200, 30))
        self.sp5 = wx.RadioButton(panel, label='5', pos=(250, 30))

        self.sp3.SetValue(True)

        self.Bind(wx.EVT_RADIOBUTTON, self.OnChoice)

    def OnChoice(self, e):

        global speed

        if self.sp1.GetValue():
            speed = 8
        if self.sp2.GetValue():
            speed = 6
        if self.sp3.GetValue():
            speed = 4
        if self.sp4.GetValue():
            speed = 3
        if self.sp5.GetValue():
            speed = 2


# ........Change...Color..........................................................


class ChangeColour(wx.Frame):
    def __init__(self, parent, display, ball, bat1, bat2, border):
        super().__init__(parent, style=wx.MINIMIZE_BOX |
                                       wx.CLOSE_BOX | wx.STAY_ON_TOP)
        self.InitUI()

        self.parent = parent

        self.display = display
        self.ball = ball
        self.bat1 = bat1
        self.bat2 = bat2
        self.border = border

        self.Show()

        self.SetPosition((800, 250))

        self.SetSize((480, 390))
        self.SetTitle('Pick Color')

        self.RGB()
        self.HEX()

    def InitUI(self):

        panel = wx.Panel(self)

        wx.StaticText(panel, label='Red:', pos=(10, 40))
        self.red = wx.Slider(panel, value=display_colour[0], minValue=10, maxValue=255,
                             pos=(70, 40), size=(150, 25))

        wx.StaticText(panel, label='Green:', pos=(10, 90))
        self.green = wx.Slider(panel, value=display_colour[1], minValue=10, maxValue=255,
                               pos=(70, 90), size=(150, 25))

        wx.StaticText(panel, label='Blue:', pos=(10, 140))
        self.blue = wx.Slider(panel, value=display_colour[2], minValue=10, maxValue=255,
                              pos=(70, 140), size=(150, 25))

        self.rint = wx.StaticText(panel, label=str(self.red.GetValue()), pos=(230, 42))
        self.gint = wx.StaticText(panel, label=str(self.green.GetValue()), pos=(230, 92))
        self.bint = wx.StaticText(panel, label=str(self.blue.GetValue()), pos=(230, 142))

        self.colp = wx.Panel(panel, pos=(270, 10), size=(200, 200))
        col = wx.Colour(255, 255, 255)
        self.colp.SetBackgroundColour(display_colour)

        wx.StaticText(panel, label='RGB:', pos=(228, 242))
        self.rgb = wx.TextCtrl(panel, pos=(270, 240), size=(200, -1))
        wx.StaticText(panel, label='HEX:', pos=(10, 242))
        self.hex = wx.TextCtrl(panel, pos=(50, 240), size=(170, -1))

        # ........Buttons..........................................................

        self.disbtn = wx.RadioButton(panel, label='Display Colour', pos=(40, 310), size=(120, -1))
        self.disbtn.SetValue(True)
        self.evtbtn = wx.RadioButton(panel, label='Element Colour', pos=(190, 310), size=(120, -1))

        self.set = wx.Button(panel, label='Set', pos=(340, 310), size=(120, -1))

        # ........Events..........................................................

        self.set.Bind(wx.EVT_BUTTON, self.OnSet)

        self.disbtn.Bind(wx.EVT_RADIOBUTTON, self.OnDis)
        self.evtbtn.Bind(wx.EVT_RADIOBUTTON, self.OnEvt)

        self.red.Bind(wx.EVT_SLIDER, self.OnRed)
        self.green.Bind(wx.EVT_SLIDER, self.OnGreen)
        self.blue.Bind(wx.EVT_SLIDER, self.OnBlue)

    # ........Change colour..........................................................

    def OnSet(self, e):
        global display_colour, element_colour

        if self.hex.GetValue() != '':
            col = self.hex.GetValue()
            col = col.lstrip('#')
            rgb = tuple(int(col[i:i + 2], 16) for i in (0, 2, 4))
            if dis == 1:
                display_colour = wx.Colour(rgb)
                self.OnDis(None)
                self.OnRed(None)
            else:
                element_colour = wx.Colour(rgb)
                self.OnEvt(None)
                self.OnRed(None)

    def OnDis(self, e):
        global dis
        dis = 1
        self.colp.SetBackgroundColour(display_colour)
        self.red.SetValue(display_colour[0])
        self.green.SetValue(display_colour[1])
        self.blue.SetValue(display_colour[2])
        self.colp.Refresh()
        self.parent.Refresh()

        self.RGB()
        self.HEX()

    def OnEvt(self, e):
        global dis
        dis = 0
        self.colp.SetBackgroundColour(element_colour)
        self.red.SetValue(element_colour[0])
        self.green.SetValue(element_colour[1])
        self.blue.SetValue(element_colour[2])
        self.colp.Refresh()
        self.parent.Refresh()

        self.RGB()
        self.HEX()

    # ........Modules..........................................................

    def OnRed(self, e):

        global display_colour, element_colour

        red = self.red.GetValue()
        self.rint.SetLabel(str(red))
        col = wx.Colour(red, self.green.GetValue(), self.blue.GetValue())
        self.colp.SetBackgroundColour(col)
        self.colp.Refresh()

        if dis == 1:
            self.display.SetBackgroundColour(col)
            display_colour = col
        if dis == 0:
            self.ball.SetBackgroundColour(col)
            self.bat1.SetBackgroundColour(col)
            self.bat2.SetBackgroundColour(col)
            self.border.SetBackgroundColour(col)
            element_colour = col
        self.parent.Refresh()

        self.RGB()
        self.HEX()

    def OnGreen(self, e):

        global display_colour, element_colour

        green = self.green.GetValue()
        G = green
        self.gint.SetLabel(str(green))
        col = wx.Colour(self.red.GetValue(), green, self.blue.GetValue())
        self.colp.SetBackgroundColour(col)
        self.colp.Refresh()

        if dis == 1:
            self.display.SetBackgroundColour(col)
            display_colour = col
        if dis == 0:
            self.ball.SetBackgroundColour(col)
            self.bat1.SetBackgroundColour(col)
            self.bat2.SetBackgroundColour(col)
            self.border.SetBackgroundColour(col)
            element_colour = col
        self.parent.Refresh()

        self.RGB()
        self.HEX()

    def OnBlue(self, e):

        global display_colour, element_colour

        blue = self.blue.GetValue()
        B = blue
        self.bint.SetLabel(str(blue))
        col = wx.Colour(self.red.GetValue(), self.green.GetValue(), blue)
        self.colp.SetBackgroundColour(col)
        self.colp.Refresh()

        if dis == 1:
            self.display.SetBackgroundColour(col)
            self.display.Refresh()
            display_colour = col
        if dis == 0:
            self.ball.SetBackgroundColour(col)
            self.bat1.SetBackgroundColour(col)
            self.bat2.SetBackgroundColour(col)
            self.border.SetBackgroundColour(col)
            element_colour = col
        self.parent.Refresh()

        self.RGB()
        self.HEX()

    def RGB(self):
        if dis == 1:
            self.rgb.SetValue(f'{display_colour[0]}, {display_colour[1]}, {display_colour[2]}')
        else:
            self.rgb.SetValue(f'{element_colour[0]}, {element_colour[1]}, {element_colour[2]}')

    def HEX(self):
        # self.hex.SetValue("#{0:02x}{1:02x}{2:02x}".format(self.red.GetValue(), self.green.GetValue(), self.blue.GetValue()))
        if dis == 1:
            self.hex.SetValue('#%x%x%x' % (display_colour[0], display_colour[1], display_colour[1]))
        else:
            self.hex.SetValue('#%x%x%x' % (element_colour[0], element_colour[1], element_colour[2]))


# def main():
# 	app=wx.App()
# 	frame=Frame(None)
# 	frame.Show()
# 	app.MainLoop()
# main()


# ........Change...Speed..........................................................


# .........Game...................................................................

class Frame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.InitUI()
        self.MenuBar()

        self.Show()
        self.SetSize((720, 486))
        self.SetSizeHints(720, 486, 720, 486)
        self.SetTitle('Tenis 1.0')

    def InitUI(self):

        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # ...........Score............................................................

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        font = wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        self.score = wx.StaticText(panel, label='00 | 00')
        self.score.SetFont(font)

        hbox2.Add(self.score)

        vbox.Add(hbox2, flag=wx.ALIGN_CENTRE | wx.TOP, border=10)

        # ..........Display..............................................................

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        self.display = wx.Panel(panel)
        self.display.SetBackgroundColour(display_colour)
        self.display.SetFocus()

        self.border = wx.Panel(self.display, pos=(349, 0), size=(2, 350))
        self.border.SetBackgroundColour(element_colour)

        hbox1.Add(self.display, 1, wx.EXPAND)

        vbox.Add(hbox1, 1, wx.EXPAND | wx.ALL, 10)

        # ..........Bats...........................................................

        self.bat1 = wx.Panel(self.display, pos=(685, 145), size=(15, 60))
        self.bat1.SetBackgroundColour(element_colour)

        self.bat2 = wx.Panel(self.display, pos=(0, 145), size=(15, 60))
        self.bat2.SetBackgroundColour(element_colour)

        # ..........Ball...........................................................

        self.ball = wx.Panel(self.display, pos=(20, 168), size=(15, 15))
        self.ball.SetBackgroundColour(element_colour)

        # ..........Buttons..................................................................

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        self.reset = wx.Button(panel, label='Reset', size=(100, -1))
        self.bb = wx.Button(panel, label='Get Ball', size=(100, -1))

        hbox3.Add(self.reset, flag=wx.RIGHT, border=20)
        hbox3.Add(self.bb)

        vbox.Add(hbox3, flag=wx.ALIGN_CENTRE | wx.BOTTOM, border=10)

        # ...........Set Sizer.................................................................

        panel.SetSizer(vbox)
        self.timer = wx.Timer(self)

        # ..............Events..........................................................

        self.Bind(wx.EVT_TIMER, self.OnTimer)

        self.display.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

        self.reset.Bind(wx.EVT_BUTTON, self.OnReset)
        self.bb.Bind(wx.EVT_BUTTON, self.GetBall)

        # self.display.Bind(wx.EVT_SIZE,self.OnSize)
        # self.display.Bind(wx.EVT_MOTION, self.OnMotion)

        self.bat1.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown1)
        self.bat1.Bind(wx.EVT_LEFT_UP, self.OnLeftUp1)

        self.bat2.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown2)
        self.bat2.Bind(wx.EVT_LEFT_UP, self.OnLeftUp2)

    # ...............Modules.........................................................

    # ...............On...Mouse...Move.........................................................

    def OnLeftDown1(self, e):
        global g, h
        g, h = e.GetPosition()

        self.bat1.Bind(wx.EVT_MOTION, self.OnMotion1)

    def OnLeftUp1(self, e):

        self.bat1.Unbind(wx.EVT_MOTION)

    def OnMotion1(self, e):

        a, b = self.GetPosition()
        c, d = 10, 97
        e, f = self.bat1.GetPosition()
        x, y = wx.GetMousePosition()

        self.bat1.SetPosition((e, y - b - d - h))

    def OnLeftDown2(self, e):
        global g, h
        g, h = e.GetPosition()

        self.bat2.Bind(wx.EVT_MOTION, self.OnMotion2)

    def OnLeftUp2(self, e):

        self.bat2.Unbind(wx.EVT_MOTION)

    def OnMotion2(self, e):

        a, b = self.GetPosition()
        c, d = 10, 97
        e, f = self.bat2.GetPosition()
        x, y = wx.GetMousePosition()

        self.bat2.SetPosition((e, y - b - d - h))

    # ...............OnSize.........................................................

    # def OnSize(self,e):
    # 	print('Display',self.display.GetSize())
    # 	print('Self',self.GetSize())

    # ...............OnKeyDown.............................................................

    def OnKeyDown(self, e):

        global tmr, ind_x, ind_y, pause

        codes = [315, 317, 65, 90, 32, 88]

        code = e.GetKeyCode()
        # print(code)
        if not code in codes:
            return

        move = 20

        a, b = self.bat1.GetPosition()
        c, d = self.bat2.GetPosition()

        x, y = self.ball.GetPosition()

        if code == 315:
            self.bat1.SetPosition((a, b - move))

            if x in range(660, 666):
                ind_y = 1

            if x == 665:
                self.ball.SetPosition((x, (self.bat1.GetPosition()[1] + 23)))

        if code == 317:
            self.bat1.SetPosition((a, b + move))

            if x in range(660, 666):
                ind_y = 0

            if x == 665:
                self.ball.SetPosition((x, (self.bat1.GetPosition()[1] + 23)))

        if code == 65:
            self.bat2.SetPosition((c, d - move))

            if x in range(20, 26):
                ind_y = 1

            if x == 20:
                self.ball.SetPosition((x, (self.bat2.GetPosition()[1] + 23)))

        if code == 90:
            self.bat2.SetPosition((c, d + move))

            if x in range(20, 26):
                ind_y = 0

            if x == 20:
                self.ball.SetPosition((x, (self.bat2.GetPosition()[1] + 23)))

        if code == 88:
            self.GetBall(None)

        if code == 32:

            if pause == 0:
                self.StartTimer()
            else:
                self.StopTimer()

    # w=87 #s=83 #up=315 down=31
    # z=90 a=65

    # ...............OnTimer.........................................................

    def OnTimer(self, e):

        global tmr, ind_x, ind_y

        x, y = self.ball.GetPosition()

        self.Borders()

        self.Go()

        if sc == 0:
            if x < -17 or x > 700:
                self.Score()

    # ...............Border.........................................................

    def Borders(self):

        global tmr, ind_x, ind_y

        x, y = self.ball.GetPosition()

        if y == 0:
            ind_y = 0
        if y == 335:
            ind_y = 1

    # ...............Border.........................................................

    def Go(self):

        global tmr, ind_x, ind_y

        a, b = self.bat2.GetPosition()
        c, d = self.bat1.GetPosition()

        f, g = self.display.GetSize()

        x, y = self.ball.GetPosition()

        if x == 665:
            if y in range(d - 20, d + 60):
                ind_x = 1

        if x == 20:
            if y in range(b - 20, b + 60):
                ind_x = 0

        l, h = 1, 1

        if ind_x == 1: l = -l
        if ind_y == 1: h = -h

        if x == 0:
            self.ball.SetPosition((x - 5, y + h))

        self.ball.SetPosition((x + l, y + h))

    # ..........Score.............................................................

    def Score(self):

        global tmr, ind_x, ind_y, pause, sc

        self.StopTimer()

        x, y = self.ball.GetPosition()

        a = int(self.score.GetLabel()[0])
        b = int(self.score.GetLabel()[1])
        c = int(self.score.GetLabel()[-2])
        d = int(self.score.GetLabel()[-1])

        if x < -15:
            d += 1
            if d == 10:
                d = 0
                c += 1

        if x > 700:
            b += 1
            if b == 10:
                b = 0
                a += 1

        self.score.SetLabel(f'{a}{b} | {c}{d}')

        sc = 1

    # ..........OnReset.............................................................

    def OnReset(self, e):

        global tmr, ind_x, ind_y, pause, sc

        self.StopTimer()

        self.bat1.SetPosition((685, 145))
        self.bat2.SetPosition((0, 145))

        x, y = self.ball.GetPosition()

        if x <= 350:
            self.ball.SetPosition((20, 168))
        if x > 350:
            self.ball.SetPosition((665, 168))

        self.score.SetLabel('00 | 00')

        sc = 0

    # ..........GetBall.............................................................

    def GetBall(self, e):

        global tmr, ind_x, ind_y, pause, sc

        self.StopTimer()

        # self.bat1.SetPosition((685,145))
        # self.bat2.SetPosition((0,145))

        x, y = self.ball.GetPosition()

        if x <= 350:
            self.ball.SetPosition((20, self.bat2.GetPosition()[1] + 23))

        if x > 350:
            self.ball.SetPosition((665, self.bat1.GetPosition()[1] + 23))

        sc = 0

    # ..........Timer.............................................................

    def StopTimer(self):

        global tmr, ind_x, ind_y, pause

        self.timer.Stop()
        tmr = 0
        pause = 0

    def StartTimer(self):

        global tmr, ind_x, ind_y, pause

        self.timer.Start(speed)
        tmr = 1
        pause = 1

    # ..........MenuBar............................................................

    def MenuBar(self):

        menubar = wx.MenuBar()

        customize = wx.Menu()
        self.ch_colour = customize.Append(wx.ID_ANY, '&Change colour\tCtrl+Z')
        self.ch_speed = customize.Append(wx.ID_ANY, '&Change speed\tCtrl+S')

        menubar.Append(customize, '&Customize')

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.ChColour, self.ch_colour)
        self.Bind(wx.EVT_MENU, self.ChSpeed, self.ch_speed)

    def ChColour(self, e):
        ChangeColour(self, self.display, self.ball, self.bat1, self.bat2, self.border)

    def ChSpeed(self, e):
        Speed(self)


# ....................Call the game....................................................

def main():
    app = wx.App()
    Frame(None)
    app.MainLoop()


if __name__ == "__main__":
    main()
