import cal
class Add(cal.Cal):
	def __init__(self,x,y):
		super(Add,self).__init__('+',x,y)
	def cal_add(self):
		self.answer = self.x+self.y
			