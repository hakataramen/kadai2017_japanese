import CaboCha

c = CaboCha.Parser('-n1')

sentense="花子と太郎が東京にいます。"

tree = c.parse(sentense)

#print(c.parseToString(sentense))

#print(tree.toString(CaboCha.FORMAT_TREE))
print(tree.toString(CaboCha.FORMAT_LATTICE))
for i in range(tree.token_size()):
    token = tree.token(i)
    print('Surface:', token.surface)
#   print(' Normalized:', token.normalized_surface)
#   print(' Feature:', token.feature)
    print(' NE:', token.ne) # 固有表現
#   print(' Info:', token.additional_info)
#   print(' Chunk:', token.chunk)
    
