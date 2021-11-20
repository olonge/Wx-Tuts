# tut_2_3_menu_checkmenu.py
""" Big Icon Toolbars """

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        viewMenu = wx.Menu()

        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar',
                                    'Show Statusbar', kind=wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar',
                                    'Show Toolbar', kind=wx.ITEM_CHECK)

        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1, '', wx.Bitmap('../../icons/filemanager/home.png'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("Ready or not, here I come, you can't hide")

        self.SetSize((450, 350))
        self.SetTitle('Check menu item')
        self.Centre()

    def ToggleStatusBar(self, e):
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):
        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()


class MyFrame2(wx.Frame):
    """ Checking if Toolbar and RadioToolbars work """
    def __init__(self, parent, title):
        super(MyFrame2, self).__init__(parent, title=title)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        menu = wx.Menu()
        menubar.Append(menu, "File")
        self.SetMenuBar(menubar)

        tb = wx.ToolBar(self, -1)
        self.ToolBar = tb

        tb.AddTool(101, '',  wx.Bitmap('../../icons/filemanager/home.png'))
        tb.AddTool(102, '',  wx.Bitmap('../../icons/filemanager/folder.png'))

        right = tb.AddRadioTool(222, '', wx.Bitmap('../../icons/filemanager/terminal.png'))
        center = tb.AddRadioTool(333, '', wx.Bitmap('../../icons/filemanager/textedit.png'))
        justify = tb.AddRadioTool(444, '', wx.Bitmap('../../icons/filemanager/pdf.png'))

        tb.Bind(wx.EVT_TOOL, self.Onright)
        tb.Bind(wx.EVT_COMBOBOX, self.OnCombo)
        self.combo = wx.ComboBox(tb, 555, value="Times", choices=["Arial", "Times", "Courier"])

        tb.AddControl(self.combo)
        tb.Realize()
        self.SetSize((350, 250))

        self.text = wx.TextCtrl(self, -1, style=wx.EXPAND | wx.TE_MULTILINE)
        self.Centre()
        self.Show(True)

    def Onright(self, event):
        self.text.AppendText(str(event.GetId()) + "\n")

    def OnCombo(self, event):
        self.text.AppendText(self.combo.GetValue() + "\n")


if __name__ == '__main__':
    app = wx.App()
    ex = MyFrame2(None, 'A Title')
    ex.Show()
    app.MainLoop()
