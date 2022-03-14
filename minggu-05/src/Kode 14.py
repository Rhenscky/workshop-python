import math
print('The value of pi is approximately %5.3f.' % math.pi)
f = open('workfile', 'w')
with open('workfile') as f:
    read_data = f.read()
f.closed
f.close()
f.read()
f.read()
f.read()
f.readline()
f.readline()
f.readline()