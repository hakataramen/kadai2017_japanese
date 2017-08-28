import sys
import MeCab

text = sys.argv[1]

if len(sys.argv) < 2:
        exit()

tagger = MeCab.Tagger('mecabric')
tagger.parse('')
Node = tagger.parseToNode(text)
while Node:
        feature = Node.feature.split(",")

        print(Node.surface, feature[0], feature[6])
        Node = Node.next
