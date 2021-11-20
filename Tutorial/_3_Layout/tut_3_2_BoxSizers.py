# tut_3_2_BoxSizers.py

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()

    def InitUI(self):
        panel = wx.Panel(self)

        # panel.SetBackgroundColour('#4f5049')
        panel.SetBackgroundColour('red')
        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#ededed')

        vbox.Add(midPan, wx.ID_ANY, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(vbox)


if __name__ == '__main__':
    app = wx.App()
    ex = Example(None, title='Border')
    ex.Show()
    app.MainLoop()