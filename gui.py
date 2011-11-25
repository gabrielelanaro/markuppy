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
        
        self.SetMinSize(size) # To prevent collapsing the window when
                              # resizing
        self.Show()

    def _create_menu(self):
        """Place the widgets that constitute the menu of the
        application.

        """

        menubar = wx.MenuBar()
        
        filemenu = wx.Menu()
        # _me is to specify that it is a "menu entry"
        open_me = filemenu.Append(wx.ID_OPEN)
        save_in_me = filemenu.Append(wx.ID_ANY, "Save In")
        save_out_me = filemenu.Append(wx.ID_ANY, "Save Out")
        quit_me = filemenu.Append(wx.ID_EXIT)
        
        
        editmenu = wx.Menu()
        cut_me = editmenu.Append(wx.ID_CUT)
        copy_me = editmenu.Append(wx.ID_COPY)
        paste_me = editmenu.Append(wx.ID_PASTE)

        helpmenu = wx.Menu()
        manual_me = helpmenu.Append(wx.ID_HELP, 'Manual')
        about_me = helpmenu.Append(wx.ID_ABOUT)
        
        menubar.Append(filemenu, "&File")
        menubar.Append(editmenu, "Edit")
        menubar.Append(helpmenu, "Help")
        
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
                                 flag=wx.EXPAND|wx.FIXED_MINSIZE)
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
    