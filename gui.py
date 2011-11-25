import wx


class MyFrame(wx.Frame):
    """Main view of the program, it represents the main window.

    """

    def __init__(self, parent=None, id=-1, title="MarKuppY",
                 size=(500,500)):
        super(MyFrame, self).__init__(parent, id, title, size=size)
        
        # this is just to keep things cleaner
        self._create_menu()
        self._create_body()
        self._create_statusbar()
        
        self.Show()

    def _create_menu(self):
        """Place the widgets that constitute the menu of the
        application.

        """

        menubar = wx.MenuBar()
        
        filemenu = wx.Menu()
        # _b is to specify that it is a "button"
        quit_b = filemenu.Append(wx.ID_EXIT, '&Quit', "Quit application")
        
        editmenu = wx.Menu()
        cut_b = editmenu.Append(wx.ID_CUT, 'Cut')
        copy_b = editmenu.Append(wx.ID_COPY, 'Copy')
        paste_b = editmenu.Append(wx.ID_PASTE, 'Paste')
        
        menubar.Append(filemenu, "&File")
        menubar.Append(editmenu, "Edit")

        self.SetMenuBar(menubar)

        
    def _create_body(self):
        """Place the widgets that constitute the body of the
        application.

        """
        # Layout widgets
        body = wx.BoxSizer(wx.HORIZONTAL)
        convert_controls_box = wx.BoxSizer(wx.VERTICAL) 

        # Controls that will take the input
        textctrl_style = wx.TE_MULTILINE
        input_ctrl = wx.TextCtrl(self, style = textctrl_style)
        convert_button = wx.Button(self, label="Convert")
        format_combo = wx.ComboBox(self, choices=["HTML", "LaTeX"],
                                   style=wx.CB_READONLY)
        format_combo.SetStringSelection("HTML")
        
        output_ctrl = wx.TextCtrl(self, style = textctrl_style)

        
        # Adding the control widgets to the layout widgets
        convert_controls_box.Add(convert_button, proportion=2,
                                 flag=wx.EXPAND)
        convert_controls_box.Add(format_combo, proportion=1,
                                 flag=wx.EXPAND)
        
        body.Add(input_ctrl, proportion=2, flag=wx.EXPAND)
        body.Add(convert_controls_box,
                 proportion=1,
                 flag=wx.ALIGN_CENTER_VERTICAL)
        body.Add(output_ctrl, proportion=2, flag=wx.EXPAND)

        self.SetSizer(body)
        
    def _create_statusbar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')
        


if __name__ == '__main__':
    app = wx.App()
    fr = MyFrame()
    app.MainLoop()
    