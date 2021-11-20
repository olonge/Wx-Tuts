# tut_2_2_menu_submenus.py

import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        m1 = fileMenu.Append(wx.ID_NEW, '&New')
        m2 = fileMenu.Append(wx.ID_OPEN, '&Open')
        m3 = fileMenu.Append(wx.ID_SAVE, '&Save')

        m1.SetBitmap(wx.Bitmap('../../icons/menu/tnew.png'))
        m2.SetBitmap(wx.Bitmap('../../icons/menu/topen.png'))
        m3.SetBitmap(wx.Bitmap('../../icons/menu/tsave.png'))
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        m4 = imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        m5 = imp.Append(wx.ID_ANY, 'Import bookmarks...')
        m6 = imp.Append(wx.ID_ANY, 'Import mail...')

        m4.SetBitmap(wx.Bitmap('../../icons/filemanager/folder.png'))
        m5.SetBitmap(wx.Bitmap('../../icons/filemanager/folder.png'))
        m6.SetBitmap(wx.Bitmap('../../icons/filemanager/folder.png'))
        fileMenu.Append(wx.ID_ANY, 'I&mport', imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        qmi.SetBitmap(wx.Bitmap('../../icons/menu/texit.png'))

        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((350, 250))
        self.SetTitle('Submenu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    ex = MyFrame(None)
    ex.Show()
    app.MainLoop()
