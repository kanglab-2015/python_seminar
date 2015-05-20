# -*- coding: utf-8 -*-

import Image
import wx
import wx.animate
import Tkinter
import tkFileDialog
import os
import string

class Gif_view(wx.Panel):
    def __init__(self, parent, id, filename):
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("white")
        ag = wx.animate.GIFAnimationCtrl(self, id, filename, pos=(10, 10))
        ag.GetPlayer().UseBackgroundColour(True)
        ag.Play()

    @classmethod
    def gif_save(self, filename, im):
        try:
            while True:
                im.save(r'./anime/'+unicode(filename.replace("/","").strip(os.getcwd().replace("\\", " ")+".Gifg"))+"_"+str(im.tell())+'.png')
                im.seek(im.tell()+1)
        except EOFError:
            pass

if __name__ == "__main__":

    root=Tkinter.Tk()
    root.withdraw()
    ftype = [('img file','*.gif')]
    iDir='./'
    filename=tkFileDialog.askopenfilename(filetypes = ftype,initialdir = iDir)
    app = wx.App()
    im = Image.open(filename)
    frame = wx.Frame(None, -1, "view_gif", size = im.size)
    Gif_view(frame, -1, filename)
    frame.Show(True)
    app.MainLoop()
    Gif_view.gif_save(filename, im)
