# coding:utf-8

class Battleship(object):
	def __init__(self,main_weapon):
		self.main_weapon=main_weapon
	def fire():
		pass

class Yamato(Battleship):
	def __init__(self):
		super(Yamato,self).__init__("46cm三連装砲")
	def fire(self):
		print self.main_weapon+"、敵を薙ぎ払え！！"

class Nagato(Battleship):
	def __init__(self):
		super(Nagato,self).__init__("41cm連装砲")
	def fire(self):
		print self.main_weapon+"、撃てぇ！！"

class Kongo(Battleship):
	def __init__(self):
		super(Kongo,self).__init__("35.6cm連装砲")
	def fire(self):
		print self.main_weapon+"、全砲門Fire！！"

def main():
	yamato = Yamato()
	yamato.fire()
	nagato = Nagato()
	nagato.fire()
	kongo = Kongo()
	kongo.fire()

if __name__=="__main__":
	main()