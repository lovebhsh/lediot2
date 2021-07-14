# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LedControl
###########################################################################

class LedControl ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LED 제어기 by 전형기 ver 1.0", pos = wx.DefaultPosition, size = wx.Size( 300,100 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_led_on = wx.Button( self, wx.ID_ANY, u"LED를 켜자", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn_led_on.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.btn_led_on.SetBackgroundColour( wx.Colour( 255, 73, 4 ) )

        bSizer1.Add( self.btn_led_on, 1, wx.ALL|wx.EXPAND, 5 )

        self.btn_led_off = wx.Button( self, wx.ID_ANY, u"LED를 끄자", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn_led_off.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.btn_led_off.SetForegroundColour( wx.Colour( 0, 24, 138 ) )
        self.btn_led_off.SetBackgroundColour( wx.Colour( 67, 202, 231 ) )

        bSizer1.Add( self.btn_led_off, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btn_led_on.Bind( wx.EVT_BUTTON, self.led_on )
        self.btn_led_off.Bind( wx.EVT_BUTTON, self.led_off )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def led_on( self, event ):
        event.Skip()

    def led_off( self, event ):
        event.Skip()



