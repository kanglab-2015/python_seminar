import pylab as pl
import numpy as np
from scipy import signal

class Graph_master(object):
	def __init__(self,graph_type):
		self.graph_type=graph_type
		self.X = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
		self.Y=[]
	def write_graph(self):
		pl.plot(self.X,self.Y)
		pl.savefig(self.graph_type+'.png')
		pl.show()
	def set_graph(self):
		pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
		pl.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])
		ax = pl.gca()
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		ax.xaxis.set_ticks_position('bottom')
		ax.spines['bottom'].set_position(('data',0))
		ax.yaxis.set_ticks_position('left')
		ax.spines['left'].set_position(('data',0))

class Nokogiri(Graph_master):
	def __init__(self,graph_type):
		super(Nokogiri,self).__init__(graph_type)
	def graph(self):pytho
		self.Y = signal.sawtooth(self.X)

class Cos(Graph_master):
	def __init__(self,graph_type):
		super(Cos,self).__init__(graph_type)
	def graph(self):
		self.Y = np.cos(self.X)

class Sin(Graph_master):
	def __init__(self,graph_type):
		super(Sin,self).__init__(graph_type)
	def graph(self):
		self.Y = np.sin(self.X)