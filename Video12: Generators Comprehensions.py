g = (i for i in range(4))
for i in g:
    print(i)

g2 = (i for i in range(4) if i%2==0)
for i in g2:
    print(i)

g3 = (i if i%2==0 else i*i for i in range(4))
for i in g3:
    print(i)
