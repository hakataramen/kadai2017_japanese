import CaboCha
import sys

c = CaboCha.Parser()

sentense = "豊工に行っています。"

print (c.parseToString(sentense))
