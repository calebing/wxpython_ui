import wx
import wx.grid
class MyApp(wx.App):
    def OnInit(self):
        frame=wx.Frame(parent=None,title="Automated test application",size=(800,583),pos=(1000,200))

        panel1 = wx.Panel(frame, -1,size=(800,40),pos=(0,1))
        panel1.SetBackgroundColour("#00000")
        panel1_button=wx.Button(panel1,-1,'Delete',pos=(0,1),size=(49,39))
        panel1_button1 = wx.Button(panel1, -1, 'Play', pos=(50, 1),size=(49,39))


        panel2 = wx.Panel(frame, -1, size=(800, 466), pos=(0, 41))
        panel2.SetBackgroundColour("#f3f7fa")
        panel2_button = wx.Button(panel2, -1, 'Serial number', pos=(0, 1), size=(85, 33))
        grid=wx.grid.Grid(panel2,-1,pos=(1,1),size=(800,500))
        grid.CreateGrid(16,5)
        grid.SetDefaultColSize(140, resizeExistingCols=True)
        grid.SetDefaultRowSize(27, resizeExistingRows=True)
        grid.SetColLabelValue(0, "Element_name")
        grid.SetColLabelValue(1, "Action")
        grid.SetColLabelValue(2, "Element")
        grid.SetColLabelValue(3, "Data")
        grid.SetColLabelValue(4, "Assert")


        panel3 = wx.Panel(frame, -1, size=(800, 37), pos=(0, 507))
        panel3.SetBackgroundColour("#f3f7fa")
        panel3_button = wx.Button(panel3, -1, 'Save', pos=(0, 0), size=(800, 37))
        frame.Show()
        return True

    def button_start(self,event):
        pass

if __name__ == '__main__':
    app=MyApp()
    app.MainLoop()
