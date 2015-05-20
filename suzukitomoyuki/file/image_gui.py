# -*- coding: utf-8 -*-

import cv2
import sys
import os
import glob
import pylab as plt
import copy
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Image(QDialog):

    def __init__(self, parent=None):
        super(Image, self).__init__(parent)
        self.img = []
        self.gray = []
        self.face = []
        self.initUI()

    def initUI(self):

        self.resize(200,200)
        self.setWindowTitle(u"画像変換")

        button1 = QPushButton('Open Image File')
        button1.setGeometry(50, 25, 100, 50)
        self.connect(button1, SIGNAL('clicked()'), self.open_img)

        button2 = QPushButton(u'グレースケール変換')
        button2.setGeometry(50, 25, 100, 50)
        self.connect(button2, SIGNAL('clicked()'), self.gray_image)

        button3 = QPushButton(u'ガウシアンフィルタ')
        button3.setGeometry(50, 25, 100, 50)
        self.connect(button3, SIGNAL('clicked()'), self.gauss_f)

        button4 = QPushButton(u'顔認識')
        button4.setGeometry(50, 25, 100, 50)
        self.connect(button4, SIGNAL('clicked()'), self.face_know)

        button5 = QPushButton(u'トリミング')
        button5.setGeometry(50, 25, 100, 50)
        self.connect(button5, SIGNAL('clicked()'), self.trimming)

        button6 = QPushButton(u'２値化')
        button6.setGeometry(50, 25, 100, 50)
        self.connect(button6, SIGNAL('clicked()'), self.threshold_im)

        button7 = QPushButton(u'ヒストグラム')
        button7.setGeometry(50, 25, 100, 50)
        self.connect(button7, SIGNAL('clicked()'), self.hist_g)

        button8 = QPushButton(u'モザイク加工')
        button8.setGeometry(50, 25, 100, 50)
        self.connect(button8, SIGNAL('clicked()'), self.mozaiku)

        lab1 = QLabel(u'分配器選択')
        lab1.setGeometry(50, 25, 100, 50)

        self.combo1 = QComboBox()
        self.combo1.addItems(glob.glob("./*.xml"))

        vbox = QVBoxLayout()

        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button6)
        vbox.addWidget(button7)
        vbox.addWidget(button3)
        vbox.addWidget(button4)
        vbox.addWidget(button5)
        vbox.addWidget(button8)
        vbox.addWidget(lab1)
        vbox.addWidget(self.combo1)

        self.setLayout(vbox)

    def open_img(self):
        self.fname = unicode(QFileDialog.getOpenFileName(self,'Open file','*.jpg;*.png'))
        self.img = cv2.imread(self.fname)
        cv2.imshow("%s" % self.fname, self.img)

    def gray_image(self):
        self.gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray",self.gray)

    def gauss_f(self):
        im_g = cv2.GaussianBlur(self.img,(21,21),0)
        cv2.imshow("gauss",im_g)

    def face_know(self):
        cascade = cv2.CascadeClassifier(unicode(self.combo1.currentText()))
        f_im = copy.deepcopy(self.img)
        self.face = cascade.detectMultiScale(f_im,1.1,3)
        for (x,y,w,h) in self.face:
            cv2.rectangle(f_im,(x,y),(x+w,y+h),(0,50,255),3)
        cv2.imshow("face_know",f_im)

    def trimming(self):
        self.face_know()
        for (x,y,w,h) in self.face:
            im_trim = self.img[y:y+h,x:x+w]
            cv2.imshow("trimming("+str(x)+","+str(y)+")",im_trim)

    def threshold_im(self):
        self.gray_image()
        #判別分析法
        th,t_im = cv2.threshold(self.gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        print u"閾値:"+str(th)
        cv2.imshow("threshold",t_im)

    def hist_g(self):
        hist = cv2.calcHist([self.img],[0],None,[256],[0,256])
        plt.plot(hist)
        plt.xlim([0,256])
        plt.show()

    def mozaiku(self):
        self.face_know()
        im_m = copy.deepcopy(self.img)
        for (x, y, w, h) in self.face:
            im_temp = im_m[y:y+h, x:x+w]
            im_temp = cv2.resize(im_temp, (w/10, h/10))
            im_temp = cv2.resize(im_temp, (w, h), interpolation=cv2.cv.CV_INTER_NN)
            im_m[y:y+h, x:x+w] = im_temp
        cv2.imshow("mozaiku",im_m)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wi = Image()
    wi.show()
    app.exec_()