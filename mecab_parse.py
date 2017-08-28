import sys
import MeCab

text = sys.argv[1]

if len(sys.argv) < 2:
    print("引数不足")
    exit()


m = MeCab.Tagger(text)

text_parsed = m.parse(text)

print(text_parsed)
