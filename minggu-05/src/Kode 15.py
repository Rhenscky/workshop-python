for line in f:
    print(line, end='')
f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)