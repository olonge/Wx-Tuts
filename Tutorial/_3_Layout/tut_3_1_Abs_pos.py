# tut_3_1_Abs_pos.py
""" Not recommended """

import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(350, 300))

        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.panel = wx.Panel(self)

        self.panel.SetBackgroundColour("gray")

        self.LoadImages()

        self.mincol.SetPosition((20, 20))
        self.bardejov.SetPosition((40, 160))
        self.rotunda.SetPosition((170, 50))

    def LoadImages(self):
        self.mincol = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                      wx.Bitmap("./icons/graphics/mincol.jpg", wx.BITMAP_TYPE_ANY))

        self.bardejov = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                        wx.Bitmap("./icons/graphics/bardejov.jpg", wx.BITMAP_TYPE_ANY))

        self.rotunda = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                       wx.Bitmap("./icons/graphics/rotunda.jpg", wx.BITMAP_TYPE_ANY))


if __name__ == '__main__':
    app = wx.App()
    ex = Example(None, title='Absolute positioning')
    ex.Show()
    app.MainLoop()
