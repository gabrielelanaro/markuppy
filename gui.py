import wx
def mock_handler(*args):
    return

class MyFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title="MarKuppY",
                 size=(500,500)):
        super(MyFrame, self).__init__(parent, id, title, size=size)
        
        self.create_menu()
        self.create_body()
        
        self.Show()

    def create_menu(self):
        menubar = wx.MenuBar()
        
        filemenu = wx.Menu()
        quit = filemenu.Append(wx.ID_EXIT, '&Quit', "Quit application")
        
        editmenu = wx.Menu()
        cut = editmenu.Append(wx.ID_CUT, 'Cut')
        
        menubar.Append(filemenu, "&File")
        menubar.Append(editmenu, "Edit")
        
        self.SetMenuBar(menubar)

        
    def create_body(self):
        body = wx.BoxSizer(wx.HORIZONTAL)
        input_ctrl = wx.TextCtrl()
        output_ctrl = wx.TextCtrl()
        body.Add(input_ctrl)
        body.Add(output_ctrl)

        self.Add(body)
        
    def create_statusbar(self):
        return
        


if __name__ == '__main__':
    app = wx.App()
    fr = MyFrame()
    app.MainLoop()
    