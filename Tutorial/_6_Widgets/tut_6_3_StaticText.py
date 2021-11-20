# tut_6_3_StaticText.py
""" A wx.StaticText widget displays one or more lines of read-only text. """

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        txt1 = '''I'm giving up the ghost of love
in the shadows cast on devotion
She is the one that I adore
creed of my silent suffocation
Break this bittersweet spell on me
lost in the arms of destiny'''

        txt2 = '''There is something in the way
You're always somewhere else
Feelings have deserted me
To a point of no return
I don't believe in God
But I pray for you'''

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)

        st1 = wx.StaticText(pnl, label=txt1, style=wx.ALIGN_LEFT)
        wx.StaticLine(pnl, pos=(15, 140), size=(255, 1))
        st2 = wx.StaticText(pnl, label=txt2, style=wx.ALIGN_LEFT)

        st1.SetFont(font)
        st2.SetFont(font)

        vbox.Add(st1, flag=wx.ALL, border=15)
        vbox.Add(st2, flag=wx.ALL, border=15)

        pnl.SetSizer(vbox)

        self.SetTitle('Bittersweet')
        self.SetSize((300, 350))
        self.SetMinSize((300, 330))
        self.SetMaxSize((325, 400))

        # self.SetSizerAndFit()
        self.Centre()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

