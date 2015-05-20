# coding:utf-8 

import factory
class YakuzaFactory(factory.Factory):
	def createGroup(self,group_name):
		return YakuzaGroup(group_name)
	def createName(self,name):
		return YakuzaName(name)
	def createPosition(self,position):
		return YakuzaPosition(position)

class YakuzaGroup(factory.Group):
	def __init__(self,group_name):
		super(YakuzaGroup,self).__init__(group_name)
	def makeList(self):
		self.buffer = []
		self.buffer.append(self.group_name+'組')
		for item in self.content:
			self.buffer.append(item.makeList())
		return "".join(self.buffer)

class YakuzaName(factory.Name):
	def __init__(self,name):
		super(YakuzaName,self).__init__(name)
	def makeList(self):
		return "\n"+self.name

class YakuzaPosition(factory.Position):
	def __init__(self,position):
		super(YakuzaPosition,self).__init__(position)
	def makeList(self):
		self.buffer = []
		for item in self.content:
			self.buffer.append(item.makeList()+"\t"+self.position)
		return "".join(self.buffer)