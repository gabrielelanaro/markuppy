import wx
from statemachine import MarkUp
import os


class MyFrame(wx.Frame):
    """Main view of the program, it represents the main window.

    """

    def __init__(self, parent=None, id=-1, title="MarKuppY",
                 size=(1000,500)):
        super(MyFrame, self).__init__(parent, id, title, size=size)

        # this is just to keep things cleaner
        self._create_menu()
        self._create_body()
        self._create_statusbar()
        
        # Binding
        self.convert_button.Bind(wx.EVT_BUTTON, self.OnConvertClick)
        self.Bind(wx.EVT_MENU, self.OnCopy, self.copy_me)
        self.Bind(wx.EVT_MENU, self.OnPaste, self.paste_me)
        self.Bind(wx.EVT_MENU, self.OnCut, self.cut_me)
        self.Bind(wx.EVT_MENU, self.OnOpen, self.open_me)
        self.Bind(wx.EVT_MENU, self.OnSaveIn, self.save_in_me)
        self.Bind(wx.EVT_MENU, self.OnSaveOut, self.save_out_me)
        self.Bind(wx.EVT_MENU, self.OnQuit, self.quit_me)
        self.Bind(wx.EVT_MENU, self.OnAboutBox, self.about_me)
        
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

        self.copy_me = copy_me
        self.paste_me = paste_me
        self.cut_me = cut_me
        self.open_me = open_me
        self.save_in_me = save_in_me
        self.save_out_me = save_out_me
        self.quit_me = quit_me
        
        helpmenu = wx.Menu()
        about_me = helpmenu.Append(wx.ID_ABOUT)
        
        self.about_me = about_me
        
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
        input_ctrl = self.input_ctrl = wx.TextCtrl(self, style = textctrl_style)
        convert_button = self.convert_button = wx.Button(self, label="Convert")
        self.format_combo = wx.ComboBox(self, choices=["HTML", "LaTeX"],
                                        style=wx.CB_READONLY)
        self.format_combo.SetStringSelection("HTML")
        
        output_ctrl = self.output_ctrl = wx.TextCtrl(self, style = textctrl_style)

        
        # Adding the control widgets to the layout widgets
        convert_controls_box.Add(convert_button, proportion=2,
                                 flag=wx.EXPAND|wx.FIXED_MINSIZE)
        convert_controls_box.Add(self.format_combo, proportion=1,
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
        
    def OnConvertClick(self, e):
        choice = self.format_combo.GetValue()
        in_text = self.input_ctrl.GetValue() 
        markup = MarkUp(in_text)
        out_text = markup.translate(format=choice)
        self.output_ctrl.ChangeValue(out_text)

    def OnOpen(self, e):
        dial = wx.FileDialog(self,message="Open an input file", defaultDir=".", style=wx.FD_OPEN)
        if dial.ShowModal() == wx.ID_OK:
            filename = dial.GetFilename()
            dirname = dial.GetDirectory()
            f = open(os.path.join(dirname, filename), 'r')
            self.input_ctrl.SetValue(f.read())
            f.close()
        dial.Destroy()

    def OnSaveIn(self, e):
        dial = wx.FileDialog(self, message="Save the input file", defaultDir=".", style=wx.FD_SAVE)
        if dial.ShowModal() == wx.ID_OK:
            filename = dial.GetFilename()
            dirname = dial.GetDirectory()
            value = self.input_ctrl.GetValue()
            f = open(os.path.join(dirname, filename), 'w')
            f.write(value)
            f.close()
        dial.Destroy()
        

    def OnSaveOut(self, e):
        dial = wx.FileDialog(self, message="Save the output file", defaultDir=".", style=wx.FD_SAVE)
        if dial.ShowModal() == wx.ID_OK:
            filename = dial.GetFilename()
            dirname = dial.GetDirectory()
            value = self.output_ctrl.GetValue()
            f = open(os.path.join(dirname, filename), 'w')
            f.write(value)
            f.close()
        dial.Destroy()

    def OnCopy(self, e):
        widget = self.FindFocus()
        copied = widget.GetStringSelection()
        if not wx.TheClipboard.IsOpened():  # may crash, otherwise
            do = wx.TextDataObject()
            do.SetText(copied)
            wx.TheClipboard.Open()
            wx.TheClipboard.SetData(do)
            wx.TheClipboard.Close()
        
    def OnPaste(self, e):
        widget = self.FindFocus()
        if not wx.TheClipboard.IsOpened():  # may crash, otherwise
            do = wx.TextDataObject()
            wx.TheClipboard.Open()
            success = wx.TheClipboard.GetData(do)
            wx.TheClipboard.Close()
            if success:
                widget.WriteText(do.GetText())

    def OnCut(self, e):
        widget = self.FindFocus()
        start,end = widget.GetSelection()
        
        if not wx.TheClipboard.IsOpened():  # may crash, otherwise
            do = wx.TextDataObject()
            do.SetText(widget.GetString(start, end))
            wx.TheClipboard.Open()
            wx.TheClipboard.SetData(do)
            wx.TheClipboard.Close()
            widget.Remove(start,end)

    def OnQuit(self, e):
        self.Close()
        
    def OnAboutBox(self, e):
        
        description = "\n".join(["Markuppy is a trivial application to convert a ",
                                "stupid (really stupid!) markup language in HTML",
                                "LaTeX and why not? -- Other formats."])

        licence = "Do what the fuck you like with this script"


        info = wx.AboutDialogInfo()

        info.SetIcon(wx.ArtProvider().GetIcon(wx.ART_HELP, size=(64,64)))
        info.SetName('Markuppy')
        info.SetVersion('0.1')
        info.SetDescription(description)
        info.SetCopyright('(C) 2011 Gabriele Lanaro')
        #info.SetWebSite('http://www.zetcode.com')
        info.SetLicence(licence)
        info.AddDeveloper('Gabriele Lanaro')
        info.AddDocWriter('Gabriele Lanaro')
        info.AddArtist('The Tango crew')
        #info.AddTranslator('Jan Bodnar')

        wx.AboutBox(info)
debug = True

if __name__ == '__main__':
    app = wx.App()
    fr = MyFrame()
    
    if debug:
        fr.input_ctrl.SetValue(open("test_input.txt").read())
    app.MainLoop()
    