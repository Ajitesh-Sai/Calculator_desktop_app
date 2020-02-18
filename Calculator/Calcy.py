import wx
import Calcx

def press_add(event):
    a = float(input1_box.GetValue())
    b = float(input2_box.GetValue())
    result.SetLabel(str(Calcx.add(a,b)))

def press_sub(event):
    a = float(input1_box.GetValue())
    b = float(input2_box.GetValue())
    result.SetLabel(str(Calcx.sub(a,b)))

def press_mult(event):
    a = float(input1_box.GetValue())
    b = float(input2_box.GetValue())
    result.SetLabel(str(Calcx.mult(a,b)))

def press_div(event):
    a = float(input1_box.GetValue())
    b = float(input2_box.GetValue())
    result.SetLabel(str(Calcx.div(a,b)))

def press_mod(event):
    a = float(input1_box.GetValue())
    b = float(input2_box.GetValue())
    result.SetLabel(str(Calcx.mod(a,b)))

def press_exp(event):
    a = int(input1_box.GetValue())
    b = int(input2_box.GetValue())
    result.SetLabel(str(Calcx.exp(a,b)))



app=wx.App()
frame= wx.Frame(parent=None,title='Calculator')
panel=wx.Panel(frame)
sizer=wx.GridBagSizer()

input1_label=wx.StaticText(panel,label="Input #1 : ")
input1_box=wx.TextCtrl(panel)
input2_label=wx.StaticText(panel,label='Input #2 : ')
input2_box=wx.TextCtrl(panel)
result_label=wx.StaticText(panel,label='Result : ')
result=wx.StaticText(panel,label="")

add_b= wx.Button(panel,label="+")
sub_b= wx.Button(panel,label="-")
mult_b= wx.Button(panel,label="*")
div_b= wx.Button(panel,label="/")
exp_b= wx.Button(panel,label="^")
mod_b= wx.Button(panel,label="%")

add_b.Bind(wx.EVT_BUTTON,press_add)
sub_b.Bind(wx.EVT_BUTTON,press_sub)
mult_b.Bind(wx.EVT_BUTTON,press_mult)
div_b.Bind(wx.EVT_BUTTON,press_div)
exp_b.Bind(wx.EVT_BUTTON,press_exp)
mod_b.Bind(wx.EVT_BUTTON,press_mod)

sizer.Add(input1_label, (0,0))
sizer.Add(input1_box,(0,1))
sizer.Add(input2_label, (1,0))
sizer.Add(input2_box,(1,1))
sizer.Add(add_b,(2,0))
sizer.Add(sub_b,(2,1))
sizer.Add(exp_b,(2,2))
sizer.Add(mod_b,(2,3))
sizer.Add(mult_b,(3,0))
sizer.Add(div_b,(3,1))
sizer.Add(result_label,(5,0))
sizer.Add(result,(5,1))

panel.SetSizerAndFit(sizer)
frame.SetSizerAndFit(sizer)
frame.Show()
app.MainLoop()