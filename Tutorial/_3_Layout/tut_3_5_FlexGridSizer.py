# tut_3_5_FlexGridSizer

import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(rows=3, cols=2, vgap=9, hgap=25)

        title = wx.StaticText(panel, label="Title")
        author = wx.StaticText(panel, label="Author")
        review = wx.StaticText(panel, label="Review")

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        fgs.AddMany([
            title, (tc1, 1, wx.EXPAND),
            author, (tc2, 1, wx.EXPAND),
            (review, 1, wx.EXPAND), (tc3, 1, wx.EXPAND)
        ])

        fgs.AddGrowableRow(idx=2, proportion=1)
        fgs.AddGrowableCol(idx=1, proportion=1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)


if __name__ == '__main__':
    app = wx.App()
    ex = Example(None, title='Review')
    ex.Show()
    app.MainLoop()
