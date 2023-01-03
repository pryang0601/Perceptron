import wx
import wx.xrc
import numpy as np
import matplotlib.pyplot as plt
import HW1_logic
class MyFrame1 ( wx.Frame ):
	inputs=[]
	settings=[]
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,600 ), 0 )
		self.Data = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,600 ), wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 5, 7, 0, 3 )

		self.m_staticText62 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		self.m_staticText62.Hide()

		gSizer3.Add( self.m_staticText62, 0, wx.ALL, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self.Data, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		self.m_choice1.Hide()

		gSizer3.Add( self.m_choice1, 0, wx.ALIGN_LEFT|wx.ALL, 5 )

		self.m_staticText64 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )

		self.m_staticText64.Hide()

		gSizer3.Add( self.m_staticText64, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_staticText105 = wx.StaticText( self.Data, wx.ID_ANY, u"Perceptron", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText105.Wrap( -1 )

		self.m_staticText105.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Krungthep" ) )

		gSizer3.Add( self.m_staticText105, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText65 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )

		self.m_staticText65.Hide()

		gSizer3.Add( self.m_staticText65, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self.Data, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,25 ), 0 )
		self.m_textCtrl7.Hide()

		gSizer3.Add( self.m_textCtrl7, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_button3 = wx.Button( self.Data, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.Hide()

		gSizer3.Add( self.m_button3, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_staticText66 = wx.StaticText( self.Data, wx.ID_ANY, u"DataSet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )

		self.m_staticText66.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lao MN" ) )

		gSizer3.Add( self.m_staticText66, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		data_comChoices = [ u"2Ccircle1.txt", u"2Circle1.txt", u"2CloseS.txt", u"2CloseS2.txt", u"2CloseS3.txt", u"2cring.txt", u"2CS.txt", u"2Hcircle1.txt", u"2ring.txt", u"perceptron1.txt", u"perceptron2.txt", u"5CloseS1.txt", u"xor.txt" ]
		self.data_com = wx.Choice( self.Data, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), data_comChoices, 0 )
		self.data_com.SetSelection( 0 )
		gSizer3.Add( self.data_com, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT|wx.ALL, 5 )

		self.m_staticText68 = wx.StaticText( self.Data, wx.ID_ANY, u"Learning Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		self.m_staticText68.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lao MN" ) )

		gSizer3.Add( self.m_staticText68, 0, wx.ALIGN_LEFT|wx.ALL, 5 )

		self.LearnRateT = wx.TextCtrl( self.Data, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,20 ), 0 )
		gSizer3.Add( self.LearnRateT, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_staticText70 = wx.StaticText( self.Data, wx.ID_ANY, u"Epoch", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )

		self.m_staticText70.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lao MN" ) )

		gSizer3.Add( self.m_staticText70, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.EpochT = wx.TextCtrl( self.Data, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,20 ), 0 )
		gSizer3.Add( self.EpochT, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.StartB = wx.Button( self.Data, wx.ID_ANY, u"Start Training", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.StartB, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_staticText73 = wx.StaticText( self.Data, wx.ID_ANY, u"Training Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )

		self.m_staticText73.SetFont( wx.Font( 15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lao MN" ) )

		gSizer3.Add( self.m_staticText73, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.TrainR = wx.TextCtrl( self.Data, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,200 ), wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL )
		gSizer3.Add( self.TrainR, 0, wx.ALIGN_LEFT|wx.ALL, 5 )

		self.m_staticText74 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )

		self.m_staticText74.Hide()

		gSizer3.Add( self.m_staticText74, 0, wx.ALL, 5 )

		self.m_staticText75 = wx.StaticText( self.Data, wx.ID_ANY, u"Testing Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )

		self.m_staticText75.SetFont( wx.Font( 15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lao MN" ) )

		gSizer3.Add( self.m_staticText75, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.TestR = wx.TextCtrl( self.Data, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,200 ), wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL )
		gSizer3.Add( self.TestR, 0, wx.ALL, 5 )

		self.m_staticText77 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )

		self.m_staticText77.Hide()

		gSizer3.Add( self.m_staticText77, 0, wx.ALL, 5 )

		self.m_staticText78 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )

		self.m_staticText78.Hide()

		gSizer3.Add( self.m_staticText78, 0, wx.ALL, 5 )

		self.m_staticText79 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		self.m_staticText79.Hide()

		gSizer3.Add( self.m_staticText79, 0, wx.ALL, 5 )

		self.m_staticText80 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		self.m_staticText80.Hide()

		gSizer3.Add( self.m_staticText80, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		self.m_staticText81.Hide()

		gSizer3.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.m_staticText82 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		self.m_staticText82.Hide()

		gSizer3.Add( self.m_staticText82, 0, wx.ALL, 5 )

		self.m_staticText83 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		self.m_staticText83.Hide()

		gSizer3.Add( self.m_staticText83, 0, wx.ALL, 5 )

		self.m_staticText84 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		self.m_staticText84.Hide()

		gSizer3.Add( self.m_staticText84, 0, wx.ALL, 5 )

		self.m_staticText85 = wx.StaticText( self.Data, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		self.m_staticText85.Hide()

		gSizer3.Add( self.m_staticText85, 0, wx.ALL, 5 )

		self.m_staticText99 = wx.StaticText( self.Data, wx.ID_ANY, u"Training  Accuracy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )

		self.m_staticText99.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lao MN" ) )

		gSizer3.Add( self.m_staticText99, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )

		self.Trainacc = wx.TextCtrl( self.Data, wx.ID_ANY, wx.EmptyString, wx.Point( 50,20 ), wx.Size( 80,20 ), 0 )
		gSizer3.Add( self.Trainacc, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_staticText101 = wx.StaticText( self.Data, wx.ID_ANY, u"Testing Accuracy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lao MN" ) )

		gSizer3.Add( self.m_staticText101, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.Testacc = wx.TextCtrl( self.Data, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,20 ), 0 )
		gSizer3.Add( self.Testacc, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_staticText103 = wx.StaticText( self.Data, wx.ID_ANY, u"Weight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText103.Wrap( -1 )

		self.m_staticText103.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lao MN" ) )

		gSizer3.Add( self.m_staticText103, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.Weight = wx.TextCtrl( self.Data, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,20 ), 0 )
		gSizer3.Add( self.Weight, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.Data.SetSizer( gSizer3 )
		self.Data.Layout()
		self.m_notebook1.AddPage( self.Data, u"DATA", True )
		self.Graph = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 0, 1, 0, 0 )

		self.graph = wx.StaticBitmap( self.Graph, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
		gSizer2.Add( self.graph, 0, wx.ALL, 5 )

		self.Graph.SetSizer( gSizer2 )
		self.Graph.Layout()
		gSizer2.Fit( self.Graph )
		self.m_notebook1.AddPage( self.Graph, u"GRAPH", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.StartB.Bind( wx.EVT_BUTTON, self.StoTrain )
		# self.Show()
		
	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def StoTrain( self,event):
		data_index=self.data_com.GetSelection()
		dataset=self.data_com.GetString(data_index)
		lrate=float(self.LearnRateT.GetValue())
		e=int(self.EpochT.GetValue())
		self.inputs.extend([dataset,lrate,e])
		self.settings=HW1_logic.Open(dataset)	#[X,Y,Z,train_X,test_X,train_Y,test_Y,train_Z,test_Z,train_size,test_size]
		x=self.settings[0]
		y=self.settings[1]
		z=self.settings[2]
		maxv=max(z)
		minv=min(z)
		train_x=self.settings[3]
		train_y=self.settings[5]
		train_z=self.settings[7]
		trainsize=self.settings[9]
		Train_Value=HW1_logic.MainTrain(z,train_x,train_y,train_z,trainsize,lrate,e)		#start training
		self.TrainR.LoadFile("Training.txt")
		w=Train_Value[0]
		train_correct=Train_Value[1]
		test_x=self.settings[4]
		test_y=self.settings[6]
		test_z=self.settings[8]
		testsize=self.settings[10]
		test_correct=HW1_logic.MainTest(testsize,test_x,test_y,test_z,maxv,minv,w)
		self.TestR.LoadFile("Testing.txt")
		self.Trainacc.write(str(round(float(train_correct/trainsize),3)))
		self.Testacc.write(str(round(float(test_correct/testsize),3)))
		self.Weight.write(str(w))
		HW1_logic.Plot(w,x,y,z,maxv)
		bmp=wx.Bitmap("Perceptron.png",wx.BITMAP_TYPE_ANY)
		self.graph.SetBitmap(bmp)
		#self.graph.SetPosition(100,100)


if __name__ == '__main__':
	app = wx.App()
	frm = MyFrame1(None)
	frm.Show()
	app.MainLoop()
