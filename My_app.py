import wx
import wx.grid
class MyApp(wx.App):
    def OnInit(self):
        frame=wx.Frame(parent=None,title="自动化工具001",size=(500,600),pos=(1000,200))

        panel1 = wx.Panel(frame, -1,size=(600,40),pos=(0,1))
        panel1.SetBackgroundColour("#00000")
        panel1_button=wx.Button(panel1,-1,'删除',pos=(0,1),size=(39,39))
        panel1_button1 = wx.Button(panel1, -1, '播放', pos=(37, 1),size=(39,39))


        panel2 = wx.Panel(frame, -1, size=(600, 482), pos=(0, 41))
        panel2.SetBackgroundColour("#f3f7fa")
        panel2_button = wx.Button(panel2, -1, '新增行', pos=(0, 1), size=(85, 33))
        grid=wx.grid.Grid(panel2,-1,pos=(1,1),size=(600,500))
        grid.CreateGrid(30,5)
        grid.SetColLabelValue(0, "名称")
        grid.SetColLabelValue(1, "类型")
        grid.SetColLabelValue(2, "元素")
        grid.SetColLabelValue(3, "数据")
        grid.SetColLabelValue(4, "断言")


        panel3 = wx.Panel(frame, -1, size=(600, 37), pos=(0, 524))
        panel3.SetBackgroundColour("#f3f7fa")
        panel3_button = wx.Button(panel3, -1, '保存', pos=(0, 0), size=(484, 37))
        frame.Show()
        return True

    def button_start(self,event):
        pass

if __name__ == '__main__':
    app=MyApp()
    app.MainLoop()
