import Graph

def main():
	nokogiri = Graph.Nokogiri('nokogiri')
	nokogiri.set_graph()
	nokogiri.graph()
	nokogiri.write_graph()
	
	cos = Graph.Cos('cos')
	cos.set_graph()
	cos.graph()
	cos.write_graph()

	sin = Graph.Sin('sin')
	sin.set_graph()
	sin.graph()
	sin.write_graph()


if __name__=='__main__':
	main()
