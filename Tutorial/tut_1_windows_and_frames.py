# tut_1_windows_frames.py

import wx


def run_1():
    app = wx.App()

    frame = wx.Frame(None, title='Simple application')
    frame.Show()

    app.MainLoop()


def run(i = 0):
    app = wx.App()

    # styles = {wx.MAXIMIZE_BOX:'', wx.RESIZE_BORDER:'', wx.SYSTEM_MENU:'', wx.CAPTION:'', wx.CLOSE_BOX:''}
    frame = wx.Frame(None, style=wx.CLOSE_BOX)
    frame.Show()
    frame.Center()

    app.MainLoop()
