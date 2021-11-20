# tut_6_7_CheckBox.py
""" CheckBox - On-Off toggle """

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)

        vbox = wx.BoxSizer(wx.HORIZONTAL)

        cb = wx.CheckBox(pnl, label='Show title')
        cb.SetValue(True)
        cb.Bind(wx.EVT_CHECKBOX, self.ShowOrHideTitle)

        vbox.Add(cb, flag=wx.TOP|wx.LEFT, border=30)

        pnl.SetSizer(vbox)

        self.SetTitle('wx.CheckBox')
        self.Centre()

    def ShowOrHideTitle(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()

        if isChecked:
            self.SetTitle('wx.CheckBox')
        else:
            self.SetTitle('')


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
