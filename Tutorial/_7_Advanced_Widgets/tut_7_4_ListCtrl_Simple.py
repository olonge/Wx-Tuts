# tut_7_4_ListCtrl_Simple.py
""" Styles:
wx.LC_LIST
wx.LC_REPORT **
wx.LC_VIRTUAL
wx.LC_ICON
wx.LC_SMALL_ICON
wx.LC_ALIGN_LEFT
wx.LC_EDIT_LABELS
wx.LC_NO_HEADER
wx.LC_SORT_ASCENDING
wx.LC_SORT_DESCENDING
wx.LC_HRULES
wx.LC_VRULES
"""

import wx

data = [('Jessica Alba', 'Pomona', '1981'), ('Sigourney Weaver', 'New York', '1949'),
  ('Angelina Jolie', 'los angeles', '1975'), ('Natalie Portman', 'Jerusalem', '1981'),
  ('Rachel Weiss', 'London', '1971'), ('Scarlett Johansson', 'New York', '1984')]


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self)

        self.list = wx.ListCtrl(panel, wx.ID_ANY, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'name', width=140)
        self.list.InsertColumn(1, 'place', width=130)
        self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

        idx = 0

        for i in data:

            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])
            idx += 1

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.SetTitle('Actresses')
        self.Centre()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
