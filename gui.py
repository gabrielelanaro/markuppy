import wx

def mock_handler(*args):
    return

class MyFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title="MarKuppY",
                 size=(500,500)):
        super(MyFrame, self).__init__(parent, id, title, size=size)
        
        self._create_menu()
        self._create_body()
        
        self.Show()

    def _create_menu(self):
        menubar = wx.MenuBar()
        
        filemenu = wx.Menu()
        quit = filemenu.Append(wx.ID_EXIT, '&Quit', "Quit application")
        
        editmenu = wx.Menu()
        cut = editmenu.Append(wx.ID_CUT, 'Cut')
        
        menubar.Append(filemenu, "&File")
        menubar.Append(editmenu, "Edit")
        
        self.SetMenuBar(menubar)

        
    def _create_body(self):
        body = wx.BoxSizer(wx.HORIZONTAL)
        convert_controls_box = wx.BoxSizer(wx.VERTICAL) 

        
        textctrl_style = wx.TE_MULTILINE
        input_ctrl = wx.TextCtrl(self, style = textctrl_style)
        convert_button = wx.Button(self, label="Convert")
        format_combo = wx.ComboBox(self, choices=["HTML", "LaTeX"],
                                   style=wx.CB_READONLY)
        format_combo.SetStringSelection("HTML")
        
        output_ctrl = wx.TextCtrl(self, style = textctrl_style)

        
        
        convert_controls_box.Add(convert_button, proportion=1,
                                 flag=wx.EXPAND)
        convert_controls_box.Add(format_combo, proportion=1,
                                 flag=wx.EXPAND)
        
        body.Add(input_ctrl, proportion=1, flag=wx.EXPAND)
        body.Add(convert_controls_box,
                 proportion=1,
                 flag=wx.ALIGN_CENTER_VERTICAL)
        body.Add(output_ctrl, proportion=1, flag=wx.EXPAND)

        self.SetSizer(body)
        
    def create_statusbar(self):
        return
        


if __name__ == '__main__':
    app = wx.App()
    fr = MyFrame()
    app.MainLoop()
    