# tut_4_1_Move
""" This is a wx.MoveEvent event demonstration.
Dynamically display the window's coordinates inside it """

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        wx.StaticText(self, label='x:', pos=(10,10))
        wx.StaticText(self, label='y:', pos=(10,30))

        self.st1 = wx.StaticText(self, label='', pos=(30, 10))
        self.st2 = wx.StaticText(self, label='', pos=(30, 30))

        self.Bind(wx.EVT_MOVE, self.OnMove)

        self.SetSize((350, 250))
        self.SetTitle('Move event')
        self.Centre()

    def OnMove(self, e):
        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))


if __name__ == '__main__':
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()