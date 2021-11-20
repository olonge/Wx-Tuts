# tut_2_1_menu_icons.py

import wx

APP_EXIT = 1


class MyFrame1(wx.Frame):
    """ Icon & shortcut does not work """
    def __init__(self, *args, **kwargs):
        super(MyFrame1, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


class MyFrame2(wx.Frame):
    """ Icon & shortcut works! """
    def __init__(self, *args, **kwargs):
        super(MyFrame2, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('../../icons/menu/exit.png'))

        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((350, 250))
        self.SetTitle('Icons and shortcuts')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    ex = MyFrame2(None)
    ex.Show()
    app.MainLoop()
