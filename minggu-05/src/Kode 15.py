for line in f:
    print(line, end='')
f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)  
f.write(s)
