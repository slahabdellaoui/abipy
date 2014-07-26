"""Collections of simple frames used to solve typical (simple) problems."""
from __future__ import print_function, division

import wx

from abipy.gui.awx.core import Frame as awxFrame

__all__ = [
    "FrameWithChoice",
]


class FrameWithChoice(awxFrame):
    """
    Simple frame with a Choice control and two buttons: OK, Cancel
    Subclasses will usually redefine onOkButton.
    """
    def __init__(self, parent, choices, **kwargs):
        super(FrameWithChoice, self).__init__(parent, id=-1, **kwargs)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        panel = wx.Panel(self, -1)
        main_sizer.Add(panel, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, border=5)

        self.wxchoices = wx.Choice(self, -1, wx.DefaultPosition, wx.DefaultSize, list(choices), 0)
        self.wxchoices.SetSelection(0)

        main_sizer.Add(self.wxchoices, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, border=5)

        ok_button = wx.Button(self, wx.ID_OK, label='Ok')
        ok_button.Bind(wx.EVT_BUTTON, self.onOkButton)

        close_button = wx.Button(self, wx.ID_CANCEL, label='Cancel')
        close_button.Bind(wx.EVT_BUTTON, self.onCloseButton)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(ok_button)
        hbox.Add(close_button, flag=wx.LEFT, border=5)

        main_sizer.Add(hbox, flag=wx.ALIGN_CENTER | wx.ALL | wx.EXPAND)

        self.SetSizerAndFit(main_sizer)

    def getChoice(self):
        """Returns the string selected by the user."""
        return self.wxchoices.GetStringSelection()

    def onOkButton(self, event):
        print("In onOkButton with choice selected %s" % self.wxchoices.GetStringSelection())

    def onCloseButton(self, event):
        self.Destroy()


if __name__ == "__main__":
    app = wx.App()
    FrameWithChoice(None, ["hello", "ciao"]).Show()
    app.MainLoop()
