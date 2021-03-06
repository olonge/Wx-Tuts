# tut_4_2_veto
""" In this example we veto an event. """

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        self.SetTitle('Event veto')
        self.Centre()

    def OnCloseWindow(self, e):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy() # not Close, otherwise infinite loop
        else:
            e.Veto()


if __name__ == '__main__':
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()