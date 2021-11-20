# tut_2_5_toolbars.py

import wx


class Example1(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example1, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        toolbar = self.CreateToolBar()
        qtool = toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('./icons/menu/texit.png'))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetSize((350, 250))
        self.SetTitle('Simple toolbar')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar1 = wx.ToolBar(self)
        tnew = toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('../../icons/menu/tnew.png'))
        topen = toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('../../icons/menu/topen.png'))
        tsave = toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('../../icons/menu/tsave.png'))
        toolbar1.Realize()

        toolbar2 = wx.ToolBar(self)
        qtool = toolbar2.AddTool(wx.ID_EXIT, '', wx.Bitmap('../../icons/menu/texit.png'))
        toolbar2.Realize()

        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.Add(toolbar2, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, lambda x: print(f"You called new"), tnew)
        self.Bind(wx.EVT_TOOL, lambda x: print(f"You called open"), topen)
        self.Bind(wx.EVT_TOOL, lambda x: print(f"You called save"), tsave)
        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetSizer(vbox)

        self.SetSize((350, 250))
        self.SetTitle('Toolbars')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()