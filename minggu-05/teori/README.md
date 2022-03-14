# INPUT DAN OUTPUT PADA PYTHON
Input adalah masukan yang kita berikan ke program.
Program akan memprosesnya dan menampilkan hasil outputnya.
Input, proses, dan output adalah inti dari semua program komputer.


## Pemformatan Keluaran yang Lebih Menarik
#### ```Kode 1```
```
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
```
#### ```Kode 2```
```
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
```
#### ```Kode 3```
```
s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
repr((x, y, ('spam', 'eggs')))
```


## Literal String Terformat
#### ```Kode 4```
```
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
```
#### ```Kode 5```
```
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
```
#### ```Kode 6```
```
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
```

## Metode String format()
#### ```Kode 7```
```
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
```
#### ```Kode 8```
```
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
```
#### ```Kode 9```
```
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
```
#### ```Kode 10```
```
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
```

## Pemformatan String Manual
#### ```Kode 11```
```
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
```
#### ```Kode 12```
```
'12'.zfill(5)
'-3.14'.zfill(7)
'3.14159265359'.zfill(5)
```

## Pemformatan string lama
#### ```Kode 13```
```
import math
print('The value of pi is approximately %5.3f.' % math.pi)
f = open('workfile', 'w')
with open('workfile') as f:
    read_data = f.read()
f.closed
f.close()
f.read()
```

## Metode Objek Berkas
#### ```Kode 14```
```
f.read()
f.read()
f.readline()
f.readline()
f.readline()
```
#### ```Kode 15```
```
for line in f:
    print(line, end='')
f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)
f.write(s)
```
#### ```Kode 16```
```
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5) 
f.read(1)
f.seek(-3, 2)  
f.read(1)
```

## Menyimpan data terstruktur dengan
#### ```Kode 17```
```
import json
json.dumps([1, 'simple', 'list'])
json.dump(x, f)
x = json.load(f)
```

## Kesimpulan



