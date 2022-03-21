# INPUT DAN OUTPUT PADA PYTHON
Input adalah masukan yang kita berikan ke program.
Program akan memprosesnya dan menampilkan hasil outputnya.
Input, proses, dan output adalah inti dari semua program komputer.


## Pemformatan Keluaran
Pemformatan adalah penambahan sentuhan pada teks untuk membuat teks mudah dibaca dan lebih menarik.
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


## F-string
Interpolasi String Literal atau lebih umum sebagai F-string (karena karakter f awal mendahului string literal). Ide dibalik f-string adalah untuk membuat interpolasi string lebih sederhana. 
Untuk membuat f-string, awali string dengan huruf “ f ”. 
    String itu sendiri dapat diformat dengan cara yang sama seperti yang Anda lakukan dengan str.format(). F-string menyediakan cara ringkas dan nyaman untuk menyematkan ekspresi python di dalam literal string untuk pemformatan
F-string lebih cepat daripada dua mekanisme pemformatan string yang paling umum digunakan, yaitu % formatting dan str.format(). 
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

## Pemformatan String ( str.format)
Pemformatan string "gaya baru" ini menghilangkan %sintaks khusus -operator dan membuat sintaks untuk pemformatan string lebih teratur. Pemformatan sekarang ditangani dengan memanggil .format()objek string .
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
Metode str.rjust() dari objek string merata-kanan-kan sebuah string dalam bidang dengan lebar tertentu dengan menambahkannya dengan spasi di sebelah kiri.
Ada metode lain, str.zfill(), yang melapisi string numerik di sebelah kiri dengan nol.
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

## Pemformatan String (% Operator)
String dalam Python memiliki operasi bawaan unik yang dapat diakses dengan %operator. Ini memungkinkan Anda melakukan pemformatan posisi sederhana dengan sangat mudah.
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
Untuk membaca konten file, panggil f.read(size), yang membaca sejumlah kuantitas data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). size adalah argumen numerik opsional. Jika akhir file telah tercapai, f.read() akan mengembalikan string kosong ('').

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

## JSON
Python memiliki paket bawaan yang disebut json, yang dapat digunakan untuk bekerja dengan data JSON.
#### ```Kode 17```
```
import json
json.dumps([1, 'simple', 'list'])
json.dump(x, f)
x = json.load(f)
```

## Kesimpulan
Fungsi input() untuk memberi jeda atau menghentikan sementara program sampai kita memasukkan data ke dalamnya, ketika data sudah dimasukkan, selanjutnya program akan berjalan kembali dan kemudian memproses data inputan.
Setelah data dimasukkan lalu diproses  menggunakan fungsi print(). fungsi print() juga dapat menginformasikan pada kita versi python yang digunakan suatu program. Jadi jika kalian menemukan program dengan deklarasi print() di dalamnya maka dapat dipastikan program tersebut sudah menggunakan versi python 3 ke atas. Sedangkan jika di dalam program tersebut ditemukan deklarasi print tanpa tanda kurung, maka dapat dipastikan program tersebut menggunakan python versi lama. Python 2.7 ke bawah.


