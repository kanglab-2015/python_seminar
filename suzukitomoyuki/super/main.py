# coding:utf-8 

import sys
from factory import *

if __name__=="__main__":
	factory = Factory.getFactory(sys.argv[1])

	ootomo = factory.createName("大友")
	mizuno = factory.createName("水野")
	abe = factory.createName("安倍")
	ishihara = factory.createName("石原")
	okazaki = factory.createName("岡崎")
	emoto = factory.createName("江本")

	yakusyoku_ootomo = factory.createPosition("組長")
	yakusyoku_ootomo.add(ootomo)
	yakusyoku_mizuno = factory.createPosition("若頭")
	yakusyoku_mizuno.add(mizuno)
	yakusyoku_abe = factory.createPosition("幹部")
	yakusyoku_abe.add(abe)
	yakusyoku_ishihara = factory.createPosition("若衆/金庫番")
	yakusyoku_ishihara.add(ishihara)
	yakusyoku_wakaino = factory.createPosition("若衆")
	yakusyoku_wakaino.add(okazaki)
	yakusyoku_wakaino.add(emoto)

	group = factory.createGroup("大友")
	group.add(yakusyoku_ootomo)
	group.add(yakusyoku_mizuno)
	group.add(yakusyoku_abe)
	group.add(yakusyoku_ishihara)
	group.add(yakusyoku_wakaino)
	group.output_file()
	group.output_console()
