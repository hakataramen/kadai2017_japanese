import CaboCha

c = CaboCha.Parser()

sentense="豊工に行っています。"

tree = c.parse(sentense)

#print(c.parseToString(sentense))

#print(tree.toString(CaboCha.FORMAT_TREE))
print(tree.toString(CaboCha.FORMAT_LATTICE))
