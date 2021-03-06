# tut_4_3_propagation
""" This example demonstrates event propagation. """

import wx


class MyButton(wx.Button):
    def __init__(self, *args, **kw):
        super(MyButton, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):
        print('event reached button class')
        e.Skip()  # propagates the event further to to panel class.
        print('event left button class')
        pass


class MyPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(MyPanel, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):
        print('event reached panel class')
        e.Skip()  # propagates the event further to to frame class.
        print('event left panel class')


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        mpnl = MyPanel(self)

        MyButton(mpnl, label='Ok', pos=(15, 15))

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        self.SetTitle('Propagate event')
        self.Centre()

    def OnButtonClicked(self, e):
        print('event reached frame class')
        e.Skip() # propagates the event further to where ?.
        print('event left frame class')


if __name__ == '__main__':
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
