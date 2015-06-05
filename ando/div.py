import cal

class Div(cal.Cal):
	def __init__(self, x, y):
		super(Div,self).__init__("/",x,y)

	def cal_div(self):
		self.answer = float(self.x) / self.y 